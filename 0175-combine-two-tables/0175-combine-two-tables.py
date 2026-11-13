import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    # Perform a left merge on 'personId'
    merged = pd.merge(person, address, on='personId', how='left')
    
    # Select and return only the required columns
    return merged[['firstName', 'lastName', 'city', 'state']]