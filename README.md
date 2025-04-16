
# OBD-Style Data Processing Pipeline 🚗📊

This project simulates a vehicle emissions compliance pipeline using Python and Power BI. It processes OBD-style logs, flags emission risks, and generates summary Excel reports and visualizations.

## Features

- Simulated vehicle log generation
- Emission risk detection based on thresholds
- Summary reports and pivot tables in Excel
- Visual analysis support for Power BI

## Folder Structure

```
OBD_Data_Pipeline/
│
├── data/
│   ├── raw_logs/         # Simulated raw vehicle logs
│   └── processed/        # Cleaned and processed logs
│
├── outputs/
│   └── reports/          # Excel reports with summaries and pivots
│
├── scripts/              # Python processing script
├── powerbi/              # Power BI visual files (placeholder)
├── notebooks/            # Jupyter notebooks (optional)
└── README.md
```

## How to Run

1. Install dependencies:
```bash
pip install pandas openpyxl
```

2. Run the processor script:
```bash
cd scripts
python process_obd_logs.py
```

3. Open the Excel report from `outputs/reports/emissions_report.xlsx`.

## Power BI

Use the exported Excel report to build visual dashboards in Power BI.

## Author

Anushka Dhole – [GitHub](https://github.com/anushkadhole)
