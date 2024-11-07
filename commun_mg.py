# +
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Charger le dataset
df = pd.read_csv("fr-en-effectifs-specialites-triplettes-1ere-generale.csv", delimiter=';')  # Ajustez le délimiteur si nécessaire

# Afficher les premières lignes et les informations générales
print(df.head())
print(df.info())

# Vérifier les valeurs manquantes
print(df.isnull().sum())


# +

# Convertir les colonnes de type objet en type numérique si nécessaire
# Par exemple, si une colonne 'Effectifs' est en texte, on la convertit :
df['EFFECTIF TOTAL'] = pd.to_numeric(df['EFFECTIF TOTAL'], errors='coerce')

# -

# Statistiques de base
print(df.describe())


#calcul de l'effectif total sur la france chaque année
df_2021 = df[df['RENTREE SCOLAIRE'] == 2021]
eff_tot_2021 = df_2021['EFFECTIF TOTAL'].sum()
print(eff_tot_2021)


