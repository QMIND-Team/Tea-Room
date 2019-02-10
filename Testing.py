import pandas as pd

# Options to make pd easier to read from print
pd.options.display.max_columns = 999
pd.options.display.max_rows = 999
pd.options.display.width = 900


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


data = import_clean_data("Tea Room/2017-2018/item_sales.csv")
print(data.describe())
print(data.head(2000))
