#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


raw_data = pd.read_csv(r'C:\\Users\\ODUNAYO\\Documents\\python training\\Absenteeism_Data.csv')
raw_data


# In[4]:


#creating a copy of the original dataset to preserve the original data while altering it
df=raw_data.copy()
df


# In[5]:


#shows us the number of columns and non-null rows
df.info()


# In[6]:


# removing the limit, to display all the data
pd.options.display.max_rows = None
pd.options.display.max_columns = None
df


# In[7]:


#dropping id column as it is not relevant to our analysis

df.drop('ID', axis='columns', inplace=True)
df.head()


# In[8]:


df['Reason for Absence']


# In[9]:


df['Reason for Absence'].nunique()


# In[10]:


df['Reason for Absence'].unique()


# In[11]:


df['Reason for Absence'].min()


# In[12]:


df['Reason for Absence'].max()


# In[13]:


df['Reason for Absence'].unique()


# In[14]:


#Arranging the values in ascending order)
sorted(df['Reason for Absence'].unique())


# ## .getdummies()

# In[15]:


pd.get_dummies(df['Reason for Absence'])


# In[16]:


# allocating it to a variable
reasons_columns= pd.get_dummies(df['Reason for Absence'])


# In[17]:


reasons_columns['Check']= reasons_columns.sum(axis=1)


# In[18]:


reasons_columns.head()


# In[19]:


reasons_columns=pd.get_dummies(df['Reason for Absence'], drop_first=True)
reasons_columns.head()


# In[20]:


#Grouping our reasons for absence column into 4 categories

group_1=reasons_columns.loc[:,1:14].max(axis=1)
group_2=reasons_columns.loc[:,15:17].max(axis=1)
group_3=reasons_columns.loc[:,18:21].max(axis=1)
group_4=reasons_columns.loc[:,22:28].max(axis=1)


# In[21]:


df.iloc[3,2:5]


# In[22]:


#difference between loc and iloc
df.loc[3,['Transportation Expense', 'Age']]


# In[23]:


df.drop('Reason for Absence', axis='columns', inplace=True)


# In[24]:


#we can drop the resons columns because weve grouped 28 reasons into 4 categories


# In[25]:


df.head()


# In[26]:


#merging the categories with our dataset
pd.concat([df,group_1,group_2,group_3,group_4], axis='columns')


# In[28]:


df=pd.concat([df,group_1,group_2,group_3,group_4], axis='columns')


# In[29]:


df.head()


# In[34]:


#df.drop([0,1,2,3], axis='columns', inplace=True) - to drop multiple columns


# In[30]:


df.columns.values


# In[31]:


col_names=['Date', 'Transportation Expense', 'Distance to Work', 'Age',
       'Daily Work Load Average', 'Body Mass Index', 'Education',
       'Children', 'Pets', 'Absenteeism Time in Hours', 'reason1', 'reason2', 'reason3','reason4']


# In[32]:


df.columns= col_names
df


# In[33]:


#for ease of copying my column names and avoiding errors in spelling
df.columns.values


# In[34]:


#rearranging the columns
reordered =['reason1', 'reason2', 'reason3', 'reason4', 'Date', 'Transportation Expense', 'Distance to Work', 'Age',
       'Daily Work Load Average', 'Body Mass Index', 'Education',
       'Children', 'Pets', 'Absenteeism Time in Hours']


# In[35]:


df=df[reordered]


# In[36]:


df.head()


# In[46]:


#creating a copy of df and checkpointing this position to save my work
df_mod = df.copy()
df_mod


# In[47]:


df_mod['Date']


# In[48]:


pd.to_datetime(df_mod['Date'])


# In[51]:


#telling pandas the date format to follow
df_mod['Date']=pd.to_datetime(df_mod['Date'], format= '%d/%m/%Y')


# In[52]:


df_mod.head(10)


# ## Extracting month

# In[54]:


# .dt as function to access date e.g .dt.month
df_mod['Date'].dt


# In[55]:


df_mod['Date'].dt.month


# In[56]:


df_mod['Month Value']=df_mod['Date'].dt.month


# In[58]:


df_mod.head()


# In[60]:


df_mod['Month Value'].unique()


# ## Extracting day of the week

# In[63]:


df_mod['Week']=df_mod['Date'].dt.isocalendar().week


# In[64]:


df_mod.head()


# In[65]:


df_mod['Day of the week']=df_mod['Date'].dt.weekday


# In[69]:


df_mod.head()


# ## Mapping
# Where education level 1= high school, 2= bachelors 3= masters 4= doctorate. We will map it into two categories 0= non-graduate/high school graduate while 1 =graduate i.e bachelors, masters and doctorate

# In[71]:


df_mod['Education'].unique()


# In[73]:


df_mod['Education'].value_counts()


# In[75]:


df_mod['Education']=df_mod['Education'].map({1:0, 2:1, 3:1, 4:1})
                                             


# In[76]:


df_mod.head()


# In[77]:


#checking that my code ran well
df_mod['Education'].unique()


# In[ ]:




