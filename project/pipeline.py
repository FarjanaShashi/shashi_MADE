# Follow your project plan to build an automated data pipeline for your project
#     Write a script (for example in Python or Jayvee) that pulls the data sets you chose from the internet, transforms it and fixes errors, and finally stores your data in the /data directory
#         Place the script in the /project directory (any file name is fine)
#         Add a /project/pipeline.sh that starts your pipeline as you would do from the command line as entry point:
#             E.g. if you run your script on your command line using `python3 /project/pipeline.py`, create a /project/pipeline.sh with the content: 
#                     #!/bin/bash
#                     python3 /project/pipeline.py
#     The output of the script should be: datasets in your /data directory (e.g., as SQLite databases) 
#         Do NOT check in your data sets, just your script
#         You can use .gitignore to avoid checking in files on git
#         This data set will be the base for your data report in future project work
# Update the issues and project plan if necessary



import os
from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd
import numpy as np
from sqlalchemy import create_engine


class ExtractData:
    #Kaggle API initialization
    def __init__(self):
        self.kaggle_api = KaggleApi()
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.data_dir = os.path.join(self.script_dir,'..','data')
        self.download_dir = os.path.abspath(self.data_dir)
        os.environ['KAGGLE_CONFIG_DIR'] = os.path.join(self.script_dir,".kaggle")
        
    # This will call kaggle api, perform authentication and download data in Data directory
    def download_dataset(self,dataset_name):
        self.kaggle_api.authenticate()
        self.kaggle_api.dataset_download_files(dataset_name, path=self.download_dir, unzip=True)
        
     
    
    def load_and_clean_data(self,dataset_name):
        print("Data Transformation")
        dataset = pd.read_csv(os.path.join(self.download_dir,dataset_name))
        numeric_mean = dataset.select_dtypes(include=[np.number]).mean()
        df_numeric_imputed =dataset.select_dtypes(include=[np.number]).fillna(numeric_mean)
        dataset_imputed = pd.concat([dataset.select_dtypes(exclude=[np.number]),df_numeric_imputed],axis=1)
        return dataset_imputed
    
    def save_data(self,database_name,dataset):
        print("Load into Sqlite\n")
        engine = create_engine(r'sqlite:///'+str(self.download_dir) + '\\' + database_name + r'.sqlite')
        dataset.to_sql(database_name,con=engine,schema=None,if_exists='replace',index=False)
    
    def remove_unnecessary_files(self):
        print("Removing Unnecessary Files")
        for filename in os.listdir(self.download_dir):
            if not filename.endswith(".sqlite"):
              file_path = os.path.join(self.download_dir, filename)
              
              if os.path.isfile(file_path):
                  os.remove(file_path)
                  print(f"file removed: {filename}")
        
        
#pipeline
if __name__ == '__main__':    
    extract = ExtractData()
    extract.download_dataset('thedevastator/the-relationship-between-crop-production-and-cli')        
    dataset = extract.load_and_clean_data('Crop_Production_and_Climate_Change.csv')   
    extract.save_data('relationship', dataset)   

    print("Loading new data\n")             
    extract.download_dataset("crawford/agricultural-survey-of-african-farm-households")
    dataset = extract.load_and_clean_data("African_Farm_Households.csv")
    extract.save_data('survey', dataset)  
    extract.remove_unnecessary_files()  