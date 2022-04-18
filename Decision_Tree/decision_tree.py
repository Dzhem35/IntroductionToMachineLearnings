# -*- coding: utf-8 -*-
"""Decision-Tree.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1chEfdWvKB6L7MqpyfAbHxYRmeTPJB2Sc
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# %%
data = pd.read_csv("data.csv") #data.csv verilerinin import edilmesi

# %%
data.drop(["id","Unnamed: 32"],axis=1,inplace=True)
# malignant = M  kotu huylu tumor
# benign = B     iyi huylu tumor

# %%
#VeriSeti icerisindeki verilerin ekrana getirilmesi
M = data[data.diagnosis == "M"]
B = data[data.diagnosis == "B"]
# scatter plot
plt.scatter(M.radius_mean,M.texture_mean,color="red",label="kotu",alpha= 0.3)
plt.scatter(B.radius_mean,B.texture_mean,color="green",label="iyi",alpha= 0.3)
plt.xlabel("radius_mean")
plt.ylabel("texture_mean")
plt.legend()
plt.show()

# %%
data.diagnosis = [1 if each == "M" else 0 for each in data.diagnosis]
y = data.diagnosis.values
x_data = data.drop(["diagnosis"],axis=1)# %%
# normalization 
x = (x_data - np.min(x_data))/(np.max(x_data)-np.min(x_data))

#%%
# train test split
from sklearn.model_selection import train_test_split
x_train, x_test,y_train, y_test = train_test_split(x,y,test_size = 0.15,random_state = 42)

# %% SVM
#Decision Tree model kutuphanesi calistirilir 
from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier(max_depth=3,criterion='gini') # Model icerisinde bulunan ozellikler verilip degistirilerek score tahmini yapilir.
dt.fit(x_train,y_train)

# DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=None,
            #max_features=None, max_leaf_nodes=None,
            #min_impurity_decrease=0.0, min_impurity_split=None,
            #min_samples_leaf=1, min_samples_split=2,
            #min_weight_fraction_leaf=0.0, presort=False, random_state=None,
            #splitter='best')   ---> Decision Tree modeli icin uygun parametler gosterildigi gibidir.

# %% test
# Yapilan score tahminin en uygun olani bulunmaya calisilir. (Bu ornek icin max_depth=3 icin en uygun score tahmini yapililir)
print("score: ", dt.score(x_test,y_test))

y_pred = dt.predict(x_test)
y_pred

# Yapilan tahminler ve veriler sonucunda Confusion Matrix olusturulur , burdanda yapilan tahminlerin yanlis ve dogrulari gozlemlenebilir.
from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, y_pred)