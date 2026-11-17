import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # Sort the DataFrame by 'id' ascending to ensure the smallest id is kept
    person.sort_values('id', inplace=True)
    
    # Drop duplicates based on the 'email' column, keeping the first occurrence
    # Since we sorted by 'id', the first occurrence will be the smallest id
    person.drop_duplicates(subset=['email'], keep='first', inplace=True)