import os
import subprocess
import time

def test_pipeline_execution():
    # Run the pipeline script
    subprocess.run(['python3', 'pipeline.py'], check=True)
    
    # Allow some time for the pipeline to finish execution
    time.sleep(5)
    
    # Check if the output file exists
    output_file_path = "./data/data.csv"
    assert os.path.isfile(output_file_path), "Output file does not exist"

if __name__ == "__main__":
    test_pipeline_execution()
    print("Test passed: Output file exists.")
