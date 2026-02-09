import pandas as pd

# Load cleaned data
df = pd.read_excel("sample_files/cleaned_data.xlsx")

# Generate summary report
summary = {
    "Total Rows": len(df),
    "Total Columns": len(df.columns)
}

report_df = pd.DataFrame([summary])

# Save report
report_df.to_excel("sample_files/report.xlsx", index=False)

print("Report generated successfully.")
