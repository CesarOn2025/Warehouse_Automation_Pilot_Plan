02_training.ipynb

----------------------------------------------------------------------
 1. SETUP: INSTALL & IMPORT LIBRARIES
 ----------------------------------------------------------------------
 Install necessary libraries (assuming requirements.txt is ready)
!pip install -r ../requirements.txt 
 If running in Colab without requirements.txt, use:
 !pip install ultralytics roboflow

from ultralytics import YOLO
import os
import torch

print(f"CUDA Available: {torch.cuda.is_available()}")
print("Setup complete. Libraries imported.")

 ----------------------------------------------------------------------
 2. DOWNLOAD DATASET FROM ROBOFLOW (Must be completed in 01_data_exploration)
 ----------------------------------------------------------------------
 IMPORTANT: You must run the download script from your 01_data_exploration.ipynb 
 or ensure the dataset is in a known location before this step.

 Replace with the folder name created by your Roboflow download script 
 (e.g., 'Warehouse-Elbow-Detection-v1-yolov8')
ROBOFLOW_DATA_FOLDER = '
