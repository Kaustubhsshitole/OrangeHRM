import logging
import os
import datetime
from utils.config_reader import ConfigReader

class LoggerUtil:
    _logger = None

    @staticmethod
    def get_logger():
        """Returns single synchronized logger instance outputting to terminal and file."""
        if LoggerUtil._logger is None:
            config = ConfigReader.get_config()
            log_dir = config["framework"]["paths"]["logs"]
            if not os.path.exists(log_dir):
                os.makedirs(log_dir)
                
            log_file = os.path.join(log_dir, f"automation_{datetime.datetime.now().strftime('%Y%m%d')}.log")
            
            LoggerUtil._logger = logging.getLogger("OrangeHRM_Automation")
            LoggerUtil._logger.setLevel(logging.DEBUG)
            
            if not LoggerUtil._logger.handlers:
                # File Handler
                fh = logging.FileHandler(log_file, encoding="utf-8")
                fh.setLevel(logging.DEBUG)
                
                # Console Handler
                ch = logging.StreamHandler()
                ch.setLevel(logging.INFO)
                
                # Format setup
                formatter = logging.Formatter('%(asctime)s [%(levelname)8s] %(message)s (%(filename)s:%(lineno)s)', '%Y-%m-%d %H:%M:%S')
                fh.setFormatter(formatter)
                ch.setFormatter(formatter)
                
                LoggerUtil._logger.addHandler(fh)
                LoggerUtil._logger.addHandler(ch)
                
        return LoggerUtil._logger