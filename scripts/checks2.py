import pandas as pd

d = "data/raw/"
orders = pd.read_csv(d + "olist_orders_dataset.csv")
items = pd.read_csv(d + "olist_order_items_dataset.csv")
payments = pd.read_csv(d + "olist_order_payments_dataset.csv")
reviews = pd.read_csv(d + "olist_order_reviews_dataset.csv")

no_items = orders[~orders["order_id"].isin(items["order_id"])]
print("Orders with no items:", len(no_items))
print(no_items["order_status"].value_counts())

pay_counts = payments.groupby("order_id").size()
print("\nOrders with 2+ payment rows:", (pay_counts > 1).sum())

rev_counts = reviews.groupby("order_id").size()
print("Orders with 2+ reviews:", (rev_counts > 1).sum())

delivered = orders[orders["order_status"] == "delivered"]
print("\nDelivered but no delivery date:",
      delivered["order_delivered_customer_date"].isna().sum())