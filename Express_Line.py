# Returns the average number of orders per minute on a given day of the week
def orders_per_minute(df):

    # Group All of the rows by weekday, hour, and minute, returns a groupBy object which is a collection of data frames
    # weekday: 0 = monday, 1 = tuesday, ... 6 = sunday
    grouped = df.groupby([df["Date_Time"].dt.weekday.rename('Day_of_Week'), df["Date_Time"].dt.hour.rename('Hour'),
                          df["Date_Time"].dt.minute.rename('Minute')])

    # Get the number of days in the data frame
    num_days = len(df["Date_Time"].dt.normalize().unique())

    # Get how many orders are placed on that day of the week, at that time, at that minute
    num_occurrences = grouped.size().to_frame('Number of Orders').reset_index()
    # Get Average Number of orders on that day and time
    num_occurrences['Average Number of Orders'] = num_occurrences['Number of Orders'].apply(lambda x: x / num_days)

    return num_occurrences


# Returns the times at which the orders per minute are above a threshold
def overwhelmed(max_orders_per_minute, df):
    df = orders_per_minute(df)

    # Find times where average number of orders is greater than what we can handle
    busy_times = df['Average Number of Orders'] > max_orders_per_minute

    return df[busy_times]
