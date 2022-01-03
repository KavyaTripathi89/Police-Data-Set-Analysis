#!/usr/bin/env python
# coding: utf-8

# # Police Dataset Analysis

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv(r"C:\Users\kavya\Downloads\3. Police Data.csv")


# In[3]:


data


# # Remove the column that only contains the missing value

# In[4]:


data.isnull().sum()


# In[5]:


data.drop(columns = 'country_name',inplace=True)


# In[6]:


data


# # For speeding, Who were stopped more often Men or Women?

# In[8]:


data[data.violation == 'Speeding'].driver_gender.value_counts()


# # Does gender affect who gets searched during a stop 

# In[9]:


data.head()


# In[11]:


data.groupby('driver_gender').search_conducted.sum()


# In[14]:


data.search_conducted.value_counts()


# # What is the mean stop duration

# In[16]:


data.head()


# In[17]:


data.stop_duration.value_counts()


# datatype of stop_duration column is string

# In[18]:


data['stop_duration'] = data['stop_duration'].map({'0-15 Min':7.5 , '16-30 Min': 24 , '30+ Min':45})


# # data

# In[24]:


data.stop_duration.mean()


# # Compare the age distribution for each violation

# In[23]:


data.groupby('violation').driver_age.describe()


# In[ ]:




