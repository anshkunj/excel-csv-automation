import pandas as pd

# Load raw CSV file
df = pd.read_csv("sample_files/raw_data.csv")

# Clean column names
df.columns = df.columns.str.strip().str.lower()

# Remove duplicates
df = df.drop_duplicates()

# Handle missing values
df = df.fillna("")

# Save cleaned data to Excel
df.to_excel("sample_files/cleaned_data.xlsx", index=False)

print("CSV cleaned and exported to Excel successfully.")
