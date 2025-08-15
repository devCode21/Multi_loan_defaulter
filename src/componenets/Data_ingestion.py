import os 
import pandas as pd
import numpy as np
import sys
from src.constants.constant import APP_TRAIN , APP_TEST, artifcraft
from dataclasses import dataclass
from src.logger import logging
from src.exception import CustomException

@dataclass  #just replce of init 


class DataIngestion:
    artifcraft_folder:str=artifcraft
    train_file_name:str='application_train.csv'
    test_file_name:str='application_test.csv'



class DatInges:
    def __init__(self):
       self.config=DataIngestion
    
    def initiate_data_inges(self):
        logging.info('data ingestion started ')
        try:
            df=pd.read_csv(APP_TRAIN)
            df2=pd.read_csv(APP_TEST)
            logging.info('copying data ')
            logging.info('copying data 2')
            df.to_csv(os.path.join(self.config.artifcraft_folder,self.config.train_file_name), index=False)
            df2.to_csv(os.path.join(self.config.artifcraft_folder,self.config.test_file_name),index=False )
            logging.info('succesfully copied data ')
        except Exception as e:
           raise  CustomException(e,sys)



print(APP_TRAIN)