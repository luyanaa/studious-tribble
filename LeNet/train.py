import tensorflow as tf
import tensorflow_datasets as tfds
import keras
import sklearn.model_selection
import os
from keras.preprocessing.image import ImageDataGenerator, load_img

def buildLeNetModel(imageWidth: int, imageHeight: int, imageChannel: int):
    model = keras.Sequential()
    model.add(keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(imageWidth, imageHeight, imageChannel)))
    model.add(keras.layers.BatchNormalization())
    model.add(keras.layers.MaxPooling2D(pool_size=(2,2)))
    model.add(keras.layers.Dropout(0.25))

    model.add(keras.layers.Conv2D(64, (3,3), activation='relu', input_shape=(imageWidth, imageHeight, imageChannel)))
    model.add(keras.layers.BatchNormalization())
    model.add(keras.layers.MaxPooling2D(pool_size=(2,2)))
    model.add(keras.layers.Dropout(0.25))

    model.add(keras.layers.Conv2D(128, (3,3), activation='relu', input_shape=(imageWidth, imageHeight, imageChannel)))
    model.add(keras.layers.BatchNormalization())
    model.add(keras.layers.MaxPooling2D(pool_size=(2,2)))
    model.add(keras.layers.Dropout(0.25))

    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(512, activation='relu'))
    model.add(keras.layers.BatchNormalization())
    model.add(keras.layers.Dropout(0.5))
    model.add(keras.layers.Dense(2, activation='softmax'))

    return model

if __name__ == '__main__':
    # Data Preprocessing
    # Read data from tensorflow_dataset
    # https://www.tensorflow.org/datasets/catalog/cats_vs_dogs?hl=en
    filenames=os.listdir("./dogs-vs-cats/train")
    categories=[]
    for data in filenames:
        category=data.split('.')[0]
        if category == 'dog':
            categories.append(1)
        else:
            categories.append(0)

    import pandas 
    df = pandas.DataFrame({'image': filenames, 'label': categories})
    df["label"] = df["label"].replace({0:'cat',1:'dog'})
    train, val = sklearn.model_selection.train_test_split(df, test_size=0.2, random_state=19260817)
    train = train.reset_index(drop=True)
    val = val.reset_index(drop=True)

    train_data = ImageDataGenerator(rotation_range=15, rescale=1./255, shear_range=0.1, zoom_range=0.2, horizontal_flip=True, width_shift_range=0.1, height_shift_range=0.1)\
        .flow_from_dataframe(train, "./dogs-vs-cats/train/", x_col='image', y_col='label', target_size=(128, 128), class_mode='categorical', batch_size=16)
    valid_data = ImageDataGenerator(rotation_range=15, rescale=1./255, shear_range=0.1, zoom_range=0.2, horizontal_flip=True, width_shift_range=0.1, height_shift_range=0.1)\
        .flow_from_dataframe(val, "./dogs-vs-cats/train/", x_col='image', y_col='label', target_size=(128, 128), class_mode='categorical', batch_size=16)

    # Model Preparation
    # Resize all input data into 128x128
    LeNetModel = buildLeNetModel(128, 128, 3)
    LeNetModel.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])
    LeNetModel.summary()

    # Training
    from keras.callbacks import EarlyStopping, ReduceLROnPlateau
    callbacks = [EarlyStopping(patience=10), ReduceLROnPlateau(monitor='val_accuracy', patience=2, verbose=1, factor=0.5, min_lr=0.00001)]

    epochs = 200
    history = LeNetModel.fit_generator(
        train_data, 
        epochs=epochs,
        validation_data=valid_data, 
        validation_steps=val.shape[0]//16,
        steps_per_epoch=train.shape[0]//16, 
        callbacks=callbacks
    )
    LeNetModel.save('LeNetSGDEpoch200.h5')
    
    # RMSprop
    # Epoch=20 0.8738 0.7214 with 128x128 without LR Reducing (Highest at Epoch18 0.8636 0.8411)
    # Epoch=10 0.8569 0.8311 with 128x128 with LR Reducing (Highest at Epoch 9 0.8519 0.8700)

    # SGD
    # Epoch=10 0.7804 0.7462
