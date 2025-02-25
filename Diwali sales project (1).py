#!/usr/bin/env python
# coding: utf-8

# # DIWALI SALES ANALYSIS

# # 1.Loading Data 

# Importing python library

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


df = pd.read_csv(r'C:\Users\NIKHIL YADAV\OneDrive\Desktop\Diwali_Sales_Data.csv', encoding ='unicode_escape')


# # 2.Analyze Dataset

# In[3]:


df.head()


# In[4]:


df.shape


# In[5]:


df.head(10)


# In[6]:


df


# In[43]:


df.tail()


# In[44]:


df


# # 3.Data cleaning

# In[7]:


df.info()


# In[8]:


df.drop(["Status","unnamed1"],axis=1, inplace=True)
df.info()


# In[9]:


df.head()


# In[10]:


df.info()


# In[11]:


pd.isnull(df).sum()


# In[12]:


df.dropna(inplace = True)


# In[13]:


df.shape


# In[14]:


df.head()


# In[15]:


df["Amount"]=df["Amount"].astype("int")


# In[16]:


df['Amount'].dtype


# # EDA(Exploratory Data Analysis)

# In[17]:


df.columns


# In[18]:


df.describe()


# In[19]:


df.describe(include = 'object')


# # 4.Data Visualization

# In[20]:


ax = sns.countplot(x="Gender", data=df)
for bars in ax.containers:
    ax.bar_label(bars)


# In[21]:


df.groupby(["Gender"],as_index=False)["Amount"].sum().sort_values(by="Amount",ascending=False)


# From the above we can see that most of the buyers are female and even the purchasing power of female are greater than male.

# In[23]:


df.columns


# In[24]:


ax = sns.countplot(data=df , x="Age Group" , hue ="Gender")
plt.show()


# In[25]:


ax = sns.countplot(data=df , x="Age Group" , hue ="Gender")
for bars in ax.containers:
    ax.bar_label(bars)


# In[26]:


sales_age=df.groupby(["Age Group"],as_index=False)["Amount"].sum().sort_values(by="Amount",ascending=False)
sns.barplot(x="Age Group", y="Amount",data=sales_age)
plt.show()


# From the above graph we can see that the most of the buyers are of the age group between 26 to 35 years female/male.

# In[28]:


df.columns


# In[29]:


sales_state = df.groupby(["State"],as_index=False)["Orders"].sum().sort_values(by="Orders",ascending=False).head(10)
sales_state


# In[30]:


sales_state = df.groupby(["State"],as_index=False)["Orders"].sum().sort_values(by="Orders",ascending=False).head(10)
sns.set(rc={'figure.figsize': (15,6)})
sns.barplot(data=sales_state,x="State", y='Orders')


# In[31]:


sales_state = df.groupby(["State"],as_index=False)["Amount"].sum().sort_values(by="Amount",ascending=False).head(10)
sns.set(rc={'figure.figsize': (15,6)})
sns.barplot(data=sales_state,x="State", y='Amount')


# From the above graph we can see that most of the order and total sales/amount are from uttarpradesh,maharashtra and karnataka.

# In[33]:


ax=sns.countplot(data=df,x="Marital_Status")
sns.set(rc={"figure.figsize":(5,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[34]:


sales_state =df.groupby(['Marital_Status','Gender'],as_index=False)['Amount'].sum().sort_values(by="Amount",ascending=False)
sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data=sales_state,x='Marital_Status', y='Amount',hue='Gender')
plt.show()


# From the above graph we can see that most of the buyer are married(women) and they have high purchasing power.

# In[36]:


ax=sns.countplot(data=df,x="Occupation")
sns.set(rc={"figure.figsize":(20,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[37]:


sales_state =df.groupby(['Occupation'],as_index=False)['Amount'].sum().sort_values(by="Amount",ascending=False)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data=sales_state,x='Occupation', y='Amount')
plt.show()


# From the above graph we can see that most of the buyer are from IT sector,healthcare and Aviation.

# In[39]:


df.head()


# In[40]:


ax=sns.countplot(data=df,x="Product_Category")
sns.set(rc={"figure.figsize":(26,6)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[41]:


sales_state =df.groupby(['Product_Category'],as_index=False)['Amount'].sum().sort_values(by="Amount",ascending=False)
sns.set(rc={'figure.figsize':(25,6)})
sns.barplot(data=sales_state,x='Product_Category', y='Amount')
plt.show()


# From the above graph we can see that most of the solds products are from food,clothing and apparel and electronics.

# CONCLUSION:-Married women age group 26-35 from UP,Maharashtra and karnataka working in IT,Healthcare and Aviation sector are more likely to buy products from Food, Clothing and Electronic category.

# In[ ]:




