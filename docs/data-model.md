## Data-quality findings

- 775 orders have no rows in order_items. Most are `unavailable` (603) or `canceled`
  (164); 8 are `created`, `invoiced` or `shipped`, which is unexpected. Joins from
  orders to items must be LEFT JOINs if these orders should be kept in counts.
- 2,961 orders have more than one payment row, so payments must be aggregated to one
  row per order before joining. One order has no payment at all.
- 547 orders have more than one review, 768 orders have none, and some `review_id`s
  repeat. Reviews will be deduplicated in staging (latest review per order).
- 8 orders are marked `delivered` but have no delivery date. They will be excluded from
  delivery-time metrics.
- Geolocation has about 50 readings per zip prefix on average and must be reduced to one
  row per zip prefix before joining.
- `customer_id` appears to be generated per order; real customers are identified by
  `customer_unique_id` (96,096 customers across 99,441 orders).
- Source column names contain typos (for example `product_name_lenght`).