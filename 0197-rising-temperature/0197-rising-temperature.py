import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    # Convert 'recordDate' to datetime to allow date arithmetic
    weather['recordDate'] = pd.to_datetime(weather['recordDate'])
    
    # Sort by 'recordDate' to ensure chronological order (often a good practice)
    weather = weather.sort_values('recordDate')
    
    # Shift the columns by 1 to bring yesterday's data to today's row
    weather['prev_temp'] = weather['temperature'].shift(1)
    weather['prev_date'] = weather['recordDate'].shift(1)
    
    # Calculate the difference in days between today and yesterday
    weather['day_diff'] = (weather['recordDate'] - weather['prev_date']).dt.days
    
    # Filter for rows where the day difference is 1 and today's temp is higher
    result = weather[(weather['day_diff'] == 1) & (weather['temperature'] > weather['prev_temp'])]
    
    # Return only the 'id' column
    return result[['id']]