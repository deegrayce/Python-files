#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install matplotlib')


# In[3]:


import matplotlib.pyplot as plt


# In[4]:


import pandas as pd
import seaborn as sns
sns.set() #setting seaborn as the default style for chart


# In[38]:


df = pd.read_excel(r'C:\\Users\\ODUNAYO\\Documents\\python training\\visualisations.xlsx')
df


# In[48]:


plt.figure(figsize=(10,6))

plt.bar(x=df['State'], height=df['Population'], color= 'midnightblue')

plt.xticks(rotation=45)
plt.title ('state and population', fontsize=16)
plt.show()


# In[41]:


df


# In[51]:


df2=pd.read_excel(r'C:\\Users\\ODUNAYO\\Documents\\python training\\visualisations.xlsx', sheet_name="pie_chart", skiprows=3)
df2


# In[164]:


plt.figure (figsize= (10,6))

plt.pie(x=df['Population'], labels=df['State'], autopct='%.2f%%')

#plt.title('States and population', fontsize=16, fontweight= 'bold')

plt.show()
plt.savefig('population by state.png')


# In[69]:


df3=pd.read_excel(r'C:\\Users\\ODUNAYO\\Documents\\python training\\visualisations.xlsx', sheet_name="line_chart")
df3


# In[70]:


df3.info()


# In[74]:


df3.dtypes


# In[87]:


#convert date to datetime datatype
df3['Newdate']=pd.to_datetime(df3['Date'])
df3['Newdate']


# In[88]:


df3.head()


# In[120]:


labels = ['Google price', 'Amazon price']
plt.figure (figsize= (20,8))
plt.plot(df3['Newdate'], df3['Google'])
plt.plot(df3['Newdate'], df3['Amazon'])


plt.legend(labels=labels)

plt.show()


# In[115]:


df4=pd.read_excel(r'C:\\Users\\ODUNAYO\\Documents\\python training\\visualisations.xlsx', sheet_name="histogram")
df4


# In[131]:


plt.figure (figsize= (10,6))

plt.hist(df4['Age'], bins=8, color= '#23a65c')


plt.show()


# In[8]:


df5=pd.read_excel(r'C:\\Users\\ODUNAYO\\Documents\\python training\\visualisations.xlsx', sheet_name="area_chart", skiprows=2)
df5


# In[16]:


df5.rename({'Movie Genre': 'Month'}, axis =1, inplace=True)
df5


# In[32]:


#labels=['Comedy','Thriller','Documentary'.'Romance']
plt.figure (figsize= (20,8))

plt.stackplot(df5['Month'],
             df5['Comedy'],
             df5['Thriller'],
             df5['Documentary'],
             df5['Romance'])

#plt.legend(labels=labels)

plt.show() 


# In[ ]:





# In[ ]:




