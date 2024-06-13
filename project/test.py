import os
import subprocess
import time

def test_pipeline_execution():
    #run the pipeline script
    subprocess.run(['python', 'pipeline.py'], check=True)
    

    time.sleep(5)
    
    #check if the output file exists
    output_file_path = "./data/data.csv"
    assert os.path.isfile(output_file_path), "Output file does not exist"

if __name__ == "__main__":
    test_pipeline_execution()
    print("Test passed: Output file exists.")
