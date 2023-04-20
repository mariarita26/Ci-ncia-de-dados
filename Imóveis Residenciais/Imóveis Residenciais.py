#!/usr/bin/env python
# coding: utf-8

# # Relatório de Análise III

# ## Imóveis Residenciais

# In[2]:


import pandas as pd


# In[6]:


data = pd.read_csv('dados/aluguel.csv', sep = ';')


# In[7]:


data


# In[12]:


list(data['Tipo'].drop_duplicates())


# In[13]:


residencial = ['Quitinete',
 'Casa',
 'Apartamento',
 'Casa de Condomínio',
 'Casa de Vila']


# In[14]:


residencial


# In[29]:


# saber se os tipos de residenciais em data estão na lista de residencial 
selecao = data['Tipo'].isin(residencial)


# In[20]:


selecao


# In[30]:


dados_residencial = data[selecao]


# In[26]:





# In[32]:


dados_residencial.shape[0]


# In[33]:


data.shape[0]


# In[38]:


# ordenar corretamente os índices de dados_residencial
dados_residencial.index = range(dados_residencial.shape[0])

dados_residencial


# ## Exportando a Base de Dados

# In[41]:


dados_residencial.to_csv('dados/aluguel_residencial.csv', sep = ';', index=False)


# In[45]:


dados_residencial_2 = pd.read_csv('dados/aluguel_residencial.csv', sep = ';')


# In[46]:


dados_residencial_2






