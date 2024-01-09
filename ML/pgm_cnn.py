import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
import os

NUM_EPOCHS = 500

STEPS_PER_EPOCH_TRAINING = 20
STEPS_PER_EPOCH_VALIDATION = 20

BATCH_SIZE_TRAINING = 15
BATCH_SIZE_VALIDATION = 2

BATCH_SIZE_TESTING = 1

import keras
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.models import Sequential
from keras import optimizers
from keras import regularizers
from keras.layers.normalization import BatchNormalization

def cnn(input_shape=(200,150,3)):
  
	model = Sequential()
	model.add(Conv2D(64, kernel_size=(4, 4), activation='relu', input_shape=input_shape))
	model.add(BatchNormalization())
	model.add(MaxPooling2D(pool_size=(2, 4)))
    
    
	model.add(Conv2D(64, (3, 5), activation='relu', kernel_regularizer=regularizers.l2(0.04)))
	model.add(MaxPooling2D(pool_size=(2, 2)))
	model.add(Dropout(0.2))
    
	model.add(Conv2D(64, (2, 2), activation='relu'))
	model.add(BatchNormalization())
	model.add(MaxPooling2D(pool_size=(2, 2)))
	model.add(Dropout(0.2))
    
	model.add(Flatten())
	model.add(Dense(64, activation='relu', kernel_regularizer=regularizers.l2(0.04)))
	model.add(Dropout(0.5))
	model.add(Dense(32, activation='relu', kernel_regularizer=regularizers.l2(0.04)))
    
	model.add(Dense(9, activation='softmax'))
  
	model.compile(loss=keras.losses.categorical_crossentropy,
                  optimizer=optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.0),
                  metrics=['accuracy'])
 
	model.summary()
	return model

model = cnn()

from keras.applications.vgg16 import preprocess_input
from keras.preprocessing.image import ImageDataGenerator

data_generator = ImageDataGenerator(preprocessing_function=preprocess_input)

train_generator = data_generator.flow_from_directory(
        'dataset/train',
        target_size=(200,150),
        batch_size=BATCH_SIZE_TRAINING,
        class_mode='categorical')

validation_generator = data_generator.flow_from_directory(
        'dataset/valid',
        target_size=(200,150),
        batch_size=BATCH_SIZE_VALIDATION,
        class_mode='categorical') 


fit_history = model.fit_generator(
        train_generator,
        steps_per_epoch=STEPS_PER_EPOCH_TRAINING,
        epochs = NUM_EPOCHS,
        validation_data=validation_generator,
        validation_steps=STEPS_PER_EPOCH_VALIDATION
)

model.save('model.hdf5')

#print(fit_history.history.keys())

plt.figure(1, figsize = (15,8)) 
    
plt.subplot(221)  
plt.plot(fit_history.history['acc'])  
plt.plot(fit_history.history['val_acc'])  
plt.title('model accuracy')  
plt.ylabel('accuracy')  
plt.xlabel('epoch')  
plt.legend(['train', 'valid']) 
    
plt.subplot(222)  
plt.plot(fit_history.history['loss'])  
plt.plot(fit_history.history['val_loss'])  
plt.title('model loss')  
plt.ylabel('loss')  
plt.xlabel('epoch')  
plt.legend(['train', 'valid']) 

plt.show()
