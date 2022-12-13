downsample_factor = 8 #pool size =2 with 3 pooling layers
def build_model():
    input_img = layers.Input(shape=(img_width,img_height, 1), name ="input_data", dtype = "float32")
    labels = layers.Input(name = "input_label", shape = max_length, dtype="float32")

    #Conv Layers
    conv_1 = layers.Conv2D(32, (3,3), 
                            activation= "relu", 
                            kernel_initializer="he_normal", 
                            padding = "same", 
                            name = "Conv1")(input_img)
    pool_1 = layers.MaxPooling2D((2,2), name = "pool1")(conv_1)

    conv_2 = layers.Conv2D(64, (3,3), activation= "relu", kernel_initializer="he_normal", padding = "same", name = "Conv2")(pool_1)
    pool_2 = layers.MaxPooling2D((2,2), name = "pool2")(conv_2)

    conv_3 = layers.Conv2D(128, (3,3), activation= "relu", kernel_initializer="he_normal", padding = "same", name = "Conv3")(pool_2)
    conv_3 = layers.Dropout(0.2)(conv_3) #drop connection with ratio 0.2 to avoid overfitting
    pool_3 = layers.MaxPooling2D((2,2), name = "pool3")(conv_3)

    # 3 maxpooling layers with stride = 2
    # Which leads to 8x smaller downsampled feature maps
    # Flatten the last conv_3 layer with 128 filters in to a feature vector and go through a Fully-Connected NN 
    # to summarize the learning features and being used as input for classification stage (RNN)
    new_shape = ((img_width //downsample_factor),(img_height // downsample_factor)*128)
    reshape = layers.Reshape(target_shape=new_shape, name = "reshape")(pool_3)
    #Fully-connected network
    dense_1 = layers.Dense(128, activation= "relu", name = "dense_1") (reshape) #FC layer
    dense_2 = layers.Dense(64, activation= "relu", name = "dense_2") (dense_1) #FC layer
    dense_2 = layers.Dropout(0.2)(dense_2)
    conv_encoder = layers.Dense(64, activation= "relu", name = "cnn_encoder") (dense_2) #FC layer
    conv_encoder = layers.Dropout(0.2)(conv_encoder) #drop connection with ratio 0.2 to avoid overfitting

    #RNNs
    lstm_1 = layers.Bidirectional(layers.LSTM(128, return_sequences=True, dropout=0.02))(conv_encoder)
    lstm_2 = layers.Bidirectional(layers.LSTM(64, return_sequences=True, dropout=0.2))(lstm_1)
    #transcipt layer
    prediction = layers.Dense(vocab_len + 1, activation="softmax", name = "pred")(lstm_2)
    # Add CTC layer for calculating CTC loss at each step
    output = CTCLayer(name="ctc_loss")(labels, prediction)

    # Define the model
    model = keras.models.Model(
        inputs=[input_img, labels], outputs=output, name="ocr_model_v1")
    # Optimizer
    opt = keras.optimizers.Adam()
    # Compile the model and return
    model.compile(optimizer=opt)
    return model

model = build_model()
print(model.input)
model.summary()
