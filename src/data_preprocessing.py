import pandas as pd

df = pd.read_csv(
    "data/raw/Mall_Customers.csv"
)

df = df[
    [
        "Age",
        "Annual Income (k$)",
        "Spending Score (1-100)"
    ]
]

df.to_csv(
    "data/processed/cleaned_data.csv",
    index=False
)

print("Data preprocessing completed.")