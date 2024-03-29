from read_data import read_data
from sklearn import preprocessing
from models import *

def main():


    df = read_data('Credit card transactions - India - Simple.csv')
    #X data
    X = pd.DataFrame(df, columns=['Date','City','ExpType','Amount','CardType'])

    #Transforming unique strings into numbers 0 -> n
    le = preprocessing.LabelEncoder()
    X_2 = X.apply(le.fit_transform)

    # Y data
    Y = pd.DataFrame(df, columns=['Gender'])

    feature_scores = find_best_features(X_2,Y)

    #Using best features for model
    X_3 = pd.DataFrame(X_2,columns=['City','Amount'])

    #Gender prediction based on city and amount
    GNB_model(X_3,Y)

    #Card prediction based on city and amounts
    Y = pd.DataFrame(df, columns=['CardType'])
    GNB_model(X_3,Y)

    #Expense prediction based on city and amounts
    Y = pd.DataFrame(df, columns=['ExpType'])
    GNB_model(X_3,Y)

main()