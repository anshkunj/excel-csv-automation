import pandas as pd
import glob

# Load all Excel files
files = glob.glob("sample_files/excel_inputs/*.xlsx")

dataframes = [pd.read_excel(file) for file in files]

# Merge all files
merged_df = pd.concat(dataframes, ignore_index=True)

# Save merged output
merged_df.to_excel("sample_files/merged_output.xlsx", index=False)

print("Excel files merged successfully.")
