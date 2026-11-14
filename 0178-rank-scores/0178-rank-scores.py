import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    # Calculate the dense rank of the scores in descending order
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)
    
    # Sort the DataFrame by score in descending order
    result = scores.sort_values(by='score', ascending=False)
    
    # Return only the required columns
    return result[['score', 'rank']]