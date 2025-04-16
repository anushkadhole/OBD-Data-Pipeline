
import pandas as pd
import os

# Paths
raw_log_path = '../data/raw_logs/vehicle_logs.csv'
processed_path = '../data/processed/processed_logs.csv'
report_path = '../outputs/reports/emissions_report.xlsx'

# Load raw vehicle logs
df = pd.read_csv(raw_log_path, parse_dates=['timestamp'])

# Apply emissions threshold logic
df['high_rpm_flag'] = df['rpm'] > 3500
df['high_load_flag'] = df['engine_load'] > 85
df['emission_risk'] = df[['high_rpm_flag', 'high_load_flag', 'emission_flag']].any(axis=1)

# Save cleaned data
os.makedirs(os.path.dirname(processed_path), exist_ok=True)
df.to_csv(processed_path, index=False)

# Create summary
summary = df.groupby('vehicle_id').agg(
    total_records=('timestamp', 'count'),
    high_rpm_events=('high_rpm_flag', 'sum'),
    high_load_events=('high_load_flag', 'sum'),
    emission_flags=('emission_flag', 'sum'),
    total_risks=('emission_risk', 'sum')
).reset_index()

# Pivot table for Excel
pivot = pd.pivot_table(df, values='emission_risk', index='vehicle_id', columns=df['timestamp'].dt.date, aggfunc='sum', fill_value=0)

# Export to Excel
with pd.ExcelWriter(report_path) as writer:
    summary.to_excel(writer, sheet_name='Summary', index=False)
    pivot.to_excel(writer, sheet_name='PivotTable')

print(f'Report generated: {report_path}')
