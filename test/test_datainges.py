import sys
import os


from src.componenets.model import Model
from src.componenets.Data_ingestion import DatInges
from src.logger import logging

if __name__=='__main__':
    data_ingestion=DatInges()
    data_ingestion.initiate_data_inges()
    logging.info("Data ingestion process finished")


