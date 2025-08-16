from src.logger import logging
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.componenets.model import Model
if __name__=='__main__':
    Model1=Model()
    X_train , y_train , X_test , y_test=Model1.data_extraction()
    report =Model1.model_building(X_train,y_train,y_test,X_test)
    Model1.tune_best_model(X_train, X_test , y_train  , y_test , report)
