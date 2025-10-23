# Data Directory

This directory should contain the datasets required for the medallion analysis notebooks.

## Required Data Files

### 1. Medallion Transfer Data
**File**: `february_2023_medallion_price_list.xls`

**Source**: NYC Taxi & Limousine Commission (TLC) - Medallion Transfer Reports

**Download**: [NYC TLC Medallion Transfers](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)

**Description**:
- Excel file containing multiple sheets (one per month)
- Each sheet contains medallion transfer/sale transactions
- Includes pricing, transaction type, and medallion classification
- Date range: March 2017 - February 2023

**Columns**:
- Medallion Classification (Unrestricted, Wheelchair Accessible, Alternative Fuel)
- Prices (total transaction price)
- Notes (Foreclosure, Estate, Bankruptcy, etc.)
- Number of Medallions

### 2. Monthly Ride Data
**File**: `data_reports_monthly.csv`

**Source**: NYC TLC - Aggregated Reports

**Download**: [NYC TLC Aggregated Reports](https://www.nyc.gov/site/tlc/about/aggregated-reports.page)

**Description**:
- Monthly statistics by license class
- Covers Yellow, Green, and various FHV (For-Hire Vehicle) categories
- Operational metrics including trips, revenue, and vehicle/driver counts

**Columns**:
- Month/Year
- License Class
- Trips Per Day
- Farebox Per Day
- Unique Drivers
- Unique Vehicles
- Vehicles Per Day
- Avg Days Vehicles on Road
- Avg Hours Per Day Per Vehicle
- Avg Days Drivers on Road
- Avg Hours Per Day Per Driver
- Avg Minutes Per Trip
- Percent of Trips Paid with Credit Card
- Trips Per Day Shared

## Data Preparation

After downloading the required files:

1. Place them in this `data/` directory
2. Ensure file names match exactly as listed above
3. Run the notebooks in sequential order (01-06)

## Data Privacy & Terms

All data used in this project is publicly available from the NYC TLC and subject to their terms of use. This project does not redistribute the raw data files; users must download them independently.

## Alternative Data Sources

If the NYC TLC data structure has changed or files are unavailable:

1. Check the [NYC Open Data Portal](https://opendata.cityofnewyork.us/)
2. Search for "TLC" or "Taxi" datasets
3. Look for monthly aggregated reports by license class
4. Adapt the notebook code if column names have changed

## File Size Notes

The data files are excluded from version control due to their size:
- `february_2023_medallion_price_list.xls`: ~500KB-1MB
- `data_reports_monthly.csv`: ~100-500KB

Total data directory size should be under 2MB.
