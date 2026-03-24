# Automated-Sales-Report-System

A simple Python project that reads sales records from a CSV file and generates a text-based sales report.

## Project Structure

- `main.py` - Main script to load data and generate a report
- `sales_data.csv` - Sample sales dataset
- `requirements.txt` - Python dependencies

## Features

- Validates input CSV schema
- Computes total units and total revenue
- Shows top products by revenue
- Summarizes revenue by region and month
- Saves report to `sales_report.txt`

## Setup

1. Create and activate a virtual environment (optional but recommended)
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

Optional arguments:

```bash
python main.py --input sales_data.csv --output sales_report.txt
```

## Expected CSV Columns

- `date` (YYYY-MM-DD)
- `product`
- `region`
- `units`
- `unit_price`
