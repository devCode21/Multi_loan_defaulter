import os 
import sys 
from dataclasses import dataclass
from src.constants.constant import APP_TEST ,APP_TRAIN ,artifcraft
import pandas as pd 
import numpy as np
from sklearn.pipeline import Pipeline 
from sklearn.metrics import accuracy_score 
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler 
from sklearn.compose import ColumnTransformer
import joblib
from src.logger import logging


@dataclass

class DataTransformconfig:
    transformed_train_data:str='transformed_train_data'
    transformed_test_data:str='transformed_test_data'
    artifacts:str=artifcraft
    preprocessor='preprocessor.pkl'
    

class DataTransform:
     def __init__(self):
          self.config=DataTransformconfig
    
     def transformation(self):
          data =pd.read_csv(APP_TRAIN)
          Y=data['TARGET']
          X=data.drop("TARGET", axis=1)
          X=X.drop("SK_ID_CURR" , axis=1)
          logging.info("tranformation started ")

          #sepearte categorical columns and numerical columns 

          cat_columns= [col for col in X.columns if X[col].dtypes=='O']
          num_columns=[col for col in X.columns if X[col].dtypes!='O']
          
          # oultlier treatment 
          logging.info("Outlier treatment started ")
          


          X_train ,X_test ,y_train , y_test =train_test_split(X, Y, test_size=0.3 ,random_state=42) 
          from sklearn.preprocessing import OneHotEncoder

          logging.info("Outlier treatment done ")
          logging.info(" Pipeline work  started ")
          numeric_pipleine =Pipeline([
                ('Simple_Imputer', SimpleImputer(strategy='mean')),
                ('scaler', StandardScaler())
          ])
            
          categorical_pipeline=Pipeline([
               ('Simple_Imputer', SimpleImputer(strategy='most_frequent')),
               ('onehotEncoder', OneHotEncoder(sparse_output=False))                 

          ])
          
          X_train_tranformed_numeric_col=numeric_pipleine.fit_transform(X_train[num_columns])
          X_test_tranformed_numeric_col=numeric_pipleine.transform(X_test[num_columns])

       
          
          X_train_tranformed_cat_col=categorical_pipeline.fit_transform(X_train[cat_columns])
          X_test_tranformed_cat_col=categorical_pipeline.transform(X_test[cat_columns])
         
          X_train_tranfromed=np.hstack([X_train_tranformed_numeric_col,X_train_tranformed_cat_col])
          X_test_tranfromed=np.hstack([X_test_tranformed_numeric_col,X_test_tranformed_cat_col])
          cat_feature_names = categorical_pipeline.named_steps['onehotEncoder'].get_feature_names_out(cat_columns)
          feature_names=list(num_columns)+list(cat_feature_names)
          preprocess={
               "feature_name":feature_names,
               "num_cols":num_columns,
               "cat_cols":cat_columns,
               "num_pipe":numeric_pipleine,
               "cat_pipe":categorical_pipeline,
               
          }

          joblib.dump(preprocess, os.path.join(self.config.artifacts, self.config.preprocessor))

          
          
          np.save(os.path.join(self.config.artifacts,self.config.transformed_train_data),{"X":X_train_tranfromed,"Y":y_train.values})
          np.save(os.path.join(self.config.artifacts,self.config.transformed_test_data),{"X":X_test_tranfromed,"Y":y_test.values})
          logging.info("DATA TRANFORMED SUCCESSFULLY ")

          return X_train_tranfromed ,X_test_tranfromed ,y_train ,y_test
     
          

    #  data> collection , missing value ,ouliers , train test split , target seperate 

