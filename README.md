# Warehouse Automation Pilot Project: Steel Component Detection and Sizing

Project Overview

This project implements a real-time object detection and classification system for steel components—specifically elbows and branches—within a warehouse environment. The goal is to support automated inventory management and quality control by identifying and measuring components directly from images or video.

Developed as the final assignment for the Computer Vision course, the system leverages the YOLOv8 architecture through Roboflow Train, enabling fast and accurate detection even with a limited dataset.

The system performs two key tasks:

1. Classification
Identifies essential attributes of each steel component:
- Brand  
- Description (Angle / Type)  
- Material Grade  

2. Sizing
Estimates the physical diameter (in millimeters) of each component using bounding box dimensions.

This two-stage approach allows the system to support both inventory categorization and dimensional verification.

Roboflow 

https://app.roboflow.com/warehouseautomationpilotproject

Project Video

https://drive.google.com/uc?id=1GVLm_pgGgVPMiiwoxpShMvyyAIpFk1Jq&export=download

Technologies Used

- Roboflow – Dataset creation, annotation, and training  
- YOLOv8 (Ultralytics) – Detection architecture used by Roboflow Train  
- Python + OpenCV – Local inference and testing  
- GitHub – Documentation and version control

Project Status
✔ Dataset completed ✔ Annotations finished ✔ Model trained (YOLOv8 via Roboflow Train) ✔ Inference tests completed ⬜ Final video pending
