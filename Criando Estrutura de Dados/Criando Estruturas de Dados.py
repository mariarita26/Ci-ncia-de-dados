#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# # Series

# In[2]:


data = [1, 2, 3, 4, 5] 


# In[3]:


s = pd.Series(data)


# In[4]:


s


# In[10]:


index = ['Linhas' + str(i) for i in range(5)]


# In[12]:


index


# In[15]:


s = pd.Series(data = data, index = index)


# In[16]:


s


# In[17]:


# criando dicionário de dados
data = {'Linha' + str(i) : i + 1 for i in range(5)}


# In[18]:


data


# In[25]:


s = pd.Series(data)


# In[26]:


s


# # DataFrame

# In[27]:


data = [[1,2 ,3], 
        [4, 5, 6], 
        [7, 8, 9]]


# In[28]:


data


# In[30]:


df1 = pd.DataFrame(data = data)


# In[31]:


df1


# In[32]:


index = ['Linha' + str(i) for i in range(3)]


# In[33]:


index


# In[34]:


df1 = pd.DataFrame(data = data, index = index)


# In[35]:


df1


# In[37]:


columns = ['Coluna' + str(i) for i in range(3)]


# In[40]:


df1 = pd.DataFrame(data = data, index = index, columns = columns)


# In[41]:


df1


# In[44]:


data = {'Coluna0': {'Linha0': 1, 'Linha1': 4, 'Linha2': 7},
       'Coluna1': {'Linha0': 2, 'Linha1': 5, 'Linha2': 8},
       'Coluna2': {'Linha0': 3, 'Linha1': 6, 'Linha2': 9}}


# In[45]:


data


# In[46]:


df2 = pd.DataFrame(data)


# In[47]:


df2


# In[48]:


data = [(1,2 ,3), 
        (4, 5, 6), 
        (7, 8, 9)]


# In[49]:


data


# In[50]:


df3 = pd.DataFrame(data = data, index = index, columns = columns)


# In[51]:


df3


# In[52]:


df1[df1 > 0] = 'A'
df1


# In[63]:


df2[df2 > 0] = 'B'
df2


# In[61]:


df3[df3 > 0] = 'C'
df3


# In[65]:


df4 = pd.concat([df1, df2, df3])


# In[66]:


df4


# In[67]:


df4 = pd.concat([df1, df2, df3], axis = 1)
df4


# In[ ]:




