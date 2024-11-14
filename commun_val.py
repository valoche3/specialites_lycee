# +
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Charger le dataset
df = pd.read_csv("fr-en-effectifs-specialites-triplettes-1ere-generale.csv", delimiter=';')  # Ajustez le délimiteur si nécessaire

# Afficher les premières lignes et les informations générales
#print(df.head())
#print(df.info())

# Vérifier les valeurs manquantes
#print(df.isnull().sum())

#df.describe()
# -

# Convertir les colonnes de type objet en type numérique si nécessaire
# Par exemple, si une colonne 'Effectifs' est en texte, on la convertit :
df['EFFECTIF TOTAL'] = pd.to_numeric(df['EFFECTIF TOTAL'], errors='coerce')

# +
#calcul des triplettes les moins choisies en tout

#on cherche les colonnes que l'on veut enlever
#print(df.columns)

#on enlève les colonnes correspondant qu'à une spécialité
i = 17 
L = []
while i <= 54 : 
    L.append(i)
    i+=1

df = df.drop(df.columns[L], axis = 1)
df = df.drop(columns = ['1087 - EDUC.PHYSIQUE PRATIQUE & CULT.SPORTIVE - filles',
       '1087 - EDUC.PHYSIQUE PRATIQUE & CULT.SPORTIVE - garçons'], axis = 1)
#df.head(5)
# +
#on garde que la rentrée 2021

df_2021 = df[df['RENTREE SCOLAIRE'] == 2021]
#df


# +
#on garde que les effectifs

df_2021 = df_2021.loc[:,'EFFECTIF TOTAL':]
df_2021

# +
#on additionne les valeurs sur la totalité de la rentrée 2021

display(df_2021.sum(axis = 0).to_frame().T)
df_2021.iloc[0,0]

# +
#création du nouveau dataframe qui va accueillir les sommes pour les filles et les garçons
df_2021bis = df_2021.iloc[:,:1].copy()

#calcul des sommes et remplissage du nouveau dataframe
i = 3
while i < 40 : 
    nom = df_2021.columns[i].replace(" - filles", "")
    df_2021bis[nom] = df_2021[[df_2021.columns[i], df_2021.columns[i+1]]].sum(axis = 1)
    i += 2
df_2021bis

# +
#df_2021bis = df_2021bis.drop(['EFFECTIF TOTAL'], axis = 1)

serie_2021 = df_2021bis.sum(axis = 0)
valeurs_2021 = serie_2021.tolist()
frequences_2021 = [x/valeurs_2021[0] for x in valeurs_2021]
# -

# Après avoir étudié pour l'année 2021, on va faire les mêmes diagrammes pour l'année 2022 et l'année 2023 pour essayer d'observer des changements en 3 ans de nouvelle réforme du baccalauréat.

# +
#année 2022

df_2022 = df[df['RENTREE SCOLAIRE'] == 2022]
df_2022 = df_2022.loc[:,'EFFECTIF TOTAL':]

df_2022.sum(axis = 0).to_frame().T

df_2022bis = df_2022.iloc[:,:1].copy()

i = 3
while i < 40 : 
    nom = df_2022.columns[i].replace(" - filles", "")
    df_2022bis[nom] = df_2022[[df_2022.columns[i], df_2022.columns[i+1]]].sum(axis = 1)
    i += 2
    
#df_2022bis = df_2022bis.drop(['EFFECTIF TOTAL'], axis = 1)

serie_2022 = df_2022bis.sum(axis = 0)
valeurs_2022 = serie_2022.tolist()
frequences_2022 = [x/valeurs_2022[0] for x in valeurs_2022]
print(frequences_2022)

# +
#année 2023

df_2023 = df[df['RENTREE SCOLAIRE'] == 2023]
df_2023 = df_2023.loc[:,'EFFECTIF TOTAL':]

df_2023.sum(axis = 0).to_frame().T

df_2023bis = df_2023.iloc[:,:1].copy()

i = 3
while i < 40 : 
    nom = df_2023.columns[i].replace(" - filles", "")
    df_2023bis[nom] = df_2023[[df_2023.columns[i], df_2023.columns[i+1]]].sum(axis = 1)
    i += 2

#df_2023bis = df_2023bis.drop(['EFFECTIF TOTAL'], axis = 1)

serie_2023 = df_2023bis.sum(axis = 0)
valeurs_2023 = serie_2023.tolist()
frequences_2023 = [x/valeurs_2023[0] for x in valeurs_2023]
print(frequences_2023)
# -

# Maintenant que nous avons étudié les triplettes les plus choisies pour les 3 années, on va pouvoir afficher les histogrammes et les camemberts pour chacune de ces années.

#définition des labels pour mieux voir
labels = {
    '01 - MATHEMATIQUES/PHYSIQUE-CHIMIE/SCIENCES DE LA VIE ET DE LA TERRE' : 1,
    '02 - HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/LANGUES, LITT. ET CULTURES ETRA. ET R./SCIENCES ECONOMIQUES ET SOCIALES' : 2,
    '03 - HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/MATHEMATIQUES/SCIENCES ECONOMIQUES ET SOCIALES' : 3,
    '04 - HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/HUMANITES, LITTERATURE ET PHILOSOPHIE/SCIENCES ECONOMIQUES ET SOCIALES' : 4,
    '05 - MATHEMATIQUES/NUMERIQUE ET SCIENCES INFORMATIQUES/PHYSIQUE-CHIMIE' : 5,
    '06 - HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/HUMANITES, LITTERATURE ET PHILOSOPHIE/LANGUES, LITT. ET CULTURES ETRA. ET R.' : 6,
    '07 - MATHEMATIQUES/PHYSIQUE-CHIMIE/SCIENCES DE L INGENIEUR' : 7,
    '08 - MATHEMATIQUES/PHYSIQUE-CHIMIE/SCIENCES ECONOMIQUES ET SOCIALES' : 8,
    '09 - LANGUES, LITT. ET CULTURES ETRA. ET R./MATHEMATIQUES/SCIENCES ECONOMIQUES ET SOCIALES' : 9,
    '10 - MATHEMATIQUES/SCIENCES ECONOMIQUES ET SOCIALES/SCIENCES DE LA VIE ET DE LA TERRE' : 10,
    '11 - HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/SCIENCES ECONOMIQUES ET SOCIALES/SCIENCES DE LA VIE ET DE LA TERRE' : 11,
    '12 - HUMANITES, LITTERATURE ET PHILOSOPHIE/LANGUES, LITT. ET CULTURES ETRA. ET R./SCIENCES ECONOMIQUES ET SOCIALES' : 12,
    '13 - LANGUES, LITT. ET CULTURES ETRA. ET R./MATHEMATIQUES/PHYSIQUE-CHIMIE' : 13,
    '14 - HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/MATHEMATIQUES/PHYSIQUE-CHIMIE' : 14,
    '15 - LANGUES, LITT. ET CULTURES ETRA. ET R./SCIENCES ECONOMIQUES ET SOCIALES/SCIENCES DE LA VIE ET DE LA TERRE' : 15,
    '16 - LANGUES, LITT. ET CULTURES ETRA. ET R./MATHEMATIQUES/SCIENCES DE LA VIE ET DE LA TERRE' : 16,
    '17 - HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/MATHEMATIQUES/SCIENCES DE LA VIE ET DE LA TERRE' : 17,
    '18 - HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/LANGUES, LITT. ET CULTURES ETRA. ET R./MATHEMATIQUES' : 18,
    'AUTRES COMBINAISONS' : 19
}

# +
#tracer de l'histogramme de l'année 2021

plt.bar(df_2021bis.columns[1:], frequences_2021[1:])
plt.xlabel('Triplette')
plt.ylabel('Fréquence')
plt.title('Fréquence de la triplette choisie en 2021')
plt.xticks(df_2021bis.columns[1:], [labels[x] for x in df_2021bis.columns[1:]])
plt.show()


#tracer de l'histogramme de l'année 2022

plt.bar(df_2022bis.columns[1:], frequences_2022[1:])
plt.xlabel('Triplette')
plt.ylabel('Fréquence')
plt.title('Fréquence de la triplette choisie en 2022')
plt.xticks(df_2022bis.columns[1:], [labels[x] for x in df_2022bis.columns[1:]])
plt.show()

#tracer de l'histogramme de l'année 2023

plt.bar(df_2023bis.columns[1:], frequences_2023[1:])
plt.xlabel('Triplette')
plt.ylabel('Fréquence')
plt.title('Fréquence de la triplette choisie en 2023')
plt.xticks(df_2023bis.columns[1:], [labels[x] for x in df_2023bis.columns[1:]])
plt.show()

print('1 : MATHEMATIQUES/PHYSIQUE-CHIMIE/SCIENCES DE LA VIE ET DE LA TERRE',
    '2 : HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/LANGUES, LITT. ET CULTURES ETRA. ET R./SCIENCES ECONOMIQUES ET SOCIALES',
    '3 : HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/MATHEMATIQUES/SCIENCES ECONOMIQUES ET SOCIALES',
    '4 : HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/HUMANITES, LITTERATURE ET PHILOSOPHIE/SCIENCES ECONOMIQUES ET SOCIALES',
    '5 : MATHEMATIQUES/NUMERIQUE ET SCIENCES INFORMATIQUES/PHYSIQUE-CHIMIE',
    '6 : HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/HUMANITES, LITTERATURE ET PHILOSOPHIE/LANGUES, LITT. ET CULTURES ETRA. ET R.',
    '7 : MATHEMATIQUES/PHYSIQUE-CHIMIE/SCIENCES DE L INGENIEUR',
    '8 : MATHEMATIQUES/PHYSIQUE-CHIMIE/SCIENCES ECONOMIQUES ET SOCIALES',
    '9 : LANGUES, LITT. ET CULTURES ETRA. ET R./MATHEMATIQUES/SCIENCES ECONOMIQUES ET SOCIALES',
    '10 : MATHEMATIQUES/SCIENCES ECONOMIQUES ET SOCIALES/SCIENCES DE LA VIE ET DE LA TERRE',
    '11 : HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/SCIENCES ECONOMIQUES ET SOCIALES/SCIENCES DE LA VIE ET DE LA TERRE',
    '12 : HUMANITES, LITTERATURE ET PHILOSOPHIE/LANGUES, LITT. ET CULTURES ETRA. ET R./SCIENCES ECONOMIQUES ET SOCIALES',
    '13 : LANGUES, LITT. ET CULTURES ETRA. ET R./MATHEMATIQUES/PHYSIQUE-CHIMIE',
    '14 : HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/MATHEMATIQUES/PHYSIQUE-CHIMIE',
    '15 : LANGUES, LITT. ET CULTURES ETRA. ET R./SCIENCES ECONOMIQUES ET SOCIALES/SCIENCES DE LA VIE ET DE LA TERRE',
    '16 : LANGUES, LITT. ET CULTURES ETRA. ET R./MATHEMATIQUES/SCIENCES DE LA VIE ET DE LA TERRE',
    '17 : HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/MATHEMATIQUES/SCIENCES DE LA VIE ET DE LA TERRE',
    '18 : HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/LANGUES, LITT. ET CULTURES ETRA. ET R./MATHEMATIQUES',
    '19 : AUTRES COMBINAISONS',
      sep = '\n')

# +
#tracer du camembert pour 2021

plt.pie(frequences_2021[1:], labels = [labels[x] for x in df_2021bis.columns[1:]], startangle = 40)
plt.title("Répartition du choix des triplettes pour l'année 2021")
plt.show()

#tracer du camembert pour 2022

plt.pie(frequences_2022[1:], labels = [labels[x] for x in df_2022bis.columns[1:]], startangle = 40)
plt.title("Répartition du choix des triplettes pour l'année 2022")
plt.show()

#tracer du camembert pour 2023

plt.pie(frequences_2023[1:], labels = [labels[x] for x in df_2023bis.columns[1:]], startangle = 40)
plt.title("Répartition du choix des triplettes pour l'année 2023")
plt.show()

print('1 : MATHEMATIQUES/PHYSIQUE-CHIMIE/SCIENCES DE LA VIE ET DE LA TERRE',
    '2 : HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/LANGUES, LITT. ET CULTURES ETRA. ET R./SCIENCES ECONOMIQUES ET SOCIALES',
    '3 : HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/MATHEMATIQUES/SCIENCES ECONOMIQUES ET SOCIALES',
    '4 : HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/HUMANITES, LITTERATURE ET PHILOSOPHIE/SCIENCES ECONOMIQUES ET SOCIALES',
    '5 : MATHEMATIQUES/NUMERIQUE ET SCIENCES INFORMATIQUES/PHYSIQUE-CHIMIE',
    '6 : HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/HUMANITES, LITTERATURE ET PHILOSOPHIE/LANGUES, LITT. ET CULTURES ETRA. ET R.',
    '7 : MATHEMATIQUES/PHYSIQUE-CHIMIE/SCIENCES DE L INGENIEUR',
    '8 : MATHEMATIQUES/PHYSIQUE-CHIMIE/SCIENCES ECONOMIQUES ET SOCIALES',
    '9 : LANGUES, LITT. ET CULTURES ETRA. ET R./MATHEMATIQUES/SCIENCES ECONOMIQUES ET SOCIALES',
    '10 : MATHEMATIQUES/SCIENCES ECONOMIQUES ET SOCIALES/SCIENCES DE LA VIE ET DE LA TERRE',
    '11 : HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/SCIENCES ECONOMIQUES ET SOCIALES/SCIENCES DE LA VIE ET DE LA TERRE',
    '12 : HUMANITES, LITTERATURE ET PHILOSOPHIE/LANGUES, LITT. ET CULTURES ETRA. ET R./SCIENCES ECONOMIQUES ET SOCIALES',
    '13 : LANGUES, LITT. ET CULTURES ETRA. ET R./MATHEMATIQUES/PHYSIQUE-CHIMIE',
    '14 : HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/MATHEMATIQUES/PHYSIQUE-CHIMIE',
    '15 : LANGUES, LITT. ET CULTURES ETRA. ET R./SCIENCES ECONOMIQUES ET SOCIALES/SCIENCES DE LA VIE ET DE LA TERRE',
    '16 : LANGUES, LITT. ET CULTURES ETRA. ET R./MATHEMATIQUES/SCIENCES DE LA VIE ET DE LA TERRE',
    '17 : HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/MATHEMATIQUES/SCIENCES DE LA VIE ET DE LA TERRE',
    '18 : HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/LANGUES, LITT. ET CULTURES ETRA. ET R./MATHEMATIQUES',
    '19 : AUTRES COMBINAISONS',
      sep = '\n')
# -

#créer des masques

# Après avoir étudié pour l'année 2021, on va faire les mêmes diagrammes pour l'année 2022 et l'année 2023 pour essayer d'observer des changements en 3 ans de nouvelle réforme du baccalauréat.


# +
#année 2022

df_2022 = df[df['RENTREE SCOLAIRE'] == 2022]
df_2022 = df_2022.loc[:,'EFFECTIF TOTAL':]

df_2022.sum(axis = 0).to_frame().T

df_2022bis = df_2022.iloc[:,:1].copy()

i = 3
while i < 40 : 
    nom = df_2022.columns[i].replace(" - filles", "")
    df_2022bis[nom] = df_2022[[df_2022.columns[i], df_2022.columns[i+1]]].sum(axis = 1)
    i += 2
#df_2022bis

df_2022bis = df_2022bis.drop(['EFFECTIF TOTAL'], axis = 1)

serie = df_2022bis.sum(axis = 0)
#print(serie)
valeurs = serie.tolist()
print(valeurs)

# +
#année 2023

df_2023 = df[df['RENTREE SCOLAIRE'] == 2023]
df_2023 = df_2023.loc[:,'EFFECTIF TOTAL':]

df_2023.sum(axis = 0).to_frame().T

df_2023bis = df_2023.iloc[:,:1].copy()

i = 3
while i < 40 : 
    nom = df_2023.columns[i].replace(" - filles", "")
    df_2023bis[nom] = df_2023[[df_2023.columns[i], df_2023.columns[i+1]]].sum(axis = 1)
    i += 2
#df_2023bis

df_2023bis = df_2023bis.drop(['EFFECTIF TOTAL'], axis = 1)

serie = df_2023bis.sum(axis = 0)
#print(serie)
valeurs = serie.tolist()
print(valeurs)
# -


