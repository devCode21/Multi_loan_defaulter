# since if we have form data as input we can ask theem put the features which are more important
from dataclasses import dataclass
import os
import joblib
from src.logger import logging
@dataclass
class Config:
    preprocesser:str='preprocessor.pkl'
    Save_Top_features:str='Top_features.pkl'
    model:str='model.pkl'
    artifacts='artifacts'


class Top_feature_extraction:
    def __init__(self):
        self.config=Config()
    
    def Top_feautre_extract(self):
      preprocess_data=joblib.load(os.path.join("..",self.config.artifacts,self.config.preprocesser))
      features_names=preprocess_data["feature_name"]
      best_model=joblib.load(os.path.join("..",self.config.artifacts, self.config.model))
      a=best_model.feature_importances_
      feature_values={}

      for i in range(0,len(a)):
          feature_values[features_names[i]]=a[i]
      
      top_feature=sorted_by_values = sorted(feature_values.items(), key=lambda x: x[1], reverse=True)

    
      k=top_feature[:10]
      logging.info(k)


    



    
