import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    # Group by email and count the occurrences
    # We use reset_index() to convert the grouped index back to a column
    counts = person.groupby('email').size().reset_index(name='count')
    
    # Filter for emails that appear more than once
    duplicates = counts[counts['count'] > 1]
    
    # Return the result in the required format
    return duplicates[['email']].rename(columns={'email': 'Email'})