def images_process(images, labels,img_height, img_width):
    #input images path file and corresponding label
    #return matrix of grayscale img and encoded numerical labels


    def is_valid_captcha(captcha):
        for ch in captcha:
            if not ch in characters:
                return False
        return True
        
    #encode text label to list of number
    def encode_to_label(label):
        label = list(map(lambda x:char_to_num[x], label))
        return label

    def read_image(path, resize = True):

        img = cv2.imread(path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        if resize:
            img = cv2.resize(img, (img_width,img_height)) #standardize image

        img = (img/255).astype(np.float32) 
        img = img.T #transpose image, timestep will fit to the width of image
        return img
        
    def prep_data(images, labels):
        X = [read_image(img) for img in images] #pre-processing image
        y = [encode_to_label(label) for label in labels] #encode text label to numerical
        y = np.array(y)
        X = np.array(X)

        return X,y

    img, labels = prep_data(images,labels)
    return img, labels

