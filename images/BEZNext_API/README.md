# BEZNext API — Query Performance Tuning Dashboard

A Django-based web application for analyzing and comparing query performance across **Snowflake** and **Teradata** data warehouses, with **Oracle** integration for workload metadata.

---

## Overview

This tool was built to support database performance tuning workflows. It provides a unified interface to query execution history from multiple database platforms, displaying performance metrics such as CPU time, I/O, elapsed time, and bytes processed — with statistics like averages and standard deviations across query sets.

---

## Features

### Multi-Database Query Analysis
- **Snowflake** — Queries `ACCOUNT_USAGE.QUERY_HISTORY` to surface query performance data including bytes scanned, elapsed time, spill to local/remote storage, network usage, compile time, and execution time.
- **Teradata** — Queries `DBQLOGTBL_HST_V` and `dbqlutilitytbl_hst_v` to surface CPU parse/execution times, logical/physical I/O, elapsed time, and execution time.

### Oracle Workload Integration
- Connects to an Oracle database (BEZNext workload management system) to look up:
  - **System names** and **System IDs** from the workload model
  - **Ruleset names** linked to each system
  - **AppIDs and Usernames** from `model_session_metrics` — used to filter Teradata queries to specific workloads

### Query Filtering & Controls
- **Date range picker** — filter queries by start and end datetime
- **Warehouse selector** — filter Snowflake queries by warehouse name
- **System/Ruleset selector** — filter Teradata queries using Oracle workload metadata
- **Sort column** — sort results by CPU time, I/O, elapsed time, etc.
- **Result limit** — cap the number of rows returned

### Performance Statistics
For both the full result set and the limited/selected rows, the dashboard calculates:
- **Subtotal** — sum of CPU time, I/O (MB), and elapsed time
- **Average** — mean values across all returned queries
- **Standard Deviation** — variability across the query set

### Query Text Popup
- Click any **Query ID** in the results table to open a popup showing the full SQL text for that query, fetched live from Snowflake or Teradata.

### Logging
Rotating log files (max 2MB each) are written to a `logs/` directory:
- `Snowflake.log` — Snowflake query activity
- `Teradata.log` — Teradata query activity
- `Oracle.log` — Oracle connection and query activity
- `Server.log` — Django server/request activity
- `Queries.log` — General query log

---

## Tech Stack

| Layer | Technology |
|---|---|
| Web Framework | Django 3.2 |
| Data Processing | pandas |
| Snowflake Connector | snowflake-connector-python |
| Teradata Connector | teradatasql |
| Oracle Connector | cx_Oracle / Django Oracle backend |
| Frontend | HTML/CSS/JS (Django templates) |
| Dev Tooling | django-debug-toolbar |

---

## Project Structure

```
GetDataForTuning/
└── RestApi_SF_BEZ/
    ├── manage.py                        # Django entry point
    ├── config.py                        # DB connection params & query placeholders
    ├── queries.py                       # SQL query definitions (Snowflake, Teradata, Oracle)
    ├── RestApi_SF_BEZ/
    │   ├── settings.py                  # Django settings, DB config, logging
    │   ├── urls.py                      # URL routing
    │   └── wsgi.py                      # WSGI entry point
    ├── RestApi/
    │   └── views.py                     # Core request handling & data processing logic
    ├── Queries/
    │   ├── RunQueries.py                # DB connection & query execution (SF, TD, Oracle)
    │   └── formatQueries.py            # Data formatting utilities
    ├── Oracle_exe/
    │   ├── GetDropdown.py              # Oracle: fetch system names, rulesets, system IDs
    │   └── warehouse_dropdown.py       # Oracle: fetch Snowflake warehouse names
    ├── DatetimeConversions/
    │   └── epochtime.py                # Datetime ↔ epoch conversion utilities
    └── logutil/
        └── logger.py                   # Custom rotating file log handler
```

---

## Setup & Running Locally

### Prerequisites
- Python 3.11
- Access to Snowflake, Teradata, and Oracle instances (optional — app starts without them)

### 1. Create and activate a virtual environment
```bash
py -3.11 -m venv GetDataForTuning/RestApi_SF_BEZ/.venv311
# Windows:
GetDataForTuning\RestApi_SF_BEZ\.venv311\Scripts\Activate.ps1
```

### 2. Install dependencies
```bash
# From repo root, using the venv's Python directly:
GetDataForTuning\RestApi_SF_BEZ\.venv311\Scripts\python.exe -m pip install --upgrade pip setuptools wheel
GetDataForTuning\RestApi_SF_BEZ\.venv311\Scripts\python.exe -m pip install -r GetDataForTuning/RestApi_SF_BEZ/requirements.txt
```
> Note: `cx_Oracle` requires [Oracle Instant Client](https://www.oracle.com/database/technologies/instant-client.html) to be installed separately. `gunicorn` is Linux-only and can be excluded on Windows.

### 3. Configure connections
Edit `GetDataForTuning/RestApi_SF_BEZ/config.py` with your database credentials:
- `conn_params` — Snowflake
- `teradata_conn_params` — Teradata
- `oracle_conn_params` — Oracle

### 4. Run the development server
```bash
python GetDataForTuning/RestApi_SF_BEZ/manage.py runserver
```

Open **http://127.0.0.1:8000/** in your browser.

---

## API Endpoints

| URL | Method | Description |
|---|---|---|
| `/` or `/query/` | GET / POST | Main dashboard — render form or execute query |
| `/open_popup/` | GET | Fetch and display full SQL text for a given Query ID |
| `/get_rulesets_for_system/` | GET | Return ruleset names for a given Oracle system name |
| `/get_systemid_for_system/` | GET | Return system ID for a given Oracle system name |

---

## How It Works

1. **User submits the form** with a date range, warehouse, database selection, sort column, and result limit.
2. For **Teradata** queries, the app first queries Oracle to identify the top AppIDs and Usernames active during that window (via `model_session_metrics`), then uses those to filter the Teradata workload log.
3. For **Snowflake** queries, the app queries `ACCOUNT_USAGE.QUERY_HISTORY` directly using the provided filters.
4. Results are returned as a **pandas DataFrame**, statistics are computed, and the data is rendered as an HTML table in the response.
5. Clicking a **Query ID** fires an AJAX call to `/open_popup/`, which fetches the full SQL text from the source database and displays it in a modal.
