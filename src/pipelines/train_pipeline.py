#  automating train pipeline 
import json
import os 
import sys 
from src.logger import logging
from dataclasses import dataclass
from src.componenets.model import Model
from src.componenets.Data_ingestion import DatInges
from src.componenets.Data_transform import DataTransform
@dataclass
class trainPipelineConfig:
    # store the model filepath , tranform data path
    artifacts='artifacts'
    test_data='transformed_test_data.npy' 
    train_data='transformed_train_data.npy'
    model_file='model.pkl'
    DataInges=DatInges()
    DataTransform=DataTransform()
    Modle=Model()



class trainPipeline:
    def __init__( self):
        self.config=trainPipelineConfig
    
    def automate_pipline(self):
        logging.info('data ingestion started ')
        self.config.DataInges.initiate_data_inges()
        logging.info('data inges comp now tranform started')
        X_train ,X_test ,y_train ,y_test=self.config.DataTransform.transformation()
        logging.info('transform done now model sleection  started')
        report=self.config.Modle.model_building(X_train,y_train,y_test,X_test)
        
        with open('../artifacts/report.json', 'w') as f:
          json.dump(report, f)
        best_model=self.config.Modle.tune_best_model(X_train ,X_test ,y_train ,y_test, report)
        logging.info('tuning of best model started ')
        self.config.Modle.save_model(best_model)
        logging.info('finally model training finished model is save din model.pkl file  ')

    
    
    
    
    
