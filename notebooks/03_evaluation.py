
 03_evaluation.ipynb

 ----------------------------------------------------------------------
 1. SETUP: IMPORT LIBRARIES
 ----------------------------------------------------------------------
from ultralytics import YOLO
import os
import pandas as pd

print("Setup complete. Libraries imported.")

 ----------------------------------------------------------------------
 2. DEFINE PATHS
 ----------------------------------------------------------------------
 Define the path to the best trained model weights
MODEL_WEIGHTS_PATH = '../models/best_elbow_detection_model.pt' 

 Define the path to the data configuration file (from Roboflow download)
 Replace with the actual Roboflow folder name created in Colab
ROBOFLOW_DATA_FOLDER = 'YOUR_ROBOFLOW_DOWNLOAD_FOLDER' 
DATA_YAML_PATH = os.path.join(ROBOFLOW_DATA_FOLDER, 'data.yaml')

 Output path for saving the metrics CSV
RESULTS_OUTPUT_PATH = '../results/evaluation_metrics.csv'

if not os.path.exists(MODEL_WEIGHTS_PATH):
    print(f"FATAL ERROR: Model weights not found at {MODEL_WEIGHTS_PATH}. Did you run 02_training.ipynb and copy the 'best.pt' file?")

if not os.path.exists(DATA_YAML_PATH):
    print("FATAL ERROR: data.yaml not found. Please ensure the dataset is downloaded or placed correctly.")
    
 ----------------------------------------------------------------------
 3. LOAD THE TRAINED MODEL
 ----------------------------------------------------------------------
model = YOLO(MODEL_WEIGHTS_PATH)
print(f"T
