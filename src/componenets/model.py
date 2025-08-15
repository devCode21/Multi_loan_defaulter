# training the model => accessing the  x train , y train ,x_test ,y_test data and conversion 
#param gridss 
#models used 
import os 
import numpy as np
from dataclasses import dataclass
from sklearn.ensemble import GradientBoostingClassifier , RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from src.constants.constant import artifcraft
from src.logger import logging
import joblib

param_grids={
    'Grad_bossting':{ 'n_estimators': [100, 200, 500],
    'learning_rate': [0.01, 0.05, 0.1, 0.2],
    'max_depth': [3, 5, 7],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'subsample': [0.6, 0.8, 1.0],
    'max_features': ['auto', 'sqrt', 'log2']
    
},
    'Xg_boost':{
    'n_estimators': [100, 200, 500],
    'learning_rate': [0.01, 0.05, 0.1, 0.2],
    'max_depth': [3, 5, 7, 10],
    'subsample': [0.6, 0.8, 1.0],
    'colsample_bytree': [0.6, 0.8, 1.0],
    'gamma': [0, 0.1, 0.2, 0.4],
    'reg_alpha': [0, 0.01, 0.1, 1],  # L1 regularization
    'reg_lambda': [1, 1.5, 2, 3]     # L2 regularization

},
    'Random_forest':{'n_estimators': [100, 200, 500],
    'max_depth': [None, 5, 10, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': ['auto', 'sqrt', 'log2'],
    'bootstrap': [True, False]}
}


model={
       'Random_forest':RandomForestClassifier(class_weight='balanced',n_jobs=-1),
       'Xg_boost':XGBClassifier(n_jobs=-1),
       'Grad_bossting':GradientBoostingClassifier()

}


@dataclass
class Modelconfig :
     Train_data :str = "transformed_train_data.npy"
     Test_data:str= "transformed_test_data.npy"
     Artifacts:str="artifacts"
     Model:str="Model.pkl"
     models=model
     params=param_grids

# to  accesss the tranformed data the n loactation of to store model.pkl acees of preopces tp get fetaure name out 
# to build a 3-4 models so to get best model a criteria or an report then choosing betsv model the hyperpareamnter tuning 

class Model :
    def __init__(self):
         self.config= Modelconfig
    
    def data_extraction(self):
         logging.info('data extraction staeted')
         data=np.load(os.path.join(artifcraft,self.config.Train_data),allow_pickle=True).item()
         X_train =data['X']
         y_train=data['Y']

         data2=np.load(os.path.join(artifcraft,self.config.Test_data), allow_pickle=True).item()
         X_test =data2['X']
         y_test=data2['Y']
         logging.info('data extracted succesfully')
         return X_train , y_train , X_test , y_test
    
    def model_building (self ,X_train , y_train ,y_test, X_test ):
         logging.info('model_build_started')
         report={}
         for model_name , model in  self.config.models.items():
              model.fit(X_train, y_train)
              y_pred= model.predict(X_test)
              report[model_name]=accuracy_score(y_pred , y_test)
          
         return report 
        
    
    def  tune_best_model (self ,X_train , X_test , y_train , y_test , report ):
         

         best_model_name = max(report, key=report.get)
         param_grids=self.config.params[best_model_name]
         best_model=GridSearchCV(estimator=self.config.models[best_model_name] ,param_grid=param_grids , verbose=1)
         best_model.fit(X_train[:100] ,y_train[:100])
         best_model1=best_model.best_estimator_
         
         y_pred=best_model1.predict(X_test)
         logging.info(f'{accuracy_score(y_pred,y_test)}')
         return best_model1
    
    def save_model(self,best_model):
         joblib.dump(best_model , os.path.join(artifcraft,'model.pkl'))
         
         
         

         


         



         
         
         

