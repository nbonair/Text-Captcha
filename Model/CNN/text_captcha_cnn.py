downsample_factor = 8 #pool size =2 with 4 pooling layers
def build_cnn_model():
    input_img = layers.Input(shape=(img_width, img_height, 1), name ="input_data", dtype = "float32")
    labels = layers.Input(name = "input_label", shape = (max_length,), dtype="float32")

    #Conv Layers
    conv_1 = layers.Conv2D(32, (3,3), 
                            activation= "relu", 
                            kernel_initializer="he_normal", 
                            padding = "same", 
                            name = "Conv1")(input_img)
    pool_1 = layers.MaxPooling2D((2,2), name = "pool1")(conv_1)

    conv_2 = layers.Conv2D(64, (3,3), activation= "relu", kernel_initializer="he_normal", padding = "same", name = "Conv2")(pool_1)
    pool_2 = layers.MaxPooling2D((2,2), name = "pool2")(conv_2)

    conv_3 = layers.Conv2D(120, (3,3), activation= "relu", kernel_initializer="he_normal", padding = "same", name = "Conv3")(pool_2)
    conv_3 = layers.Dropout(0.2)(conv_3) #drop connection with ratio 0.2 to avoid overfitting
    pool_3 = layers.MaxPooling2D((2,2), name = "pool3")(conv_3)

    # conv_4 = layers.Conv2D(256, (3,3), activation= "relu", kernel_initializer="he_normal", padding = "same", name = "Conv4")(pool_3)
    # batch_norm_4 = layers.BatchNormalization()(conv_4)
    # pool_4 = layers.MaxPooling2D((2,2), name = "pool4")(batch_norm_4)

    # Reshape layer for RNN input
    new_shape = ((img_width //downsample_factor),(img_height // downsample_factor)*120)
    reshape = layers.Reshape(target_shape=(max_length,new_shape[1]*new_shape[0]//max_length), name = "reshape")(pool_3)
    dense_1 = layers.Dense(256, activation= "relu", name = "dense_1") (reshape) #FC layer
    dense_1 = layers.Dropout(0.2)(dense_1)
    dense_2 = layers.Dense(128, activation= "relu", name = "dense_2") (dense_1) #FC layer

    # conv_encoder = layers.Dropout(0.2)(conv_encoder) #drop connection with ratio 0.2 to avoid overfitting

    #Single CNN model 
    output = layers.Dense(vocab_len, activation= "softmax", name ="CNN_output")(dense_2)
    cnn_model = keras.models.Model(inputs = input_img, outputs = output, name = "CNN_model")
    cnn_model.compile(optimizer = keras.optimizers.Adam(), loss="sparse_categorical_crossentropy", metrics = "accuracy")
    return cnn_model
cnn_model = build_cnn_model()
cnn_model.summary()

