import pandas as pd
from encoder import classify_columns, suggest_encoding, rare_encode_dataframe


data = {
    "age": [20, 21, 22, 23, 24, 25, 26, 27],
    "gender": ["M", "F", "M", "F", "M", "F", "M", "F"],
    "department": ["IT", "HR", "Finance", "IT", "HR", "IT", "Finance", "HR"],
    "city": ["Baku", "Ganja", "Baku", "Sumqayit", "Sheki", "Baku", "Quba", "RareCity"],
    "status": ["active", "inactive", "active", "active", "inactive", "active", "active", "inactive"]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print()

print("Column Groups:")
groups = classify_columns(df)
print(groups)
print()

print("Encoding Suggestions:")
plan = suggest_encoding(df)
for column, recommendation in plan.items():
    print(f"{column}: {recommendation}")
print()

print("After Rare Encoding on 'city':")
df = rare_encode_dataframe(df, ["city"], threshold=0.15)
print(df)