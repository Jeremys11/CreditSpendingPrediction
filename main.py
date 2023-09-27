import psycopg2
import pandas as pd
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn import metrics

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

#Finding the best features
#Higher score -- more related
best_features= SelectKBest(score_func=chi2, k='all')
fit= best_features.fit(X_2,Y.values.ravel())

df_scores= pd.DataFrame(fit.scores_)
df_columns= pd.DataFrame(X_2.columns)

features_scores= pd.concat([df_columns, df_scores], axis=1)
features_scores.columns= ['Features', 'Score']
features_scores.sort_values(by = 'Score')

#Amount + City hightest score
#print(features_scores)

#Using best features for model
X_3 = pd.DataFrame(X_2,columns=['city','amount'])

#Splitting into training and test data
X_train,X_test,y_train,y_test=train_test_split(X_3,Y,test_size=0.4,random_state=100)

#Model using Gaussian Naive Bayes
model = GaussianNB()

#y_train.values.ravel() removes indices from dataframe reshaping it into 1D array
model.fit(X_train,y_train.values.ravel())

y_pred = model.predict(X_test)

print('CL Report: ',metrics.classification_report(y_test, y_pred, zero_division=1))