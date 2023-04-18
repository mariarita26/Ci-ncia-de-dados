#!/usr/bin/env python
# coding: utf-8

# # Relatório de Análise I

# ## Importando a Base de Dados

# In[4]:


import pandas as pd

# pra separar os dados com ; é só colocar o sep
pd.read_csv('dados/aluguel.csv', sep = ';')


# In[5]:


dados = pd.read_csv('dados/aluguel.csv', sep=';')


# In[6]:


dados


# In[7]:


type(dados)


# In[8]:


dados.info()


# In[10]:


dados.head()


# ## Informações Gerais sobre a Base de Dados

# In[12]:


dados.dtypes


# In[15]:


tipos_de_dados = pd.DataFrame(dados.dtypes, columns = ['Tipos de Dados'])


# In[17]:


tipos_de_dados.columns.name = 'Variáveis'


# In[18]:


tipos_de_dados


# In[19]:


dados.shape


# In[20]:


# quantidade de variáveis
dados.shape[1]


# In[21]:


print('A base de dados apresenta {} registros (imóveis) e {} variáveis'.format(dados.shape[0], dados.shape[1]))


# In[22]:





# In[23]:





# In[24]:




