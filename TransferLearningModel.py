from keras.layers import Dense, GlobalAveragePooling2D, Dropout, Flatten
from keras.applications import MobileNet, VGG16
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Model, Sequential
from keras import optimizers
from keras.callbacks import EarlyStopping


# imports the mobilenet model and discards the last 1000 neuron layer.
base_model = MobileNet(input_shape=[255, 255, 3], weights='imagenet', include_top=False)

base_model.trainable = False

model = Sequential([
    base_model,
    Flatten(),
    Dropout(0.2),
    Dense(3, activation='softmax')
])

opt = optimizers.Adam() #learning_rate=0.001

model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])

train_datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=5,
        brightness_range=[0.9, 1.1],
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

train_generator = train_datagen.flow_from_directory('/home/mark/Documents/Term 8/Image Processing/TransferLearn/Learning1/',
                                                 target_size=(255, 255),
                                                 color_mode='rgb',
                                                 batch_size=32,
                                                 class_mode='categorical',
                                                 shuffle=True)

test_datagen = ImageDataGenerator(rescale=1./255)

test_generator = test_datagen.flow_from_directory('/home/mark/Documents/Term 8/Image Processing/TransferLearn/Validation1/',
                                                 target_size=(255, 255),
                                                 color_mode='rgb',
                                                 batch_size=32,
                                                 class_mode='categorical',
                                                 shuffle=True)




step_size_train = train_generator.n//train_generator.batch_size
step_size_test = test_generator.n//test_generator.batch_size

early_stopping = EarlyStopping(monitor='loss', patience=3)

model.fit_generator(generator=train_generator,
                   steps_per_epoch=step_size_train,
                   epochs=10,
                    validation_data=test_generator,
                    validation_steps=step_size_test,
                    callbacks=early_stopping
                    )
model.save("A$APKeith.h5")