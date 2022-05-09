# -*- coding: utf-8 -*-
"""PCA-1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15bFQpoDveDW_uszhJj1rm0XBJSVASW2h
"""

from sklearn.datasets import load_iris
import pandas as pd

# %%
iris = load_iris() #iris datasetin yüklenmesi

data = iris.data
feature_names = iris.feature_names
y = iris.target

df = pd.DataFrame(data,columns = feature_names)
df["sinif"] = y

x = data

#%% PCA
from sklearn.decomposition import PCA
pca = PCA(n_components = 2, whiten= True ) #n_components = içerik sayısını tutar # n_components == min(n_samples, n_features) # whitten = normalize
pca.fit(x) # x değeri ile modeli fit eder

x_pca = pca.transform(x) # x'e dimensionality reduction uygular

print("variance ratio: ", pca.explained_variance_ratio_) # explained_varience_ratio = Seçilen bileşenlerin her biri tarafından açıklanan varyans yüzdesi

print("sum: ",sum(pca.explained_variance_ratio_))

#%% 2D
# Dataset ile verilen verinin 2D olarak görselleştirilmesi
df["p1"] = x_pca[:,0]
df["p2"] = x_pca[:,1]

color = ["red","green","blue"]

import matplotlib.pyplot as plt
for each in range(3):
    plt.scatter(df.p1[df.sinif == each],df.p2[df.sinif == each],color = color[each],label = iris.target_names[each])
    
plt.legend()
plt.xlabel("p1")
plt.ylabel("p2")
plt.show()