#!/usr/bin/env python
# coding: utf-8

# # Exploratory Data Analysis

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


df=pd.read_csv('C:\\Users\\ODUNAYO\\Documents\\python training\\titanic.csv')


# In[5]:


df.head()


# In[6]:


df.shape


# In[8]:


# to get the number of rows
df.shape[0]


# In[9]:


# to get the number of columns
df.shape[1]


# In[13]:


print(f'Titanic datase contains {df.shape[0]} rows and {df.shape[1]} columns') 


# ## Data types and missing value count

# In[15]:


df.info()


# In[17]:


#Checking for the number of missing values
df.isnull().sum()


# In[22]:


#visualising missing data

sns.heatmap(df.isnull(), 
            yticklabels=False, 
            cbar=False,
            cmap= 'viridis')


# In[23]:


#summary statistics of numerical data
df.describe()


# ## Feature analysis
# (Machine Learning)
# 
# Row = observations

# In[24]:


df.head()


# ### Categorical Variables
# 
# Categorical variables in the dataset are sex, pclass and embarked

# In[31]:


#value count of the sex column
df['Sex'].value_counts(dropna=False)


# In[32]:


#mean of survival by sex
df[['Sex', 'Survived']].groupby('Sex', as_index= False).mean()


# In[42]:


sns.barplot(x= 'Sex', 
            y= 'Survived', 
            data=df)
plt.title('Survival probability by sex', fontsize=16)
plt.ylabel('Survival Probability')


# In[34]:


#mean of survival by Pclass
df[['Pclass', 'Survived']].groupby('Pclass', as_index= False).mean()


# In[41]:


sns.barplot(x= 'Pclass', 
            y= 'Survived', 
            data=df)
plt.title('Survival probability by class', fontsize=16)
plt.ylabel('Survival Probability')


# In[40]:


sns.catplot(x= 'Pclass', 
            y= 'Survived',
            data=df,
           kind='bar',
           hue='Sex')
plt.title('Survival probability by class by sex', fontsize=16)
plt.ylabel('Survival Probability')


# In[43]:


##mean of survival by place embarked
df[['Embarked', 'Survived']].groupby('Embarked', as_index= False).mean()


# In[51]:


sns.catplot(x= 'Embarked', 
            data=df,
           kind='count',
           hue='Sex')
plt.title('Survival probability by place embarked', fontsize=14)
plt.ylabel('Survival Count', fontsize=14)


# In[ ]:




