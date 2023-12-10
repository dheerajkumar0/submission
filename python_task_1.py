import pandas as pd


def generate_car_matrix(df)->pd.DataFrame:
    """
    Creates a DataFrame  for id combinations.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values, 
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """
    # Write your logic here
    car_matrix = df.pivot(index='id_1', columns='id_2', values='car').fillna(0)
    car_matrix.values[[range(len(car_matrix))]*2] = 0
    return car_matrix

    return df


def get_type_count(df)->dict:
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    # Write your logic here
    conditon = [(df['car'] <= 15),
                (df['car']>15)&(df['car']<=25),
                (['car']>25)]
    choices = ['low','medium','high']
    df['car_type'] = pd.Series(np.select(condition, choices, default='unknown'), dtpye='category')
    type_count = df['car_type'].value_counts().to_dict()
    sorted_type_count = dict(sorted(type_count.items()))
    return sorted_type_count
    
    return dict()


def get_bus_indexes(df)->list:
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
    # Write your logic here
    
    bus_mean = df['bus'].mean()
    bus_indexes= df[df['bus']>2*bus_mean].index.tolist()
    bus_indexes.sort()
    return bus_indexes
    

    return list()


def filter_routes(df)->list:
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    # Write your logic here
    
    rout_avg_truck = df.groupby('route')[route_avg_truck > 7].index.tolist()
    filtered_routes.sort()
    return filtered_routes

    return list()


def multiply_matrix(matrix)->pd.DataFrame:
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
    # Write your logic here
    
    modified_matrix = car_matrix.copy()
    modified_matrix[modified_matrix > 20] *= 0.75
    modified_matrix[modified_matrix <= 20] *= 1.25
    modified_matrix = modified_matrix.round(1)
    return modified_matrix
    
    return matrix


def time_check(df)->pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here
     df['start_datetime'] = pd.to_datetime(df['startDay'] + ' ' + df['startTime'])
    df['end_datetime'] = pd.to_datetime(df['endDay'] + ' ' + df['endTime'])
      full_day_range = pd.date_range('00:00:00', '23:59:59', freq='1H').time
      full_day_df = pd.DataFrame({'time': full_day_range, 'dummy': 1})
      merged_df = pd.merge(df, full_day_df, how='cross')
     Svalid_timestamps = merged_df[(merged_df['time'] >= merged_df['start_datetime'].dt.time) &
                                 (merged_df['time'] <= merged_df['end_datetime'].dt.time)]
    result_series = valid_timestamps.groupby(['id', 'id_2']).size().eq(len(full_day_range) * 7)

    return result_series



    return pd.Series()
