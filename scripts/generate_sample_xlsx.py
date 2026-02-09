import pandas as pd

data = {
    "product": ["A", "C"],
    "quantity": [800, 4],
    "revenue": [4500, 500]
}

df = pd.DataFrame(data)

df.to_excel(
    "sample_files/excel_inputs/sales_feb.xlsx",
    index=False
)
