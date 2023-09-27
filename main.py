import psycopg2
from sklearn import preprocessing
from models import *


def main():
    #Connecting to SQL database
    conn = psycopg2.connect(database="jeremysingh",
                            host="localhost",
                            user="jeremysingh",
                            password="",
                            port="5432")

    #Getting data from SQL database
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM spending")
    sql_query = cursor.fetchall()

    #Dataframe containing SQL Query
    df = pd.DataFrame(sql_query, columns = ['id','date','city','cardtype','exptype','gender','amount'])

    #Modifying data to make it easier to model to parse
    df['gender'].replace(['M', 'F'], [1,0], inplace=True)
    df['date'] = df['date'].apply(lambda x: x.month) #Taking only month of purchase
    df['city'] = df['city'].apply(lambda x: x.split(',')[0]) #Taking only City name

    #X data
    X = pd.DataFrame(df, columns=['date','city','exptype','amount','cardtype'])

    #Transforming unique strings into numbers 0 -> n
    le = preprocessing.LabelEncoder()
    X_2 = X.apply(le.fit_transform)

    # Y data
    Y = pd.DataFrame(df, columns=['gender'])

    feature_scores = find_best_features(X_2,Y)

    #Using best features for model
    X_3 = pd.DataFrame(X_2,columns=['city','amount'])

    GNB_model(X_3,Y)

main()