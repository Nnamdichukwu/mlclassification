

# Importing the Keras libraries and packages

import os

import keras
import numpy as np
import tensorflow as tf
from keras.models import load_model
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator

from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

from keras.models import Sequential
from keras.callbacks import ModelCheckpoint

from utils.constants import model_dir

train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)

test_datagen = ImageDataGenerator(rescale=1./255)


def _generator(folder_path=None, is_train_set=True):
    """
    Accepts a training folder path and generate training set from it.

    if a folder is not supplied, defaults to using ./datasets/training_set
    """
    if is_train_set:
        if folder_path is None:
            folder_path = './datasets/training_set'
                                                 batch_size=32,
    model_path = "./model/{}".format(model_name)

    print("Training")
    print(model_path, model_name, train_folder, test_folder)
    classifier = Sequential()

    # Step 1 - Convolution
    classifier.add(
        Conv2D(32, (3, 3), input_shape=(64, 64, 3), activation='relu'))
    # Step 2 - Pooling
    classifier.add(MaxPooling2D(pool_size=(2, 2)))

    # Adding a second convolutional layer
    classifier.add(Conv2D(32, (3, 3), activation='relu'))
    classifier.add(MaxPooling2D(pool_size=(2, 2)))
    # Step 3 - Flattening
    classifier.add(Flatten())

    # Step 4 - Full connection
    classifier.add(Dense(units=128, activation='relu'))
    classifier.add(Dense(units=1, activation='sigmoid'))
    # checkpoint

    checkpoint = ModelCheckpoint(
        model_path, monitor='val_acc', verbose=1, save_best_only=True, mode='max')
    callbacks_list = [checkpoint]
    if os.path.isfile(model_path):
        print("Resumed model's weights from {}".format(model_path))
        # load weights
        classifier.load_weights(model_path)
    # Compiling the CNN
    classifier.compile(
        optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    classifier.fit_generator(training_set, steps_per_epoch=epoch_steps, epochs=epochs, verbose=1,
                             validation_data=test_set,
                             validation_steps=2000,
                             callbacks=callbacks_list)
    print(training_set.class_indices)


def prepImage(testImage):

    test_image = image.load_img(testImage, target_size=(64, 64))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)

    return test_image


def setupTF():

    config = tf.ConfigProto(device_count={'GPU': 1})
    sess = tf.Session(config=config)
    keras.backend.set_session(sess)