import pandas as pd


# Clean data by removing unnecessary items and removing null values
def import_clean_data(file_path):
    # Combine the date and time columns to one
    df = pd.read_csv(file_path, parse_dates=[["Date", "Time"]])
    # Remove Columns that are not useful to us
    df.drop(["Time Zone", "Transaction ID", "Payment ID", "Device Name", "Details", "Location", "Dining Option",
             "Customer ID", "Customer Name", "Customer Reference ID"], axis=1, inplace=True)
    # Remove the Refunds
    df = df[df.Category != "None"]
    # Convert columns to appropriate types
    # Dollar columns to floats using regex to remove dollar sign
    dollar_column = df[df.columns[7:11]].replace('[$]', '', regex=True)
    # Update df with proper dollar columns
    df.update(dollar_column)
    # Change the dollar columns to float type
    df[["Gross Sales", "Discounts", "Net Sales", "Tax"]] = df[["Gross Sales", "Discounts", "Net Sales", "Tax"]]\
        .apply(pd.to_numeric)

    return df


# Returns only the specified items (list of strings or string)
def get_specific_items(item_name, df):
    # Check to see if item_name is not a list
    if not isinstance(item_name, list):
        # make item_name a list in order to work with isin
        item_name = [item_name]
    items = df.loc[df["Item"].isin(item_name)]

    return items
