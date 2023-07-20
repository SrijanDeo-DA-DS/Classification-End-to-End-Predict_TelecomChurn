import os
path = 'C:/Users/srija/Documents/DS_Predict_TelecomChurn'

os.chdir(path)

import sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
import keras 
from keras.layers import Dense
from keras.models import Sequential
from sklearn.metrics import classification_report,confusion_matrix
import pickle
from src.exception import CustomException
from src.logger import logging

def model_trainer(path):
    
    try:
        logging.info("Read training data has started")
        df_train = pd.read_csv('C:/Users/srija/Documents/DS_Predict_TelecomChurn/data/training_data.csv')
        X_train, X_test, y_train, y_test = train_test_split(df_train.drop(['Customer_Status'],axis=1), 
                                                    df_train['Customer_Status'], test_size=0.10, 
                                                    random_state=101)
        
        logging.info("Logistic regression has started")
        #Logistic Regression
        logmodel = LogisticRegression()
        logmodel.fit(X_train,y_train)
        predictions = logmodel.predict(X_test)
        print(confusion_matrix(y_test,predictions))
        print(classification_report(y_test,predictions))
        
        logging.info("Decision Tree classification has started")
        # Decision Tree
        dt_model=DecisionTreeClassifier()
        dt_model.fit(X_train,y_train)
        dt_pred = dt_model.predict(X_test)
        print(confusion_matrix(y_test,dt_pred))
        print(classification_report(y_test,predictions))
        
        logging.info("Random Forest classification has started")
        #Random Forest
        rf= RandomForestClassifier(n_estimators=500)
        rf.fit(X_train,y_train)
        rf_pre=rf.predict(X_test)
        print(confusion_matrix(y_test,rf_pre))
        print(classification_report(y_test,predictions))
        
        logging.info("XgBoost classification has started")
        #XgBoost
        xgboost = XGBClassifier(n_estimators=1000)
        xgboost.fit(X_train,y_train)
        xg_pred = xgboost.predict(X_test)
        print(confusion_matrix(y_test,xg_pred))
        print(classification_report(y_test,xg_pred))
        
        logging.info("Artificial Neural Network has started")
        #ANN
        ann  = Sequential()
        ann.add(Dense(units= 32, activation = 'relu', input_dim=10))
        ann.add(Dense(units= 32, activation = 'relu'))
        ann.add(Dense(units= 1, activation = 'sigmoid'))
        ann.compile(optimizer='adam',
              loss='mean_squared_error',
              metrics=['accuracy'])
        ann.fit(X_train,y_train, epochs=300,verbose= 0)
        ann_pred = ann.predict(X_test)
        ann_pred = [ 1 if y>=0.5 else 0 for y in ann_pred]
        
        print(confusion_matrix(y_test,ann_pred))
        print(classification_report(y_test,ann_pred))
        
        logging.info("Pickling the Random Forest Model")
        #Pickle the model
        file = open('C:/Users/srija/Documents/DS_Predict_TelecomChurn/data/random_forest_classification_model.pkl', 'wb')
        pickle.dump(rf, file)
        
    except Exception as e:
        raise CustomException(e,sys)
        
        
model_trainer('C:/Users/srija/Documents/DS_Predict_TelecomChurn/data/train.csv')