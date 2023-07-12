import os
path = 'C:/Users/srija/Documents/DS_Predict_TelecomChurn'

os.chdir(path)

import sys
import pandas as pd
import shutil
from pathlib import Path
from src.exception import CustomException
from src.logger import logging
from sklearn.model_selection import train_test_split

def train_test_splitting(path):
    os.chdir(path)
    
    
    try:
        logging.info("Train Test Split Started")
        for i in os.listdir():
            
            df = pd.read_csv(i)
            df_train, df_test = train_test_split(df,test_size=0.2)
            df_train.to_csv('C:/Users/srija/Documents/DS_Predict_TelecomChurn/data/train.csv',index=False)
            df_test.to_csv('C:/Users/srija/Documents/DS_Predict_TelecomChurn/data/test.csv',index=False)

    except Exception as e:
        logging.info("Train Test Split has an error")
        raise CustomException(e,sys)
        
train_test_splitting('C:/Users/srija/Documents/DS_Predict_TelecomChurn/data/good_data')