# 2 pipelines one for form data another for csv 
from dataclasses import dataclass
from src.logger import logging
import os 
import sys 
import pandas as pd
import joblib
import numpy as np 
from sklearn.metrics import accuracy_score
# csv data 


class train_model_config:
    preprocessor='preprocessor.pkl'
    artifacts='artifacts'
    model='model.pkl'
    store_csv='test_data.csv'
    form_data_stored='new.pkl'
    


class test_Csv_Data :
    def __init__(self):
        self.config=train_model_config()
    
    def test_Csv_data(self , test_data):
        preprocess=joblib.load(os.path.join(self.config.artifacts, self.config.preprocessor))
        
        df=pd.read_csv(test_data)
        numeric_cols=df[preprocess['num_cols']]
        categorical_cols=df[preprocess['cat_cols']]

        numeric_transformed_cols= preprocess['num_pipe'].transform(numeric_cols)
        categorical_transformed_cols=preprocess['cat_pipe'].transform(categorical_cols)

        train_transformed_data =np.hstack([numeric_transformed_cols,categorical_transformed_cols])

        model=joblib.load(os.path.join(self.config.artifacts, self.config.model))
        y_pred=model.predict(train_transformed_data)

        df["Target_predicted"]=y_pred 

        df.to_csv(os.path.join(self.config.artifacts,self.config.store_csv))
        return df
    

class test_form_Data:
    # from  train model selcting import features 
    def __init__(self):
        self.config =train_model_config()
    
    def  predict_form_Data(self , data):
        Data=[data]
        new_Data =pd.DataFrame(data)
        new_Data.to_csv('new.csv')
        df=test_Csv_Data.test_Csv_data(self.config.form_data_stored)
        return df['Target']
        



    
        
