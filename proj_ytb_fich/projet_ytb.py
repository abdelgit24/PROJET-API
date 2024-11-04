#import les packages
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#collecter les noms des fichiers (datasets):
files=[file for file in os .listdir(r'C:\Users\user\Desktop\revisionpython\projet_yout')]
for file in files:
    print(file)

#creer une base de données:
path=r'C:\Users\user\Desktop\revisionpython\projet_yout'
all_data=pd.DataFrame()

for file in files:
    current_data=pd.read_csv(path+'\\'+file)
    all_data=pd.concat([all_data,current_data])
print(all_data)

#rassembler tous les fichiers en un fichie csv:
path2=r'C:\Users\user\Desktop\revisionpython'
all_data.to_csv(path2+'\\all_data.csv',index=False)
print(all_data.dtypes)
#afficher les valeurs manquants:
print(all_data.isnull().sum())

#supprimer les valeurs manquants:
all_data=all_data.dropna(how='all')
print(all_data.shape)