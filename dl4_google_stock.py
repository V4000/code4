#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


train_df = pd.read_csv(r"D:\Datasets\Google_Stock_Price_Train.csv")


# In[3]:


train_df


# In[4]:


test_df = pd.read_csv(r"D:\Datasets\Google_Stock_Price_Test.csv")


# In[5]:


test_df


# In[6]:


test_df.info()


# In[7]:


#Data Preprocessing
from sklearn.preprocessing import MinMaxScaler


# In[8]:


# Convert 'Close' column to string type and remove commas
train_df['Close'] = train_df['Close'].astype(str).str.replace(',', '').astype(float)
test_df['Close'] = test_df['Close'].astype(str).str.replace(',', '').astype(float)


# In[9]:


# Normalize the training and testing data separately
train_scaler = MinMaxScaler()
train_df['Normalized Close'] = train_scaler.fit_transform(train_df['Close'].values.reshape(-1, 1))
test_scaler = MinMaxScaler()
test_df['Normalized Close'] = test_scaler.fit_transform(test_df['Close'].values.reshape(-1, 1))


# In[10]:


# Convert the data to the appropriate format for RNN
x_train = train_df['Normalized Close'].values[:-1].reshape(-1, 1, 1)
y_train = train_df['Normalized Close'].values[1:].reshape(-1, 1, 1)
x_test = test_df['Normalized Close'].values[:-1].reshape(-1, 1, 1)
y_test = test_df['Normalized Close'].values[1:].reshape(-1, 1, 1)


# In[11]:


print("x_train shape: ",x_train.shape)
print("y_train shape: ",y_train.shape)
print("x_test shape: ",x_test.shape)
print("y_test shape: ",y_test.shape)


# In[12]:


train_df


# In[13]:


test_df


# In[14]:


test_df.info()


# In[15]:


#Building our Model
from keras.models import Sequential
from keras.layers import LSTM, Dense


# In[16]:


model = Sequential()
model.add(LSTM(4, input_shape=(1, 1)))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.summary()


# In[18]:


#Training our Model
model.fit(x_train, y_train, epochs=4, batch_size=1, verbose=1)


# In[19]:


#Evaluating our Model
test_loss = model.evaluate(x_test, y_test)
print('Testing loss: ', test_loss)


# In[21]:


#Testing our Model
y_pred = model.predict(x_test)


# In[22]:


# Inverse transform the normalized values to get the actual values
y_test_actual = test_scaler.inverse_transform(y_test.reshape(-1, 1))
y_pred_actual = test_scaler.inverse_transform(y_pred.reshape(-1, 1))


# In[23]:


i = 1


# In[24]:


print("Actual value: {:.2f}".format(y_test_actual[i][0]))
print("Predicted value: {:.2f}".format(y_pred_actual[i][0]))

