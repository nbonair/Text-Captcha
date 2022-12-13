
data_dir = "samples" #replace by path to dataset
images, labels, max_length = raw_data_process(data_dir)

X, y = images_process(images, labels,img_height,img_width)
# print(X[:10])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1, shuffle = True)
y_train = pad_sequences(y_train, maxlen=max_length, padding='post', value = len(characters))
y_test = pad_sequences(y_test, maxlen=max_length, padding='post', value = len(characters))
print(X_train.shape)

print(y_train.shape)