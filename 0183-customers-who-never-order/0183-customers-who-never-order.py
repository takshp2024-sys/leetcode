import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Perform a left merge on 'id' and 'customerId'
    merged = pd.merge(customers, orders, left_on='id', right_on='customerId', how='left')
    
    # Filter for customers where the order id is null (meaning they never ordered)
    result = merged[merged['customerId'].isna()]
    
    # Select and rename the column to match the required output
    return result[['name']].rename(columns={'name': 'Customers'})