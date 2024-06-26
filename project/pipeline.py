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
import pandas as pd
import requests


class Pipeline:
    def __init__(self, url1, url2):
        self.url1 = url1
        self.url2 = url2
        self.data1 = None
        self.data2 = None

    def get_data(self):
        downloaded1 = requests.get(self.url1)
        downloaded2= requests.get(self.url2)

        with open('file1.csv', 'wb') as file:
            file.write(downloaded1.content)
                
        self.data1 = pd.read_csv("file1.csv")

        with open('file2.csv', 'wb') as file:
            file.write(downloaded2.content)
                
        self.data2 = pd.read_csv("file2.csv")


    def transform(self):
        self.data1 = self.data1[self.data1["country"]=="World"]
        self.data1 = self.data1[["year", "co2", "co2_growth_prct"]]
        self.data2 = self.data2[["Year", "CSIRO Adjusted Sea Level"]]

        self.data = pd.merge(self.data1, self.data2, left_on="year", right_on="Year")
        self.data.drop(columns=["Year"], inplace=True)


    def save(self):
        # Ensure the data directory exists
        os.makedirs("./data", exist_ok=True)
        self.data.to_csv(".//data//data.csv", index=False)

    def run_pipeline(self):
        self.get_data()
        self.transform()
        self.save()



if __name__ == '_main_':
    pipe = Pipeline("https://github.com/owid/co2-data/raw/master/owid-co2-data.csv",
                    "https://github.com/datasets/sea-level-rise/raw/master/data/epa-sea-level.csv")
    pipe.run_pipeline()
