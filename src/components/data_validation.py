import os
path = 'C:/Users/srija/Documents/DS_Predict_TelecomChurn'

os.chdir(path)

import sys
import pandas as pd
import shutil
from pathlib import Path
from src.exception import CustomException
from src.logger import logging


def Data_validation(path):
    '''
    This function will validate the raw data coming in on 3 basis:
    1. Is the directory empty ?
    2. If directory is not empty, then name of the file matches the expected value?
    3. If name of file is correct, are there exact number of columns as expected and no entire null columns in the data?
    '''
    
    os.chdir(path)
    
    logging.info("Data Validation started")
    try:
        if os.listdir():
            for i in os.listdir():
                if i.startswith('telecom') and i.endswith('.csv'):
                    df = pd.read_csv(i)
                    if len(df.columns)==38 and df.isnull().values.all(axis=0).sum()==0:
                        logging.info("Correct data")
                        shutil.copy(i,"C:/Users/srija/Documents/DS_Predict_TelecomChurn/data/good_data")
                    else:
                        logging.info("Incorrect data")
                        shutil.copy(i,"C:/Users/srija/Documents/DS_Predict_TelecomChurn/data/bad_data_archived")
                else:
                    logging.info("Incorrect filename")
                    shutil.copy(i,"C:/Users/srija/Documents/DS_Predict_TelecomChurn/data/bad_data_archived")
        else:
            logging.info("Folder is empty")
    except Exception as e:
        raise CustomException(e,sys)
        
Data_validation('C:/Users/srija/Documents/DS_Predict_TelecomChurn/data/raw_data')