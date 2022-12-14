# Non-segmentation model for breaking Text CAPTCHA
---
I have implement 2 non-segmentation models to break the text captcha: CNN and CRNN  
Figures below show the accuracy of each model, with similar training and testing dataset  
## 1. CNN
![image](https://user-images.githubusercontent.com/86250240/207528159-e5f46589-d38a-493d-be38-3cd5cda8fde4.png)

## 2. CRNN
![image](https://user-images.githubusercontent.com/86250240/207529574-5133c0a7-5481-4c75-b7b8-8198a10105f9.png)

- The accuracy for CNN model could be improved by extra steps in image processing stage, to reduce noises feature in the image. With a simple image crop, the accuracy for testing dataset could reach ~80%.   
- CRNN model with the original dataset could predict the text in all captcha with nearly absolute accuracy. More complicated dataset could be implement, for further evaluate this techniques
- Details related to model configuration, architecture explaination will be shown in each corresponding file
