import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.componenets.model import Model
# from src.componenets.Data_ingestion import DatInges
# from src.logger import logging

# if __name__=='__main__':
#     data_ingestion=DatInges()
#     data_ingestion.initiate_data_inges()
#     logging.info("Data ingestion process finished")


# import numpy as np

# data = np.load('../artifacts/transformed_test_data.npy', allow_pickle=True).item()
# X_test = data["X"]
# y_test = data["Y"]

# print(X_test.shape, y_test.shape)

if __name__=='__main__':
    Model1=Model()
    X_train , y_train , X_test , y_test=Model1.data_extraction()
    report =Model1.model_building(X_train,y_train,y_test,X_test)
    Model1.tune_best_model(X_train, X_test , y_train  , y_test , report)
