from pathlib import Path
import string
import os
#This function used for extract data and labels from dataset, using dataset's dir as input
def raw_data_process(path):
    ##  Parameter
    # Input: Path to your dataset
    # Output: 
    #   images: list of dir to captcha images
    #   labels: list of corresponding labels
    #   characters: list of possible characters in labels (here we includes all characters in alphabet and numbers)
    #   max_length: maximum length of a label
    path = Path(path)
    images = sorted(list(map(str, list(path.glob("*.png")))))
    #split labels
    labels = [img.split(os.path.sep)[-1].split(".png")[0] for img in images]

    #Get dataset information
    char_list = string.ascii_letters+string.digits

    characters = set(char for char in char_list)
    characters = sorted(list(characters))
    max_length = max([len(label) for label in labels])
    for i, label in enumerate(labels):
        if len(label) > 5:
            print(f"{i} {label}")
            print(images[i])

    print("Number of images found: ", len(images))
    print("Number of labels found: ", len(labels))
    print("Number of unique characters: ", len(characters))
    print("Characters present: ", characters)
    print("Maximum label length: ",max_length)
    return images, labels, characters, max_length

