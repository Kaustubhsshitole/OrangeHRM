<<<<<<< HEAD
# OrangeHRM11
=======
# Enterprise-Level Python Automation Testing Framework for OrangeHRM

A highly scalable, robust, and maintainable test automation framework designed for the **OrangeHRM** application. Follows the **Page Object Model (POM)** pattern, implementing full end-to-end multi-module UI automation, data-driven parameters, and runtime media logs.

## 🛠️ Tech Stack & Key Features

* **Language:** Python 3.10+
* **Engine:** Selenium WebDriver (Cross-browser options for Chrome, Edge, and Firefox)
* **Runner:** PyTest (Supports parallel executing via `pytest-xdist`)
* **Architecture:** Page Object Model (POM) separating UI mappings from tests
* **Data-Driven:** Single `master_config.json` file controlling URLs, browsers, test metrics, and expected validations
* **Media Logging:** Automatic screenshots on success/failure and live-action AVI screen recording via opencv thread
* **Reporting:** Integrated PyTest HTML Reports and detailed Allure Dashboard integration

---

## 📂 Directory Structure

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

---

## 🚀 Getting Started

### 1. Prerequisites
Install all core libraries in your virtual environment:
```bash
pip install -r requirements.txt
```

### 2. Configure Settings
Modify `testdata/master_config.json` to customize execution parameters:
* Toggle `browser` (chrome / firefox / edge)
* Set `headless` mode (true / false)
* Set usernames, credentials, and mock payloads for employee directories.

### 3. Execution Commands

**Run Entire Suite in Parallel:**
```bash
pytest -n auto
```

**Run Specific Modules:**
```bash
pytest tests/admin/
pytest tests/pim/test_pim_employee_list.py
```

**Generate and View Allure Reports:**
```bash
allure serve reports/allure-results
```

**Generate Static HTML Report:**
The static report is output automatically to `reports/report.html`.
>>>>>>> 79a5655 (Initial project upload)
