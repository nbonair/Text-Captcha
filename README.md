# Text-Captcha
## Executive Summary
---
This text stream is aiming to develop a fully functional program for breaking text CAPTCHAs. The program is based on Artificial Intelligence technologies to automatically extract the text from the captcha image with high noise level and complicated background.   
Our current CRNN approach is evaluated by a grayscale CAPTCHA dataset, which provides promising result with high accuracy rate. Future development will focus on expanding training dataset for current model and developing a program to breaking input CAPTCHA from users.

## Project Progress
---
This project is still under early R&D phases. Currently, we have created a simple image-processing module for raw data and a CRNN model to extract the captchas into text format. The whole program could be accessed from [Text_captcha.ipynb](https://github.com/nbonair/Text-Captcha/blob/main/Text_captcha_CNN.ipynb)   
To facilitate the future development, we breakdown the notebook into different module. The details guidance is included in each module folder:
1. Image Preprocessing: Processing raw image data into model-compatible input and labels
2. Model: Include our current models' architectures (using CNN and CRNN techniques). Model summary included in each model's file
3. Pretrained Model: Trained model extracted in .tf file. Using ``tf.keras.models.load_model('dir_to_model')``` to load the model for further training or development
4. Dataset: Current dataset resources 

## Future Plan
---
### Application Development
- Develop program using current model to break user's input CAPTCHA
- Improve image processing module
- Integrate to company pipeline
### R&D
- Expand training dataset with more complicated CAPTCHA
- Complete training and evaluating phase to release final model for our application
- Further research and development for new features in OCR
## Research Resources
---
## Model Overview
### 1. CNN
![image](https://user-images.githubusercontent.com/86250240/207933521-28f9877a-4567-4ebf-ae4f-f615e5baed4f.png)

### 2. CRNN
![image](https://user-images.githubusercontent.com/86250240/207933555-e473cde8-6048-4dff-8736-159d8b4c39ee.png)

