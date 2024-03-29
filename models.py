from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
import pandas as pd
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns


def find_best_features(X,Y):
    #Finding the best features
    #Higher score -- more related
    best_features= SelectKBest(score_func=chi2, k='all')
    fit= best_features.fit(X,Y.values.ravel())

    df_scores= pd.DataFrame(fit.scores_)
    df_columns= pd.DataFrame(X.columns)

    features_scores= pd.concat([df_columns, df_scores], axis=1)
    features_scores.columns= ['Features', 'Score']
    features_scores.sort_values(by = 'Score')

    #Amount + City hightest score
    #print(features_scores)
    return(features_scores)



def GNB_model(X,Y):
    #Splitting into training and test data
    X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.4,random_state=100)

    #Model using Gaussian Naive Bayes
    model = GaussianNB()

    #y_train.values.ravel() removes indices from dataframe reshaping it into 1D array
    model.fit(X_train,y_train.values.ravel())

    y_pred = model.predict(X_test)

    print('GNB CL Report: ',metrics.classification_report(y_test, y_pred, zero_division=1))

    # Compute confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    print('Confusion Matrix: \n', cm)

    # Define the labels
    labels = Y.iloc[:, 0].unique()

    # Create a heatmap
    sns.heatmap(cm, annot=True, fmt='d', xticklabels=labels, yticklabels=labels)
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.title('Confusion Matrix')
    plt.savefig('images/confusion_matrix/'+str(Y.head())+'.png')
    plt.close()