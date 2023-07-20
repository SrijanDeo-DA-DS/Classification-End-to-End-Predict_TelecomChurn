import os
path = 'C:/Users/srija/Documents/DS_Predict_TelecomChurn'

os.chdir(path)

import sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import chi2
from sklearn.impute import SimpleImputer
from src.exception import CustomException
from src.logger import logging
from sklearn.feature_selection import mutual_info_classif


def data_preprocessing(path):
    
    try:
        logging.info("Data pre-processing has started")
        df = pd.read_csv(path)
        df.columns = df.columns.str.replace(' ', '_')
        
        ## Dropping these columns for simplicty 
        df.drop(['Customer_ID','City','Zip_Code','Latitude','Longitude','Churn_Category','Churn_Reason'],axis=1,inplace=True)
        df['Customer_Status'] = df['Customer_Status'].apply(lambda i:1 if i =='Churned' else 0)
        
        ## train test split
        logging.info("Data train test has started")
        
        X = df.drop(['Customer_Status'],axis=1)
        y = df['Customer_Status']
        X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)
        
        col_with_NaN = [i for i in X_train.columns if (X_train[i].isnull().sum())>0]
        
        ## Simple Imputer for missing values
        logging.info("Imputing missing values has started")
        
        for i in col_with_NaN:
            if X_train[i].dtype=='object':
                si_mean = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
                X_train[i] = si_mean.fit_transform(X_train[i].values.reshape(-1,1))[:,0]
            else:
                si_mode = SimpleImputer(missing_values=np.nan, strategy='mean')
                X_train[i] = si_mode.fit_transform(X_train[i].values.reshape(-1,1))[:,0]
                
        col_with_int = [i for i in X_train.columns if X_train[i].dtype!='object']
        col_with_object = [i for i in X_train.columns if X_train[i].dtype=='object']
        
        ## Label Encoding categorical columns
        logging.info("Data label-encoding has started")
        
        le = LabelEncoder()
        X_train[col_with_object] = X_train[col_with_object].apply(le.fit_transform)
        
        ## Feature Selection categorical data
        logging.info("Feature Selection of categorical data has started")
        
        f_p_values=chi2(X_train[col_with_object],y_train)
        p_values=pd.Series(f_p_values[1])
        p_values.index=X_train[col_with_object].columns
        
        ## Feature Selection numerical columns
        logging.info("Feature Selection of numerical data has started")
        
        mutual_info = mutual_info_classif(X_train[col_with_int], y_train)
        mutual_info = pd.Series(mutual_info)
        mutual_info.index = X_train[col_with_int].columns
        mutual_info.sort_values(ascending=False)
        
        ## We wiil select the top 5 features from categorical and numerical features
        X_train = X_train[['Unlimited_Data','Streaming_TV','Streaming_Music','Streaming_Movies','Premium_Tech_Support',
                  'Number_of_Referrals','Tenure_in_Months','Total_Charges','Monthly_Charge','Total_Long_Distance_Charges']]
        
        df_training_data = pd.concat([X_train,y_train],axis=1)
        
        logging.info("Final dataset for model training")
        
        df_training_data.to_csv('C:/Users/srija/Documents/DS_Predict_TelecomChurn/data/training_data.csv',index=False)
        
        ## Test data Pipeline
        logging.info("Final test dataset for model training")
        
        ##Imputer
        for i in col_with_NaN:
            if X_test[i].dtype=='object':
                X_test[i] = si_mean.transform(X_test[i].values.reshape(-1,1))[:,0]
            else:
                X_test[i] = si_mode.transform(X_test[i].values.reshape(-1,1))[:,0]
                
        ##Label-Encoding
        col_with_int = [i for i in X_test.columns if X_test[i].dtype!='object']
        col_with_object = [i for i in X_test.columns if X_test[i].dtype=='object']
        
        X_test[col_with_object] = X_test[col_with_object].apply(le.transform)
        
        X_test = X_test[['Unlimited_Data','Streaming_TV','Streaming_Music','Streaming_Movies','Premium_Tech_Support',
                  'Number_of_Referrals','Tenure_in_Months','Total_Charges','Monthly_Charge','Total_Long_Distance_Charges']]
        
        df_test_data = pd.concat([X_test,y_test],axis=1)
        df_test_data.to_csv('C:/Users/srija/Documents/DS_Predict_TelecomChurn/data/test_data.csv',index=False)
        
        logging.info("Data-Preprocessing ended")
        
    except Exception as e:
        logging.info("Data pre_processing error")
        raise CustomException(e,sys)
    
data_preprocessing('C:/Users/srija/Documents/DS_Predict_TelecomChurn/data/train.csv')