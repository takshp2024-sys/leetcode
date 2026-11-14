import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # Merge the two dataframes
    merged = pd.merge(employee, department, left_on='departmentId', right_on='id', suffixes=('_emp', '_dept'))
    
    # Find the max salary per department and broadcast it
    max_salaries = merged.groupby('departmentId')['salary'].transform('max')
    
    # Filter for employees whose salary matches the max in their department
    result = merged[merged['salary'] == max_salaries]
    
    # Select and rename the required columns
    return result[['name_dept', 'name_emp', 'salary']].rename(
        columns={'name_dept': 'Department', 'name_emp': 'Employee', 'salary': 'Salary'}
    )