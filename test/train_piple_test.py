import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.utlis.Top_feature_extract import Top_feature_extraction
from src.pipelines.train_pipeline import trainPipeline
from src.pipelines.test_pipeline import test_Csv_Data

if __name__ =='__main__':
    # trainPipeline().automate_pipline()
    # Top_feature_extraction().Top_feautre_extract()
    a=test_Csv_Data().test_Csv_data('../artifacts/application_train.csv')
    print(a)
    

    