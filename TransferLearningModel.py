from keras.layers import Dense, GlobalAveragePooling2D, Dropout, Flatten
from keras.applications import MobileNet, VGG16
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Model, Sequential
from keras import optimizers
from keras.callbacks import EarlyStopping
from matplotlib import pyplot as plt




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

model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['acc'])

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

early_stopping = EarlyStopping(monitor='val_loss', patience=3)

history = model.fit_generator(generator=train_generator,
                   steps_per_epoch=step_size_train,
                   epochs=5,
                    validation_data=test_generator,
                    validation_steps=step_size_test,
                    callbacks=[early_stopping]
                    )
model.save("A$APKeith.h5")

acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(len(acc))
plt.plot(epochs, acc, 'b', label='Training acc')
plt.plot(epochs, val_acc, 'r', label='Validation acc')
plt.title('Training and validation accuracy')
plt.legend()
plt.figure()
plt.plot(epochs, loss, 'b', label='Training loss')
plt.plot(epochs, val_loss, 'r', label='Validation loss')
plt.title('Training and validation loss')
plt.legend()
plt.show()

