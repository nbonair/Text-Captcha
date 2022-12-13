# Image processing functions
## This folder include functions used to process raw input dataset
### 1. parameter_initialization.py  
Initialize images size, list of possible characters and dictionary for text - numerical labels
### 2. raw_data_process.py  
Use dataset path as input. Split data into 2 lists: images dir and corresponding label   
### 3. image_processing.py  
Input: images path and labels  
Output: Images in normalized vector and numerical labels. Dataset now is ready to be used by any neuron network
### 4. main.py
Get processed data and split into train-test dataset
### 5. data_visualization.py
Visualize data for testing purpose
