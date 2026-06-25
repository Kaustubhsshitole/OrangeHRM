import os
import threading
import time
import numpy as np
from PIL import ImageGrab
import cv2

class VideoRecorder(threading.Thread):
    def __init__(self, filename, fps=8):
        """Initializes a background recording thread leveraging PIL capture and OpenCV."""
        super().__init__()
        self.filename = filename
        self.fps = fps
        self.running = False
        self._stop_event = threading.Event()
        
        dirname = os.path.dirname(filename)
        if dirname and not os.path.exists(dirname):
            os.makedirs(dirname)

    def run(self):
        self.running = True
        try:
            screen = ImageGrab.grab()
            width, height = screen.size
        except Exception:
            # Fallback size if display capture fails
            width, height = 1920, 1080
            
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(self.filename, fourcc, self.fps, (width, height))
        
        interval = 1.0 / self.fps
        last_time = time.time()
        
        while not self._stop_event.is_set():
            curr_time = time.time()
            elapsed = curr_time - last_time
            if elapsed < interval:
                time.sleep(interval - elapsed)
                
            last_time = time.time()
            
            try:
                img = ImageGrab.grab()
                frame = np.array(img)
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                out.write(frame)
            except Exception:
                pass
                
        out.release()
        self.running = False

    def stop(self):
        self._stop_event.set()
        if self.is_alive():
            self.join()