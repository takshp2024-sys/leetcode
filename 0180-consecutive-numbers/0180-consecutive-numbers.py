import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    # Shift the 'num' column to create 'prev1' and 'prev2'
    logs['prev1'] = logs['num'].shift(1)
    logs['prev2'] = logs['num'].shift(2)
    
    # Filter rows where num == prev1 == prev2
    result = logs[(logs['num'] == logs['prev1']) & (logs['num'] == logs['prev2'])]
    
    # Get unique consecutive numbers and format the output
    consecutive_nums = result['num'].unique()
    
    return pd.DataFrame({'ConsecutiveNums': consecutive_nums})