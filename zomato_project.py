#!/usr/bin/env python
# coding: utf-8

# In[21]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

df = pd.read_csv('zomato.csv')
df


# In[22]:


df


# In[23]:


df = pd.read_csv('zomato.csv', encoding='latin-1')
df.head()


# In[24]:


df.drop(['Latitude','Longitude'],axis = 1)


# In[25]:


df[['Restaurant ID', 'Restaurant Name', 'City']]


# In[26]:


df['new rating'] = df['Aggregate rating']*2
df.head(3)


# In[27]:


df.sort_values('Votes', ascending=False)


# In[28]:


df


# In[29]:


restt = df['City']=='Kolkata'
df[restt].groupby('Restaurant Name')['Aggregate rating'].agg('sum').plot(kind='bar')


# In[37]:


df.describe()


# In[32]:


df['Currency'].unique()


# In[38]:


df['Price in Rupees'] = df['Price range']


# In[39]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




