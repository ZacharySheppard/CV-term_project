from keras.layers import Dense, GlobalAveragePooling2D
from keras.applications import MobileNet
from keras.applications.mobilenet import preprocess_input
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Model



# imports the mobilenet model and discards the last 1000 neuron layer.
base_model = MobileNet(weights='imagenet', include_top=False)


x = base_model.output
x = GlobalAveragePooling2D()(x)
# add dense layers so that the model can learn more complex functions and classify for better results.
x = Dense(1024, activation='relu')(x)
x = Dense(1024, activation='relu')(x)
x = Dense(512, activation='relu')(x)
# final layer with softmax activation
preds = Dense(2, activation='softmax')(x)

# specify the inputs and outputs
model = Model(inputs=base_model.input, outputs=preds)

for layer in model.layers[:20]:
    layer.trainable = False
for layer in model.layers[20:]:
    layer.trainable = True

train_datagen = ImageDataGenerator(preprocessing_function=preprocess_input) #included in our dependencies

train_generator = train_datagen.flow_from_directory('/home/mark/Documents/Term 8/Image Processing/TransferLearn/Learning/',
                                                 target_size=(224,224),
                                                 color_mode='rgb',
                                                 batch_size=32,
                                                 class_mode='categorical',
                                                 shuffle=True)

test_datagen = ImageDataGenerator(rescale=1./255)

test_generator = train_datagen.flow_from_directory('/home/mark/Documents/Term 8/Image Processing/TransferLearn/Validation/',
                                                 target_size=(224,224),
                                                 color_mode='rgb',
                                                 batch_size=32,
                                                 class_mode='categorical',
                                                 shuffle=True)


model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['accuracy'])

step_size_train = train_generator.n//train_generator.batch_size
step_size_test = test_generator.n//test_generator.batch_size
model.fit_generator(generator=train_generator,
                   steps_per_epoch=step_size_train,
                   epochs=5,
                    validation_data=train_generator,
                    validation_steps=step_size_test)

model.save("A$APKeith.h5")