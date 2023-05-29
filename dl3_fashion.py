#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


class_names=['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankleboot']


# In[4]:


df1 = pd.read_csv(r"D:\Datasets\fashion-mnist_train.csv")


# In[5]:


df1


# In[6]:


x_train = df1.drop("label", axis=1).values
y_train = df1["label"].values


# In[7]:


print("x_train shape: ",x_train.shape)
print("y_train shape: ",y_train.shape)


# In[8]:


np.unique(y_train)


# In[10]:


df2 = pd.read_csv(r"D:\Datasets\fashion-mnist_test.csv")


# In[11]:


df2


# In[12]:


x_test = df2.drop("label", axis=1).values
y_test = df2["label"].values


# In[13]:


print("x_test shape: ",x_test.shape)
print("y_test shape: ",y_test.shape)


# In[15]:


#28*28=784 Pixels
x_train = x_train.reshape(60000, 28, 28)
x_test = x_test.reshape(10000, 28, 28)


# In[16]:


print(x_train[0])


# In[17]:


y_train[0]


# In[18]:


plt.imshow(x_train[0])


# In[19]:


x_test[10]


# In[20]:


y_test[10]


# In[21]:


plt.imshow(x_test[10])


# In[22]:


#Normalization & Reshaping
x_train = x_train/255
x_test = x_test/255


# In[23]:


x_train = x_train.reshape(60000, 28, 28, 1)
x_test = x_test.reshape(10000, 28, 28, 1)


# In[24]:


print("Train Shape :",x_train.shape)
print("Test Shape :",x_test.shape)
print("y_train shape :",y_train.shape)
print("y_test shape :",y_test.shape)


# In[25]:


#Building our Model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten


# In[26]:


model=Sequential()
model.add(Conv2D(64, (3,3), activation='relu', input_shape=(28,28,1)))
model.add(MaxPooling2D((2,2)))
model.add(Conv2D(64, (3,3), activation='relu'))
model.add(MaxPooling2D((2,2)))
model.add(Flatten())
model.add(Dense(128,activation='relu'))
model.add(Dense(10,activation='softmax'))
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',metrics=['accuracy'])
model.summary()


# In[28]:


#Training our Model
model.fit(x_train, y_train, epochs=3, verbose=1, validation_data=(x_test,y_test))


# In[30]:


#Testing our Model
predictions = model.predict(x_test)


# In[31]:


import numpy as np
index=10
print(predictions[index])
final_value=np.argmax(predictions[index])
print("Actual label :",y_test[index])
print("Predicted label :",final_value)
print("Class :",class_names[final_value])


# In[32]:


plt.imshow(x_test[10])


# In[33]:


#Evaluating our Model
loss, accuracy = model.evaluate(x_test, y_test)
print("Loss :",loss)
print("Accuracy (Test Data) :",accuracy*100)

