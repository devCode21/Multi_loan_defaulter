import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.componenets.Data_transform import DataTransform
from src.logger import logging

if __name__=='__main__':
    Data_Tranformed=DataTransform()
    X_train ,y_train ,x_test ,y_test =Data_Tranformed.transformation()
    logging.info("Data ingestion process finished")