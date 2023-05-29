#!/usr/bin/env python
# coding: utf-8

# In[3]:


from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array


# In[12]:


train_dir = r"D:\Datasets\New Plant Diseases Dataset(Augmented)\train"
val_dir = r"D:\Datasets\New Plant Diseases Dataset(Augmented)\valid"


# In[13]:


img_size = 224
batch_size = 32


# In[14]:


#Preprocessing
train_datagen = ImageDataGenerator(rescale=1./255)
train_generator = train_datagen.flow_from_directory(train_dir,
target_size=(img_size, img_size),
batch_size=batch_size,
class_mode='categorical')


# In[15]:


val_datagen = ImageDataGenerator(rescale=1./255)
val_generator = val_datagen.flow_from_directory(val_dir,
target_size=(img_size, img_size),
batch_size=batch_size,
class_mode='categorical')


# In[16]:


list(train_generator.class_indices)


# In[17]:


#Building our Model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization


# In[18]:


model = Sequential()
model.add((Conv2D(32, (3,3), activation='relu', input_shape=(img_size, img_size, 3))))
model.add(BatchNormalization())
model.add((MaxPooling2D(2,2)))
model.add((Conv2D(64, (3,3), activation='relu')))
model.add(BatchNormalization())
model.add((MaxPooling2D(2,2)))
model.add((Conv2D(64, (3,3), activation='relu')))
model.add(BatchNormalization())
model.add((MaxPooling2D(2,2)))
model.add((Conv2D(128, (3,3), activation='relu')))
model.add(BatchNormalization())
model.add((MaxPooling2D(2,2)))
model.add((Flatten()))
model.add((Dense(128, activation='relu')))
model.add((Dropout(0.2)))
model.add((Dense(64, activation='relu')))
model.add((Dense(train_generator.num_classes, activation='softmax')))
model.summary()


# In[19]:


model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])


# In[22]:


#Training our Model
model.fit(train_generator, epochs=2, validation_data=val_generator)


# In[23]:


#Evaluating our Model
loss, accuracy = model.evaluate(val_generator)
print("Loss :",loss)
print("Accuracy (Test Data) :",accuracy*100)


# In[26]:


#Testing our Model
import numpy as np
img_path =r"D:\Datasets\New Plant Diseases Dataset(Augmented)\valid\Tomato___Early_blight\5b86ab6a-3823-4886-85fd-02190898563c___RS_Erly.B 8452.JPG"
img = load_img(img_path, target_size=(224, 224))
img_array = img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array /= 255.


# In[27]:


prediction = model.predict(img_array)
class_names=['Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___healthy']


# In[28]:


predicted_class = np.argmax(prediction)
print(prediction)
print(predicted_class)
print('Predicted class:', class_names[predicted_class])

