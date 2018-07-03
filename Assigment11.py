
# coding: utf-8

# In[1]:


#this assigment is for visualization using matplotlib


import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


# In[2]:


titanic = pd.read_csv("https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv")
titanic


# In[3]:


#create a pie presenting the male/female proportion


# In[4]:


titanic.groupby('sex').agg('count').plot(kind='pie', y='name')
plt.show()


# In[5]:


#create a scatterplot  with the fare paid and the age, differ the plot color by gender.


# In[6]:


plt.scatter(titanic['age'], titanic['fare'])
plt.show()

