import sys 
import logging
from datetime import datetime
import os 

Log_file= f'{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log'


Logs_path=os.path.join(os.getcwd() ,"logs", Log_file)
os.makedirs(Logs_path, exist_ok=True)

logs_file_path =os.path.join(Logs_path,Log_file)




logging.basicConfig(
    filename=logs_file_path,
    level=logging.INFO,
    format='%(asctime)s-%(levelname)s-%(message)s'
)

