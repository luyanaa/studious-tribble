import tensorflow as tf
import tensorflow_datasets as tfds
import keras
import sklearn.model_selection
import os
from keras.preprocessing.image import ImageDataGenerator, load_img
import keras.models

def buildVGG16Model(imageWidth: int, imageHeight: int, imageChannel: int):
    model=keras.Sequential()
    model.add(keras.layers.Conv2D(64,(3,3),padding='same',input_shape=(imageWidth,imageHeight,3),activation='sigmoid'))
    model.add(keras.layers.BatchNormalization())
    model.add(keras.layers.Conv2D(64,(3,3),padding='same',activation='sigmoid'))
    model.add(keras.layers.BatchNormalization())
    model.add(keras.layers.MaxPooling2D((2,2),strides=2))
    
    model.add(keras.layers.Conv2D(128,(3,3),padding='same',activation='sigmoid'))
    model.add(keras.layers.Conv2D(128,(3,3),padding='same',activation='sigmoid'))
    model.add(keras.layers.MaxPooling2D((2,2),strides=2))
    
    model.add(keras.layers.Conv2D(256,(3,3),padding='same',activation='sigmoid'))
    model.add(keras.layers.Conv2D(256,(3,3),padding='same',activation='sigmoid'))
    model.add(keras.layers.MaxPooling2D((2,2),strides=2))
    
    model.add(keras.layers.Conv2D(512,(3,3),padding='same',activation='sigmoid'))
    model.add(keras.layers.Conv2D(512,(3,3),padding='same',activation='sigmoid'))
    model.add(keras.layers.Conv2D(512,(3,3),padding='same',activation='sigmoid'))
    model.add(keras.layers.Conv2D(512,(3,3),padding='same',activation='sigmoid'))
    model.add(keras.layers.MaxPooling2D((2,2),strides=2))
    
    model.add(keras.layers.Conv2D(512,(3,3),padding='same',activation='sigmoid'))
    model.add(keras.layers.Conv2D(512,(3,3),padding='same',activation='sigmoid'))
    model.add(keras.layers.Conv2D(512,(3,3),padding='same',activation='sigmoid'))
    model.add(keras.layers.Conv2D(512,(3,3),padding='same',activation='sigmoid'))
    model.add(keras.layers.MaxPooling2D((2,2),strides=2))
    
    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(1024,activation='sigmoid'))
    model.add(keras.layers.Dense(1024,activation='sigmoid'))
    model.add(keras.layers.Dense(1024,activation='sigmoid'))
    model.add(keras.layers.Dense(2,activation='softmax'))

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
    vggModel = buildVGG16Model(128, 128, 3)
    vggModel.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])
    vggModel.summary()


    epochs = 30
    history = vggModel.fit_generator(
        train_data, 
        epochs=epochs,
        validation_data=valid_data, 
        validation_steps=val.shape[0]//16,
        steps_per_epoch=train.shape[0]//16
    )
    vggModel.save('vgg16Epoch30.h5')


