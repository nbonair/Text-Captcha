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
    #   max_length: maximum length of a label
    path = Path(path)
    images = sorted(list(map(str, list(path.glob("*.png")))))
    #split labels
    labels = [img.split(os.path.sep)[-1].split(".png")[0] for img in images]
    max_length = max([len(label) for label in labels])
    for i, label in enumerate(labels):
        if len(label) > 5:
            print(f"{i} {label}")
            print(images[i])

    print("Number of images found: ", len(images))
    print("Number of labels found: ", len(labels))

    print("Maximum label length: ",max_length)
    return images, labels, max_length

