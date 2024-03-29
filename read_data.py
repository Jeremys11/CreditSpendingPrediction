import pandas as pd

def read_data(csv_file, gender_to_numeric=True, date_to_month=True, city_only=True, amount_filter=True, card_type_only=True):
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)

    if gender_to_numeric:
        # Replace gender values with M=1 and F=0
        df['Gender'].replace(['M', 'F'], [1,0], inplace=True)

    if date_to_month:
        # Take only month of purchase
        df['Date'] = pd.to_datetime(df['Date']).dt.month

    if city_only:
        # Take only City name
        df['City'] = df['City'].apply(lambda x: x.split(',')[0])

    # Calculate the mean and standard deviation of the transaction amounts
    mean_amount = df['Amount'].mean()
    std_amount = df['Amount'].std()

    # Filter the DataFrame to only include rows where the transaction amount is within 2 standard deviations of the mean
    df_filtered = df[(df['Amount'] >= mean_amount - 2 * std_amount) & (df['Amount'] <= mean_amount + 2 * std_amount)]

    # Create a new DataFrame with the modified columns
    df_new = df_filtered[['id','Gender', 'Date', 'City', 'ExpType', 'Amount', 'CardType']]


    # Return the new DataFrame
    return df_new