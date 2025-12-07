# 04 - Demo Notebook

# This script demonstrates how to run inference using the Roboflow Hosted API.

from roboflow import Roboflow

# Replace YOUR_API_KEY with your actual key or leave as placeholder
rf = Roboflow(api_key="YOUR_API_KEY")
project = rf.workspace().project("elbowsdetection")
model = project.version(3).model

print("Running inference on sample image...")

# Example inference (sample.jpg must exist locally if executed)
# For the project submission, this is only illustrative.
# prediction = model.predict("sample.jpg", confidence=40, overlap=30).json()
# print(prediction)

print("Demo script placeholder. Inference example commented out for safety.")
