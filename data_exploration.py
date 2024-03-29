import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from read_data import read_data
import plotly.express as px
import time

def data_exploration():
    data = read_data('Credit card transactions - India - Simple.csv',gender_to_numeric=False)
    return data

def average_spending():
    data = data_exploration()

    # Assuming your data is in a DataFrame named df
    data['Amount'] = data['Amount'].astype(float)  # Ensure 'Amount' is a float
    average_city = data.groupby(['City'])['Amount'].mean().reset_index()
    average_card = data.groupby(['CardType'])['Amount'].mean().reset_index()
    average_gender = data.groupby(['Gender'])['Amount'].mean().reset_index()
    average_exptype = data.groupby(['ExpType'])['Amount'].mean().reset_index()

    #Just get top 12 cities
    average_city = average_city.sort_values(by='Amount', ascending=False).head(12)

    averages = [average_city, average_card, average_gender, average_exptype]

    for item in averages:
        fig = px.pie(item, names=item.columns[0], values=item.columns[1])
        fig.update_layout(title='Average Spending by ' + item.columns[0])
        fig.show()
        time.sleep(5)
        fig.write_html('images/'+str(item.columns[0])+'.html')

def data_viz():

    data = data_exploration()

    plt.figure(figsize=(10,6))
    sns.boxplot(x='Gender', y='Amount', data=data)
    plt.title('Transaction Amounts by Gender')
    plt.show()

    plt.figure(figsize=(10,6))
    data.groupby('CardType')['Amount'].sum().plot(kind='pie', autopct='%1.1f%%')
    plt.title('Transaction Amounts by Card Type')
    plt.show()

    plt.figure(figsize=(10,6))
    data.groupby('ExpType')['Amount'].sum().plot(kind='pie', autopct='%1.1f%%')
    plt.title('Transaction Amounts by Expense Type')
    plt.show()

    plt.figure(figsize=(10,6))
    data.groupby('Date')['Amount'].sum().plot(kind='pie', autopct='%1.1f%%')
    plt.title('Transaction Amounts by Month')
    plt.show()

data_viz()
average_spending()