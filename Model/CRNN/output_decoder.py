prediction_model = keras.models.Model(
    model.get_layer(name="input_data").input, model.get_layer(name="pred").output
)
prediction_model.summary()
def decode_to_text(output):
    text_label = ""
    for c in output:
        if c in num_to_char:
            text_label += num_to_char[c]

    return text_label
def decode_model_output(y_pred):
    result = keras.backend.ctc_decode(y_pred, 
                                        input_length=np.ones(y_pred.shape[0])*y_pred.shape[1],
                                        greedy=True)[0][0][:,:max_length] 
    labels = []
    for output in result.numpy():
        labels.append(decode_to_text(output))

    return labels


y_pred = prediction_model.predict(X_test) # y_pred shape = (104,50,20)
label_pred = decode_model_output(y_pred)
for i in range(len(X_test)):
    image = X_test[i]
    label_truth = decode_to_text(y_test[i])
    print(f'Ground truth: {label_truth} \t Predicted: {label_pred[i]}')

