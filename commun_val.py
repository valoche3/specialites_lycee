# +
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Charger le dataset
df = pd.read_csv("fr-en-effectifs-specialites-triplettes-1ere-generale.csv", delimiter=';')  # Ajustez le délimiteur si nécessaire

# Afficher les premières lignes et les informations générales
print(df.head())
#print(df.info())

# Vérifier les valeurs manquantes
#print(df.isnull().sum())

df.describe()
# -

# Convertir les colonnes de type objet en type numérique si nécessaire
# Par exemple, si une colonne 'Effectifs' est en texte, on la convertit :
df['EFFECTIF TOTAL'] = pd.to_numeric(df['EFFECTIF TOTAL'], errors='coerce')

# +
#calcul des triplettes les moins choisies en tout

#on cherche les colonnes que l'on veut enlever
print(df.columns)

#on enlève les colonnes correspondant qu'à une spécialité
i = 17 
L = []
while i <= 54 : 
    L.append(i)
    i+=1

df = df.drop(df.columns[L], axis = 1)
df = df.drop(columns = ['1087 - EDUC.PHYSIQUE PRATIQUE & CULT.SPORTIVE - filles',
       '1087 - EDUC.PHYSIQUE PRATIQUE & CULT.SPORTIVE - garçons'], axis = 1)
df.head(5)
# +
#on garde que la rentrée 2021

df = df[df['RENTREE SCOLAIRE'] == 2021]
df


# +
#on garde que les effectifs

df = df.loc[:,'EFFECTIF TOTAL':]
df

# +
#on additionne les valeurs sur la totalité de la rentrée 2021

df.sum(axis = 0).to_frame().T

# +
#création du nouveau dataframe qui va accueillir les sommes pour les filles et les garçons
df2 = df.iloc[:,:1].copy()

#calcul des sommes et remplissage du nouveau dataframe
i = 3
while i < 40 : 
    nom = df.columns[i].replace(" - filles", "")
    df2[nom] = df[[df.columns[i], df.columns[i+1]]].sum(axis = 1)
    i += 2
df2

# +
df2 = df2.drop(['EFFECTIF TOTAL'], axis = 1)

serie = df2.sum(axis = 0)
print(serie)
valeurs = serie.tolist()
print(valeurs)

plt.plot(df2.columns, valeurs)
# -

plt.pie(valeurs, labels = df2.columns)
plt.show()




