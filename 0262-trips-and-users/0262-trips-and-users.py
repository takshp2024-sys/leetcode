import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    # Filter out banned users
    unbanned_users = users[users['banned'] == 'No']['users_id']
    
    # Filter trips where both client and driver are unbanned
    valid_trips = trips[
        (trips['client_id'].isin(unbanned_users)) & 
        (trips['driver_id'].isin(unbanned_users)) &
        (trips['request_at'] >= '2013-10-01') & 
        (trips['request_at'] <= '2013-10-03')
    ]
    
    # Create a column indicating if the trip was canceled
    valid_trips['is_canceled'] = valid_trips['status'] != 'completed'
    
    # Group by date and calculate the cancellation rate
    result = valid_trips.groupby('request_at').agg(
        total=('id', 'count'),
        canceled=('is_canceled', 'sum')
    ).reset_index()
    
    # Calculate the rate and format
    result['Cancellation Rate'] = (result['canceled'] / result['total']).round(2)
    
    # Rename and select the required columns
    result.rename(columns={'request_at': 'Day'}, inplace=True)
    return result[['Day', 'Cancellation Rate']]