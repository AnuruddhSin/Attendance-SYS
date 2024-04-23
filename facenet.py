import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Input, Conv2D, BatchNormalization, Activation, MaxPooling2D, Flatten, Dense
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import SparseCategoricalCrossentropy

def FaceNet(input_shape=(160, 160, 3), embedding_size=128):
    input = Input(shape=input_shape)

    # Convolutional layers
    x = Conv2D(32, (3, 3), padding='same')(input)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    x = MaxPooling2D((2, 2))(x)


    # Flatten and dense layers
    x = Flatten()(x)
    x = Dense(256)(x)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    output = Dense(embedding_size)(x)

    model = Model(inputs=input, outputs=output)
    return model

# Create and compile the FaceNet model
model = FaceNet()
model.compile(optimizer=Adam(), loss=SparseCategoricalCrossentropy())

model.save("facenet_model.h5")
