#!/usr/bin/env python
# coding: utf-8

# # Relatório de Análise II

# ## Tipos de Imóveis 

# In[2]:


import pandas as pd 


# In[3]:


dados = pd.read_csv('dados/aluguel.csv', sep = ';')


# In[4]:


dados.head(10)


# In[5]:


dados['Tipo']


# In[9]:


dados.Tipo


# In[7]:


tipo_de_imovel = dados.Tipo


# In[8]:


type(tipo_de_imovel)


# In[10]:


# remover duplicadas
tipo_de_imovel.drop_duplicates()


# In[11]:


# remove automaticamente as duplicadas da variável
tipo_de_imovel.drop_duplicates(inplace = True)


# In[12]:


tipo_de_imovel


# ## Organizando a Visualização

# In[13]:


tipo_de_imovel = pd.DataFrame(tipo_de_imovel)


# In[14]:


tipo_de_imovel


# In[21]:


#descobrir o tamanho do dataframe
tipo_de_imovel.shape[0]


# In[16]:


range(tipo_de_imovel.shape[0])


# In[17]:


for i in range(tipo_de_imovel.shape[0]):
    print(i)


# In[18]:


tipo_de_imovel.index = range(tipo_de_imovel.shape[0])


# In[22]:


tipo_de_imovel.index


# In[23]:


tipo_de_imovel


# In[24]:


tipo_de_imovel.columns.name = 'Id'


# In[25]:


tipo_de_imovel


# In[ ]:




