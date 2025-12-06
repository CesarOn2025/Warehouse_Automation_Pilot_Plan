 01_data_exploration.ipynb

 ----------------------------------------------------------------------
 1. SETUP: INSTALL & IMPORT LIBRARIES
 ----------------------------------------------------------------------
 Installation of necessary libraries
!pip install -r ../requirements.txt 
 If running in Colab without the requirements.txt, use:
 !pip install ultralytics roboflow

from ultralytics import YOLO
import matplotlib.pyplot as plt
import os
import shutil
from roboflow import Roboflow

print("Setup complete. Libraries imported.")

 ----------------------------------------------------------------------
 2. DOWNLOAD DATASET FROM ROBOFLOW
 ----------------------------------------------------------------------
 NOTE: Replace with YOUR OWN Roboflow API key and project link.
 Get this code after exporting your dataset in YOLOv8 format on Roboflow.
 This code will download your labeled dataset directly to Colab.

 rf = Roboflow(api_key="YOUR_ROBOFLOW_API_KEY")
 project = rf.workspace("YOUR_WORKSPACE").project("YOUR_PROJECT_NAME")
 dataset = project.version(1).download("yolov8")

print("Dataset download section prepared. You will insert the real code here.")

 ----------------------------------------------------------------------
 3. DATASET PATHS AND CONFIGURATION
 ----------------------------------------------------------------------

 Define the root path of the dataset. 
DATA_DIR = '../data' 
DATA_YAML_PATH = os.path.join(DATA_DIR, 'data.yaml')

 ----------------------------------------------------------------------
 4. EXPLORATION: VISUALIZE SAMPLE IMAGES WITH LABELS
 ----------------------------------------------------------------------

 Load a pre-trained YOLOv8 model for prediction/visualization
model = YOLO('yolov8n.pt') 

 Define the path to a sample image from your 'test' or 'valid' set for visualization
 IMPORTANT: You must replace 'YOUR_ROBOFLOW_DOWNLOAD_FOLDER' and 'sample_image.jpg'
SAMPLE_IMAGE_PATH = os.path.join('
