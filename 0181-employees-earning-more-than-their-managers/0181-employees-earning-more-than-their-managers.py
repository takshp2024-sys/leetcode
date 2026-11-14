import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    # Merge the dataframe with itself on managerId (left) and id (right)
    merged = pd.merge(employee, employee, left_on='managerId', right_on='id', suffixes=('', '_manager'))
    
    # Filter employees whose salary is greater than their manager's salary
    result = merged[merged['salary'] > merged['salary_manager']]
    
    # Select and rename the column to match the expected output
    return result[['name']].rename(columns={'name': 'Employee'})