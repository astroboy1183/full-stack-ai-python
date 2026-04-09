'''

You're creating a monthly report for a cafe's sales.
Instead of putting all logic in one place, break it down.

Task:

Write a function generate_report() that calls:
fetch_sales()
filter_valid_orders()
summarize_data()

'''

def fetch_sales():
    print("Fetching sales data...")
    # Simulate fetching data
    return [{"order_id": 1, "amount": 150}, {"order_id": 2, "amount": 200}, {"order_id": 3, "amount": -50}] 

def filter_valid_orders(sales_data):
    print("Filtering valid orders...")
    return [order for order in sales_data if order["amount"] > 0]

def summarize_data(filtered_orders):
    print("Summarizing data...")
    total_sales = sum(order["amount"] for order in filtered_orders)
    print(f"Total sales: {total_sales}")

def generate_report():
    sales_data = fetch_sales()
    valid_orders = filter_valid_orders(sales_data)
    summarize_data(valid_orders)

generate_report()
