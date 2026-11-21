import pandas as pd
print(pd.__version__)
print("Miemie")
sales_data={
    "product": ["A", "B", "C"],
    "quantity": [3, 2, 5],
    "price": [100, 300, 500]
}
df = pd.DataFrame(sales_data)
print(df)