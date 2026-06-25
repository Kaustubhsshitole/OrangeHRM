

 Directory Structure

```text
project_root/
├── pages/                   # Page Object files mapping elements and actions
│   ├── base_page.py         # Standard wrapper for actions and waiters
│   ├── login_page.py        # Mappings and auth flow for main entry page
│   ├── admin/               # Admin module sub-pages
│   ├── pim/                 # PIM employee management sub-pages
│   ├── leave/               # Leave application and tracking sub-pages
│   ├── time/                # Timesheets and attendance sub-pages
│   ├── recruitment/         # Candidate tracking sub-pages
│   ├── performance/         # KPI reviews sub-pages
│   ├── dashboard/           # Main landing metrics sub-pages
│   ├── directory/           # Employee directory sub-pages
│   ├── maintenance/         # Secure purging sub-pages
│   ├── claim/               # Expense claims sub-pages
│   └── buzz/                # Internal social sub-pages
│
├── tests/                   # Parallelizable pytest verification files
│   ├── admin/
│   ├── pim/
│   └── ...
│
├── utils/                   # Shared infrastructure wrappers (drivers, loggers, media)
│   ├── driver_manager.py
│   ├── screenshot_util.py
│   ├── video_recorder.py
│   └── ...
│
├── screenshots/             # Output directories for execution images
│   ├── passed/
│   └── failed/
│
├── videos/                  # Timestamped full-session execution AVI clips
├── reports/                 # Static HTML and interactive Allure data
├── logs/                    # Formatted INFO, DEBUG, ERROR trace logs
└── testdata/
    └── master_config.json   # Unified JSON controlling the entire suite
```


