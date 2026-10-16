import pandas as pd

d = "data/raw/"
orders = pd.read_csv(d + "olist_orders_dataset.csv")
customers = pd.read_csv(d + "olist_customers_dataset.csv")
items = pd.read_csv(d + "olist_order_items_dataset.csv")
payments = pd.read_csv(d + "olist_order_payments_dataset.csv")
reviews = pd.read_csv(d + "olist_order_reviews_dataset.csv")
geo = pd.read_csv(d + "olist_geolocation_dataset.csv")

print("orders: rows", len(orders), "| unique order_id", orders["order_id"].nunique())
print("customers: rows", len(customers),
      "| unique customer_id", customers["customer_id"].nunique(),
      "| unique customer_unique_id", customers["customer_unique_id"].nunique())
print("items: rows", len(items), "| unique order_id", items["order_id"].nunique())
print("payments: rows", len(payments), "| unique order_id", payments["order_id"].nunique())
print("reviews: rows", len(reviews),
      "| unique order_id", reviews["order_id"].nunique(),
      "| unique review_id", reviews["review_id"].nunique())
print("geolocation: rows", len(geo), "| unique zip prefixes", geo["geolocation_zip_code_prefix"].nunique())

print("\nMissing values in orders:")
print(orders.isna().sum())

print("\nOrder statuses:")
print(orders["order_status"].value_counts())