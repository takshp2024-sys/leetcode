import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # Merge employee and department tables
    merged = pd.merge(employee, department, left_on='departmentId', right_on='id', suffixes=('_emp', '_dept'))
    
    # Calculate dense rank of salaries within each department
    merged['rnk'] = merged.groupby('departmentId')['salary'].rank(method='dense', ascending=False)
    
    # Filter for top 3 ranks
    result = merged[merged['rnk'] <= 3]
    
    # Select and rename required columns
    return result[['name_dept', 'name_emp', 'salary']].rename(
        columns={'name_dept': 'Department', 'name_emp': 'Employee', 'salary': 'Salary'}
    )