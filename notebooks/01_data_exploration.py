# ----------------------------------------------------------------------
# 2. DOWNLOAD DATASET FROM ROBOFLOW - EMERGENCY PUBLIC DATASET
# ----------------------------------------------------------------------
# We use a public 'Real Package' dataset to bypass the photo upload block.

# IMPORTANT: No API Key needed for PUBLIC dataset.

!pip install roboflow
from roboflow import Roboflow

# Descargar el dataset público 'real-package-v1-14lml' (8409 imágenes)
rf = Roboflow(model_format="yolov8")
dataset = rf.dataset("real-package-v1-14lml")
dataset.download(model_format="yolov8") 
