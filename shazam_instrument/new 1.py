import tensorflow as tf
import cv2 as cv

logdir = "c:\\tmp\\mnistv1\\" 
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=logdir)


mnist = tf.keras.datasets.mnist
(img_train, label_train ), (img_test, label_test) = mnist.load_data()
# Normalisation entre 0 et 1
img_train = img_train / 255

model = tf.keras.Sequential()
couche0 = tf.keras.layers.Flatten()
couche1 = tf.keras.layers.Dense(32, activation='relu')
couche2 = tf.keras.layers.Dense(10,activation='softmax')
model.add(couche0)
model.add(couche1)
model.add(couche2)
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
model.fit(img_train,label_train,batch_size=32,epochs=10,callbacks=[tensorboard_callback])
print(model.summary())

