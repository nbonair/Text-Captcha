fig=plt.figure(figsize=(20, 10))
fig.add_subplot(2, 4, 1)
plt.imshow(X_train[0], cmap='gray')
#plt.imshow(X_train[0].transpose((1,0,2)), cmap='gray')
plt.title('Image from X_train with label '+ str(y_train[0]))
plt.axis('off')
fig.add_subplot(2, 4, 2)
plt.imshow(X_train[len(X_train)-1], cmap='gray')
#plt.imshow(X_train[935].transpose((1,0,2)), cmap='gray')
plt.title('Image from X_train with label '+ str(y_train[len(X_train)-1]))
plt.axis('off')
fig.add_subplot(2, 4, 3)
plt.imshow(X_test[0], cmap='gray')
#plt.imshow(X_test[0].transpose((1,0,2)), cmap='gray')
plt.title('Image from X_test with label '+ str(y_test[0]))
plt.axis('off')
fig.add_subplot(2, 4, 4)
plt.imshow(X_test[len(X_test)-1], cmap='gray')
#plt.imshow(X_test[103].transpose((1,0,2)), cmap='gray')
plt.title('Image from X_test with label '+ str(len(X_test)-1))
plt.axis('off')

