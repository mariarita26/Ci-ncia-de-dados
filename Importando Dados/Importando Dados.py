#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


json = open('dados/aluguel.json')
print(json.read())


# In[4]:


df_json = pd.read_json('dados/aluguel.json')
df_json


# In[5]:


txt = open('dados/aluguel.txt')
print(txt.read())


# In[8]:


df_txt = pd.read_table('dados/aluguel.txt')
df_txt


# In[9]:


df_xlsx = pd.read_excel('dados/aluguel.xlsx')
df_xlsx


# In[11]:


df_html = pd.read_html('dados/dados_html_1.html')
df_html[0]


# In[12]:


get_ipython().system('pip install requests')


# In[13]:


get_ipython().system('pip install bs4')


# In[14]:


import requests
from bs4 import BeautifulSoup

url='https://www.federalreserve.gov/releases/h3/current/default.htm'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, 'html.parser')
table = soup.findAll('table')
html_file = f'<html><body>{table}</body></html>'
df = pd.read_html(html_file)

# Como a função read_html retorna uma lista de DataFrames, basta acessar as tabelas pelos índices da lista.
# Como temos três tabelas na página usamos os índices 0, 1 ou 2 para acessar os DataFrames que buscamos
df[0]

