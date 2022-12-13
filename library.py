import os,cv2
import numpy as np
import matplotlib.pyplot as plt
import string

from pathlib import Path
from collections import Counter

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from keras.utils import pad_sequences
from keras.utils.np_utils import to_categorical
from keras.models import load_model

import sklearn
from sklearn.model_selection import train_test_split
import numpy as np