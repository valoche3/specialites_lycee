# # ÉTUDE DU CHOIX DES TRIPLETTES PAR LES ÉLÈVES DE PREMIÈRE EN FRANCE EN 2021, 2022 et 2023

# Dans ce notebook, on étudie grâce aux données gouvernementales la répartition du choix des triplettes par les élèves de première en France sur les rentrées 2021, 2022 et 2023. Nous allons d'abord déterminer les fréquences de choix de chacune des triplettes pour ces trois années, puis la proportion de filles et de garçons dans chacune de ces triplettes en moyenne sur les trois années.

# Le but de cette étude est d'alors de mettre en lumière des différences sociétales quant aux choix de triplettes plus scientifiques, plus littéraires ou plus économiques, ainsi que la discrimination genrée pour chacune des triplettes.

# ## Étude des triplettes les plus choisies

# Nous allons tout d'abord créer de nouveaux dataframes afin de cibler les informations dont nous avons besoin pour répondre à la question des triplettes les plus choisies en 2021, 2022 et 2023.

# +
#import des librairies utiles

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# +
#charger le dataset

df = pd.read_csv("fr-en-effectifs-specialites-triplettes-1ere-generale.csv", delimiter=';')  # Ajustez le délimiteur si nécessaire

#afficher les premières lignes et les informations générales

display(df.head())
df.describe()

# +
#convertir les colonnes de type objet en type numérique si nécessaire

df['EFFECTIF TOTAL'] = pd.to_numeric(df['EFFECTIF TOTAL'], errors='coerce')
# -

# Pour rendre notre dataframe plus lisible, notre premier but est de supprimer toutes les colonnes dont nous n'allons pas avoir besoin pour notre étude (colonne correspondant qu'à une spécialité et non à une triplette).

# +
#enlever les colonnes correspondant qu'à une spécialité

i = 17 
L = [] #liste contenant les indices des colonnes à supprimer
while i <= 54 : 
    L.append(i)
    i+=1

df = df.drop(df.columns[L], axis = 1)
df = df.drop(columns = ['1087 - EDUC.PHYSIQUE PRATIQUE & CULT.SPORTIVE - filles',
       '1087 - EDUC.PHYSIQUE PRATIQUE & CULT.SPORTIVE - garçons'], axis = 1)

#vérification

df.head(5)
# -
# Nous allons ensuite procéder à l'étude des fréquences de choix de chaque triplette pour les années 2021, 2022 et 2023.

# ### 2021

# +
#créer un dataframe rentrée 2021

df_2021 = df[df['RENTREE SCOLAIRE'] == 2021]


# +
#garder que les colonnes utiles (effectifs)

df_2021 = df_2021.loc[:,'EFFECTIF TOTAL':]

# +
#somme sur tous les lycées de la rentrée 2021

df_2021 = df_2021.sum(axis = 0).to_frame().T
# -

# On crée ensuite un nouveau dataframe qui somme les effectifs filles et garçons pour chaque spécialité. En effet, dans cette première partie d'étude, on ne s'intéresse pas à la répartition selon le genre (mais seulement sur l'effectif total).

# +
#créer un nouveau dataframe

df_2021bis = df_2021.iloc[:,:1].copy() #garder que la colonne EFFECTIF TOTAL

#calcul des sommes et remplissage du nouveau dataframe

i = 3
while i < 40 : 
    nom = df_2021.columns[i].replace(" - filles", "") #nouveaux noms des colonnes
    df_2021bis[nom] = df_2021[[df_2021.columns[i], df_2021.columns[i+1]]].sum(axis = 1)
    i += 2
    
#vérification

df_2021bis
# -

# La dernière étape consiste à calculer la proportion d'élèves dans chaque triplette par rapport à l'effectif total.

# +
#calcul des fréquences

serie_2021 = df_2021bis.sum(axis = 0)
valeurs_2021 = serie_2021.tolist()
frequences_2021 = [x/valeurs_2021[0] for x in valeurs_2021]
# -

# Après avoir étudié l'année 2021, on va faire les mêmes opérations pour l'année 2022 et l'année 2023 afin d'observer les changements sur 3 ans de la nouvelle réforme du baccalauréat.

# ### 2022

# +
df_2022 = df[df['RENTREE SCOLAIRE'] == 2022] #créer un dataframe rentrée 2022
df_2022 = df_2022.loc[:,'EFFECTIF TOTAL':]

df_2022.sum(axis = 0).to_frame().T

df_2022bis = df_2022.iloc[:,:1].copy() #créer un nouveau dataframe

i = 3
while i < 40 : 
    nom = df_2022.columns[i].replace(" - filles", "")
    df_2022bis[nom] = df_2022[[df_2022.columns[i], df_2022.columns[i+1]]].sum(axis = 1)
    i += 2

serie_2022 = df_2022bis.sum(axis = 0)
valeurs_2022 = serie_2022.tolist()
frequences_2022 = [x/valeurs_2022[0] for x in valeurs_2022]
# -

# ### 2023

# +
df_2023 = df[df['RENTREE SCOLAIRE'] == 2023] #créer un dataframe rentrée 2023
df_2023 = df_2023.loc[:,'EFFECTIF TOTAL':]

df_2023.sum(axis = 0).to_frame().T

df_2023bis = df_2023.iloc[:,:1].copy() #créer un nouveau dataframe

i = 3
while i < 40 : 
    nom = df_2023.columns[i].replace(" - filles", "")
    df_2023bis[nom] = df_2023[[df_2023.columns[i], df_2023.columns[i+1]]].sum(axis = 1)
    i += 2

serie_2023 = df_2023bis.sum(axis = 0)
valeurs_2023 = serie_2023.tolist()
frequences_2023 = [x/valeurs_2023[0] for x in valeurs_2023]
# -

# ### Affichage des résultats

# Maintenant que nous avons étudié les triplettes les plus choisies pour les 3 années, on va pouvoir afficher les histogrammes et les camemberts pour chacune de ces années.

# +
#définition des labels

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

plt.bar(df_2021bis.columns[1:], frequences_2021[1:]) #on enlève la première valeur correspondant à EFFECTIF TOTAL
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

#afficher la légende

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
#tracer du camembert pour l'année 2021

plt.pie(frequences_2021[1:], labels = [labels[x] for x in df_2021bis.columns[1:]], startangle = 40)
plt.title("Répartition du choix des triplettes pour l'année 2021")
plt.show()

#tracer du camembert pour l'année 2022

plt.pie(frequences_2022[1:], labels = [labels[x] for x in df_2022bis.columns[1:]], startangle = 40)
plt.title("Répartition du choix des triplettes pour l'année 2022")
plt.show()

#tracer du camembert pour l'année 2023

plt.pie(frequences_2023[1:], labels = [labels[x] for x in df_2023bis.columns[1:]], startangle = 40)
plt.title("Répartition du choix des triplettes pour l'année 2023")
plt.show()

#afficher la légende

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

# A travers ces graphiques, nous pouvons nous rendre compte que la spécialité Maths/Physique/SVT est largement la spécialité la plus choisie sur ces trois années. En deuxième et troisième places, nous retrouvons les spécialités Histoire-Géo/Langues/SES et Histoire-Géo/Maths/SES (sur les trois années). Finalement, ces résultats nous montrent que les 3 spécialités les plus choisies sur les trois années 2021, 2022 et 2023 ressemblent fortement aux anciennes filières S, ES et L. Nous pouvons alors questionner l'utilité de la réforme du nouveau BAC quant à la possibilité de la diversité 

# ## Triplettes les plus choisies par genre

# ### Triplettes les plus choisies pour les filles

# +
df_filles = df.copy()
df_filles = df_filles.loc[:,'EFFECTIF TOTAL':]

i = -1
L = []
for name in df_filles.columns:
    i+=1
    if 'garçons' in name:
        L.append(i)

# +
#on enlève les colonnes qui ne nous intéressent pas

df_filles = df_filles.drop(df_filles.columns[L], axis = 1)
df_filles = df_filles.drop(['EFFECTIF TOTAL GARCONS', 'EFFECTIF TOTAL'], axis = 1)
# -

display(df_filles.sum(axis = 0).to_frame().T)

# +
#on calcule les fréquences pour les filles

serie_filles = df_filles.sum(axis = 0)
print(serie_filles)
valeurs_filles = serie_filles.tolist()
frequences_filles = [x/valeurs_filles[0] for x in valeurs_filles]
print(frequences_filles)

# +
df_fillesbis = df_filles.iloc[:,:1].copy()

#i = 1
#while i < 20 : 
    #nom = df_filles.columns[i].replace(" - filles", "")
    #df_fillesbis.columns[nom] = df_filles[i].iloc[:,i]
    #i += 1

df_fillesbis
# -

# ### Triplettes les plus choisies pour les garçons

# +
df_garcons = df.copy()
df_garcons = df_garcons.loc[:,'EFFECTIF TOTAL':]

i = -1
L = []
for name in df_garcons.columns:
    i+=1
    if 'filles' in name:
        L.append(i)

# +
#on enlève les colonnes qui ne nous intéressent pas

df_garcons = df_garcons.drop(df_garcons.columns[L], axis = 1)
df_garcons = df_garcons.drop(['EFFECTIF TOTAL FILLES', 'EFFECTIF TOTAL'], axis = 1)

# +
#on calcule les fréquences pour les garçons

serie_garcons = df_garcons.sum(axis = 0)
valeurs_garcons = serie_garcons.tolist()
print(valeurs_garcons)
frequences_garcons = [x/valeurs_garcons[0] for x in valeurs_garcons]
print(frequences_garcons)
# -

# ### Affichage des résultats et comparaison

# +
#définition des labels filles et garçons pour mieux voir
labels_filles = ['01 - MATHEMATIQUES/PHYSIQUE-CHIMIE/SCIENCES DE LA VIE ET DE LA TERRE - filles',
    '02 - HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/LANGUES, LITT. ET CULTURES ETRA. ET R./SCIENCES ECONOMIQUES ET SOCIALES - filles',
    '03 - HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/MATHEMATIQUES/SCIENCES ECONOMIQUES ET SOCIALES - filles',
    '04 - HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/HUMANITES, LITTERATURE ET PHILOSOPHIE/SCIENCES ECONOMIQUES ET SOCIALES - filles',
    '05 - MATHEMATIQUES/NUMERIQUE ET SCIENCES INFORMATIQUES/PHYSIQUE-CHIMIE - filles',
    '06 - HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/HUMANITES, LITTERATURE ET PHILOSOPHIE/LANGUES, LITT. ET CULTURES ETRA. ET R. - filles',
    '07 - MATHEMATIQUES/PHYSIQUE-CHIMIE/SCIENCES DE L INGENIEUR - filles',
    '08 - MATHEMATIQUES/PHYSIQUE-CHIMIE/SCIENCES ECONOMIQUES ET SOCIALES - filles',
    '09 - LANGUES, LITT. ET CULTURES ETRA. ET R./MATHEMATIQUES/SCIENCES ECONOMIQUES ET SOCIALES - filles',
    '10 - MATHEMATIQUES/SCIENCES ECONOMIQUES ET SOCIALES/SCIENCES DE LA VIE ET DE LA TERRE - filles',
    '11 - HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/SCIENCES ECONOMIQUES ET SOCIALES/SCIENCES DE LA VIE ET DE LA TERRE - filles',
    '12 - HUMANITES, LITTERATURE ET PHILOSOPHIE/LANGUES, LITT. ET CULTURES ETRA. ET R./SCIENCES ECONOMIQUES ET SOCIALES - filles',
    '13 - LANGUES, LITT. ET CULTURES ETRA. ET R./MATHEMATIQUES/PHYSIQUE-CHIMIE - filles',
    '14 - HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/MATHEMATIQUES/PHYSIQUE-CHIMIE - filles',
    '15 - LANGUES, LITT. ET CULTURES ETRA. ET R./SCIENCES ECONOMIQUES ET SOCIALES/SCIENCES DE LA VIE ET DE LA TERRE - filles',
    '16 - LANGUES, LITT. ET CULTURES ETRA. ET R./MATHEMATIQUES/SCIENCES DE LA VIE ET DE LA TERRE - filles',
    '17 - HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/MATHEMATIQUES/SCIENCES DE LA VIE ET DE LA TERRE - filles',
    '18 - HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/LANGUES, LITT. ET CULTURES ETRA. ET R./MATHEMATIQUES - filles',
    'AUTRES COMBINAISONS - filles']

labels_garcons = ['01 - MATHEMATIQUES/PHYSIQUE-CHIMIE/SCIENCES DE LA VIE ET DE LA TERRE - garçons',
    '02 - HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/LANGUES, LITT. ET CULTURES ETRA. ET R./SCIENCES ECONOMIQUES ET SOCIALES - garçons',
    '03 - HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/MATHEMATIQUES/SCIENCES ECONOMIQUES ET SOCIALES - garçons',
    '04 - HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/HUMANITES, LITTERATURE ET PHILOSOPHIE/SCIENCES ECONOMIQUES ET SOCIALES - garçons',
    '05 - MATHEMATIQUES/NUMERIQUE ET SCIENCES INFORMATIQUES/PHYSIQUE-CHIMIE - garçons',
    '06 - HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/HUMANITES, LITTERATURE ET PHILOSOPHIE/LANGUES, LITT. ET CULTURES ETRA. ET R. - garçons',
    '07 - MATHEMATIQUES/PHYSIQUE-CHIMIE/SCIENCES DE L INGENIEUR - garçons',
    '08 - MATHEMATIQUES/PHYSIQUE-CHIMIE/SCIENCES ECONOMIQUES ET SOCIALES - garçons',
    '09 - LANGUES, LITT. ET CULTURES ETRA. ET R./MATHEMATIQUES/SCIENCES ECONOMIQUES ET SOCIALES - garçons',
    '10 - MATHEMATIQUES/SCIENCES ECONOMIQUES ET SOCIALES/SCIENCES DE LA VIE ET DE LA TERRE - garçons',
    '11 - HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/SCIENCES ECONOMIQUES ET SOCIALES/SCIENCES DE LA VIE ET DE LA TERRE - garçons',
    '12 - HUMANITES, LITTERATURE ET PHILOSOPHIE/LANGUES, LITT. ET CULTURES ETRA. ET R./SCIENCES ECONOMIQUES ET SOCIALES - garçons',
    '13 - LANGUES, LITT. ET CULTURES ETRA. ET R./MATHEMATIQUES/PHYSIQUE-CHIMIE - garçons',
    '14 - HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/MATHEMATIQUES/PHYSIQUE-CHIMIE - garçons',
    '15 - LANGUES, LITT. ET CULTURES ETRA. ET R./SCIENCES ECONOMIQUES ET SOCIALES/SCIENCES DE LA VIE ET DE LA TERRE - garçons',
    '16 - LANGUES, LITT. ET CULTURES ETRA. ET R./MATHEMATIQUES/SCIENCES DE LA VIE ET DE LA TERRE - garçons',
    '17 - HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/MATHEMATIQUES/SCIENCES DE LA VIE ET DE LA TERRE - garçons',
    '18 - HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/LANGUES, LITT. ET CULTURES ETRA. ET R./MATHEMATIQUES - garçons',
    'AUTRES COMBINAISONS - garçons']
# -

labels = ['01 - MATHEMATIQUES/PHYSIQUE-CHIMIE/SCIENCES DE LA VIE ET DE LA TERRE',
    '02 - HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/LANGUES, LITT. ET CULTURES ETRA. ET R./SCIENCES ECONOMIQUES ET SOCIALES',
    '03 - HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/MATHEMATIQUES/SCIENCES ECONOMIQUES ET SOCIALES',
    '04 - HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/HUMANITES, LITTERATURE ET PHILOSOPHIE/SCIENCES ECONOMIQUES ET SOCIALES',
    '05 - MATHEMATIQUES/NUMERIQUE ET SCIENCES INFORMATIQUES/PHYSIQUE-CHIMIE',
    '06 - HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/HUMANITES, LITTERATURE ET PHILOSOPHIE/LANGUES, LITT. ET CULTURES ETRA. ET R.',
    '07 - MATHEMATIQUES/PHYSIQUE-CHIMIE/SCIENCES DE L INGENIEUR',
    '08 - MATHEMATIQUES/PHYSIQUE-CHIMIE/SCIENCES ECONOMIQUES ET SOCIALES',
    '09 - LANGUES, LITT. ET CULTURES ETRA. ET R./MATHEMATIQUES/SCIENCES ECONOMIQUES ET SOCIALES',
    '10 - MATHEMATIQUES/SCIENCES ECONOMIQUES ET SOCIALES/SCIENCES DE LA VIE ET DE LA TERRE',
    '11 - HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/SCIENCES ECONOMIQUES ET SOCIALES/SCIENCES DE LA VIE ET DE LA TERRE',
    '12 - HUMANITES, LITTERATURE ET PHILOSOPHIE/LANGUES, LITT. ET CULTURES ETRA. ET R./SCIENCES ECONOMIQUES ET SOCIALES',
    '13 - LANGUES, LITT. ET CULTURES ETRA. ET R./MATHEMATIQUES/PHYSIQUE-CHIMIE',
    '14 - HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/MATHEMATIQUES/PHYSIQUE-CHIMIE',
    '15 - LANGUES, LITT. ET CULTURES ETRA. ET R./SCIENCES ECONOMIQUES ET SOCIALES/SCIENCES DE LA VIE ET DE LA TERRE',
    '16 - LANGUES, LITT. ET CULTURES ETRA. ET R./MATHEMATIQUES/SCIENCES DE LA VIE ET DE LA TERRE',
    '17 - HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/MATHEMATIQUES/SCIENCES DE LA VIE ET DE LA TERRE',
    '18 - HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES/LANGUES, LITT. ET CULTURES ETRA. ET R./MATHEMATIQUES',
    'AUTRES COMBINAISONS']

# +
# Données
categories = labels
data1 = frequences_filles[1:]  # Premier ensemble de données
data2 = frequences_garcons[1:]  # Deuxième ensemble de données

# Création du graphique à barres empilées
x = np.arange(1, len(categories)+1)  # Position des catégories

plt.bar(x, data1, label='Filles', color='blue')  # Barres pour le premier ensemble
plt.bar(x, data2, label='Garçons', color='green', bottom=data1)  # Empilage du deuxième ensemble

# Ajout des titres, étiquettes et légendes
plt.title('Fréquence des triplettes choisies de 2021 à 2023 pour les filles (bleu) et les garçons (vert)')
plt.xlabel('Triplette')
plt.ylabel('Fréquence')
plt.xticks(x)
plt.legend()  # Affiche la légende

# Affichage
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

for i in range(19):
    plt.pie([frequences_filles[i+1]/(frequences_filles[i+1]+frequences_garcons[i+1]), frequences_garcons[i+1]/(frequences_filles[i+1]+frequences_garcons[i+1])], labels = [labels_filles[i], labels_garcons[i]], startangle = 40)
    plt.title(f"Répartition du choix de la triplette {labels[i]} par genre sur les trois années 2021, 2022 et 2023")
    plt.show()
    print('----------------------------------------------------------------------------------------------------------------------------','\n','\n', sep = '\n')
