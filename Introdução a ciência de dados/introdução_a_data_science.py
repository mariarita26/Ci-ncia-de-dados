# -*- coding: utf-8 -*-
"""Introdução a Data Science

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1llfSXk216MVAu2U-0V4IdtGJpRrgbJ_f
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt   #biblioteca pra gerar gráficos
import numpy as np

notas = pd.read_csv("ratings.csv")
#head = cabeçalho, só mostra as 5 primeiras linhas
notas.head()

#shape = mostra o formato da tabela, quantidade de linhas e colunas
notas.shape

notas.columns = ["usuarioID", "filmeID", "nota", "momento"]
notas.head()

notas['nota'].unique()

#contar os valores das notas
notas['nota'].value_counts()

#média das notas
print(notas['nota'].mean())

#mediana das notas
print(notas.nota.median())

#visualizar as notas em forma de histograma
notas.nota.plot(kind='hist')

#diversas medidas de dispersão 
notas.nota.describe()

#visualizar os dados de outra maneira
sns.boxplot(notas.nota)

#visualizar no eixo x
sns.boxplot(x=notas.nota)

filmes = pd.read_csv("movies.csv")
filmes.head()

filmes.columns = ['filmeId', 'titulo', 'generos'] 

filmes.head()

"""# Analisando algumas notas específicas por filme - CAP 2"""

#notas.head()

#pegar as notas em que o filme é igual a Toy Story, filme = 1
notas.query("filmeID==1").nota

#Filme Jumanji

notas.query("filmeID==2").nota.mean()

# visualizar a média de cada nota (agrupar)

medias_por_filme = notas.groupby("filmeID").nota.mean()

medias_por_filme

medias_por_filme.plot(kind='hist')

sns.boxplot(medias_por_filme)

sns.histplot(medias_por_filme, bins=10)

sns.distplot(medias_por_filme, bins=10)

plt.hist(medias_por_filme)
plt.title("Histograma das médias dos filmes")

"""#Cap 3"""

tmdb = pd.read_csv('tmdb_5000_movies.csv')

tmdb.head()

tmdb.original_language.unique()   #variavel categorica nominal

#budget => orcamento => quantitativo contínuo

#saber quantas vezes aparece cada categoria
tmdb.original_language.value_counts()  #assim é apenas uma série

# pra transformar em uma tabela (data frame), faz o seguinte:
tmdb.original_language.value_counts().to_frame()

# pra remover o índice da língua e criar uma nova coluna:
contagem_de_lingua = tmdb['original_language'].value_counts().to_frame().reset_index()

contagem_de_lingua.columns = ['original_language', 'total']
contagem_de_lingua.head()

#gráfico de barras, apresentar a língua no eixo x
sns.barplot(x='original_language', y='total', data = contagem_de_lingua)

#plot de categoria
sns.catplot(x='original_language', kind='count', data=tmdb)

#gráfico de pizza (não recomendado em nenhuma situação)
plt.pie(contagem_de_lingua['total'], labels = contagem_de_lingua['original_language'])

"""Pra melhorar a visualização dos dados, é melhor fazer um gráfico comparativo entre cada categoria, em vez de fazer a comparação por todas as línguas existentes"""

#separando as categorias pra fazer um gráfico comparativo apenas entre elas
total_por_lingua = tmdb['original_language'].value_counts()

total_geral = total_por_lingua.sum()
total_de_ingles = total_por_lingua.loc['en']
total_do_resto = total_geral - total_de_ingles
print(total_de_ingles, total_do_resto)

dados = {
    'lingua': ['ingles', 'outros'],
    'total': [total_de_ingles, total_do_resto]
}

dados

#criar um data frame em cima dos dados
dados = pd.DataFrame(dados)

sns.barplot(x='lingua', y='total', data = dados)

#visualizar os filmes diferentes de inglês
total_por_lingua_de_outros_filmes = tmdb.query("original_language != 'en'").original_language.value_counts()

total_por_lingua_de_outros_filmes

#sns.catplot(x = "original_language", kind='count', data=total_por_lingua_de_outros_filmes)
sns.catplot(x='original_language', kind='count', data=total_por_lingua_de_outros_filmes)

"""# Capítulo 6"""

notas_do_toyStory = notas.query("filmeID == 1")
notas_do_jumanji = notas.query("filmeID == 2")

#imprimir quantidade de notas dos dois filmes
print(len(notas_do_toyStory), len(notas_do_jumanji))

print("Nota média do Toy Story", notas_do_toyStory.nota.mean())
print("Nota média do Jumanji", notas_do_jumanji.nota.mean())

# a diferença entre as pessoas q gostaram e q n gostaram é mt grande?

print("Nota mediana do Toy Story", notas_do_toyStory.nota.median())
print("Nota mediana do Jumanji", notas_do_jumanji.nota.median())

filme1 = np.append(np.array([2.5] * 10), np.array([3.5] * 10))
filme2 = np.append(np.array([5.0] * 10), np.array([1.0] * 10))

print(filme1.mean(), filme2.mean())

print(np.median(filme1), np.median(filme2))

sns.distplot(filme1)
sns.distplot(filme2)

plt.hist(filme1)
plt.hist(filme2)

plt.boxplot([filme1, filme2])

sns.boxplot(notas_do_toyStory.nota)

plt.boxplot([notas_do_toyStory.nota, notas_do_jumanji.nota])

sns.boxplot(x = "filmeID", y = "nota", data = notas.query("filmeID in [1,2]"))

# desvio padrão 
notas_do_jumanji.nota.std()

