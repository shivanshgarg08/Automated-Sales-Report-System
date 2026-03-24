import pandas as pd
import random
from datetime import datetime, timedelta

stores = [f"S{i}" for i in range(1, 11)]
products = ["Milk", "Bread", "Coke", "Pepsi", "Chips"]

data = []

for _ in range(300):
    store = random.choice(stores)
    product = random.choice(products)
    sales = random.randint(20, 500)

    date = datetime.now() - timedelta(days=random.randint(0, 10))

    data.append([store, product, sales, date.strftime("%Y-%m-%d")])

df = pd.DataFrame(data, columns=["store_id", "product", "sales", "date"])

df.to_csv("sales_data.csv", index=False)

print("✅ 300 records generated in sales_data.csv")