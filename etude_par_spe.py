# # ETUDE DU CHOIX DE SPECIALITES PAR LES ELEVES DE PREMIERE EN FRANCE EN 2021, 2022, 2023

# A travers cette analyse de données sur les choix de spécialités en première tirées du site data.gouv, nous allons mener une étude comparative afin de mettre en lumière des tendances, des caractéristiques sur ces choix des différentes spécialités
#
# On s'intéresse ici à la première partie du dataframe qui repertorie les effectifs par spécialité individuelle et non par triplette (cf deuxieme notebook pour l'étude du choix des triplettes) 
#
# Nous allons notamment nous pencher sur des comparaisons entre filles et garçons, mais aussi entre lycée public et privé et enfin en fonction du département étudié
#

import pandas as pd
import numpy as np
import geopandas as gpd
import seaborn as sns
import matplotlib.pyplot as plt

#chargement du dataset
df = pd.read_csv("fr-en-effectifs-specialites-triplettes-1ere-generale.csv", delimiter=';')

# Convertir les colonnes de type objet en type numérique si nécessaire:
df['EFFECTIF TOTAL'] = pd.to_numeric(df['EFFECTIF TOTAL'], errors='coerce')

# Statistiques de base
print(df.describe())


# +
#calcul de l'effectif total (mixte, fille, garcon) sur la france chaque année
#2021
print("\033[1mEffectifs 2021\033[0m")
df_2021 = df[df['RENTREE SCOLAIRE'] == 2021]
eff_tot_2021 = df_2021['EFFECTIF TOTAL'].sum()
print("l'effectif total en 2021 est de", eff_tot_2021, 'eleves')
eff_filles_2021 = df_2021['EFFECTIF TOTAL FILLES'].sum()
print("l'effectif total féminin en 2021 est de", eff_filles_2021, 'eleves')
eff_garcons_2021 = df_2021['EFFECTIF TOTAL GARCONS'].sum()
print("l'effectif total masculin en 2021 est de", eff_garcons_2021, 'eleves')
print('')

#2022
print("\033[1mEffectifs 2022\033[0m")
df_2022 = df[df['RENTREE SCOLAIRE'] == 2022]
eff_tot_2022 = df_2022['EFFECTIF TOTAL'].sum()
print("l'effectif total en 2022 est de", eff_tot_2022, 'eleves')
eff_filles_2022 = df_2022['EFFECTIF TOTAL FILLES'].sum()
print("l'effectif total féminin en 2022 est de", eff_filles_2022, 'eleves')
eff_garcons_2022 = df_2022['EFFECTIF TOTAL GARCONS'].sum()
print("l'effectif total masculin en 2022 est de", eff_garcons_2022, 'eleves')
print('')

#2023
print("\033[1mEffectifs 2023\033[0m")
df_2023 = df[df['RENTREE SCOLAIRE'] == 2023]
eff_tot_2023 = df_2023['EFFECTIF TOTAL'].sum()
print("l'effectif total en 2023 est de", eff_tot_2023, 'eleves')
eff_filles_2023 = df_2023['EFFECTIF TOTAL FILLES'].sum()
print("l'effectif total féminin en 2023 est de", eff_filles_2023, 'eleves')
eff_garcons_2023 = df_2023['EFFECTIF TOTAL GARCONS'].sum()
print("l'effectif total masculin en 2023 est de", eff_garcons_2023, 'eleves')
# -
# On constate ici que ces effectifs sont relativement constants sur ces trois dernières années

# ## Etude du choix des specialités par filière

# L'objectif ici est de répartir les différentes spécialités par filières (scientifique, littéraire, eco et sociale, art) et voir la répartitions des filles et des garcons dans ces filières

# +

#répartition des spes par filière
liste_spe_lit_filles = ['0105 - HUMANITES, LITTERATURE ET PHILOSOPHIE - filles', '0241 - LITTERATURE ET LCA LATIN - filles', '0242 - LITTERATURE ET LCA GREC - filles', '0300 - LANGUES, LITTERATURE ET CULTURES ETRANGERES ET REGIONALES - filles']
liste_spe_lit_garcons = ['0105 - HUMANITES, LITTERATURE ET PHILOSOPHIE - garçons', '0241 - LITTERATURE ET LCA LATIN - garçons', '0242 - LITTERATURE ET LCA GREC - garçons', '0300 - LANGUES, LITTERATURE ET CULTURES ETRANGERES ET REGIONALES - garçons']
liste_spe_eco_filles = ['0439 - HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES - filles', '0507 - SCIENCES ECONOMIQUES ET SOCIALES - filles']
liste_spe_eco_garcons = ['0439 - HIST.-GEO. GEOPOLITIQUE & SC.POLITIQUES - garçons', '0507 - SCIENCES ECONOMIQUES ET SOCIALES - garçons']
liste_spe_scient_filles = ['0613 - MATHEMATIQUES - filles', '0623 - PHYSIQUE-CHIMIE - filles', '0629 - SCIENCES DE LA VIE ET DE LA TERRE - filles', "0673 - SCIENCES DE L'INGENIEUR - filles", '0747 - NUMERIQUE ET SCIENCES INFORMATIQUES - filles', '3045 - BIOLOGIE-ECOLOGIE - filles']
liste_spe_scient_garcons = ['0613 - MATHEMATIQUES - garçons', '0623 - PHYSIQUE-CHIMIE - garçons', '0629 - SCIENCES DE LA VIE ET DE LA TERRE - garçons', "0673 - SCIENCES DE L'INGENIEUR - garçons", '0747 - NUMERIQUE ET SCIENCES INFORMATIQUES - garçons', '3045 - BIOLOGIE-ECOLOGIE - garçons']
liste_spe_art_filles = ['0825 - DANSE - filles', '0832 - MUSIQUE - filles', '2757 - HISTOIRE DES ARTS - filles', '2785 - THEATRE - filles', '2786 - ARTS DU CIRQUE - filles', '2852 - CINEMA-AUDIOVISUEL - filles']
liste_spe_art_garcons = ['0825 - DANSE - garçons', '0832 - MUSIQUE - garçons', '2757 - HISTOIRE DES ARTS - garçons', '2785 - THEATRE - garçons', '2786 - ARTS DU CIRQUE - garçons', '2852 - CINEMA-AUDIOVISUEL - garçons']

#2021
#filtrage des colonnes correspondant aux différentes filières 
df_lit_filles_21 = df_2021[liste_spe_lit_filles]
df_lit_garcons_21 = df_2021[liste_spe_lit_garcons]
df_eco_filles_21 = df_2021[liste_spe_eco_filles]
df_eco_garcons_21 = df_2021[liste_spe_eco_garcons]
df_scient_filles_21 = df_2021[liste_spe_scient_filles]
df_scient_garcons_21 = df_2021[liste_spe_scient_garcons]
df_art_filles_21 = df_2021[liste_spe_art_filles]
df_art_garcons_21 = df_2021[liste_spe_art_garcons]

#calcul des différents effectifs 
#effectif des filles en littéraire
df_tot_lit_f_21 = df_lit_filles_21.sum()
eff_lit_f_21 = df_tot_lit_f_21.sum()
#effectif des garcons en littéraire
df_tot_lit_g_21 = df_lit_garcons_21.sum()
eff_lit_g_21 = df_tot_lit_g_21.sum()
#effectif des filles en eco
df_tot_eco_f_21 = df_eco_filles_21.sum()
eff_eco_f_21 = df_tot_eco_f_21.sum()
#effectif des garcons en eco
df_tot_eco_g_21 = df_eco_garcons_21.sum()
eff_eco_g_21 = df_tot_eco_g_21.sum()
#effectif des filles en scientifique
df_tot_scient_f_21 = df_scient_filles_21.sum()
eff_scient_f_21 = df_tot_scient_f_21.sum()
#effectif des garcons en scientifique
df_tot_scient_g_21 = df_scient_garcons_21.sum()
eff_scient_g_21 = df_tot_scient_g_21.sum()
#effectif des filles en art
df_tot_art_f_21 = df_art_filles_21.sum()
eff_art_f_21 = df_tot_art_f_21.sum()
#effectif des garcons en art
df_tot_art_g_21 = df_art_garcons_21.sum()
eff_art_g_21 = df_tot_art_g_21.sum()

print('nb de filles ayant choisi une spé littéraire en 2021: ', eff_lit_f_21)
print('nb de garçons ayant choisi une spé littéraire en 2021: ', eff_lit_g_21)
print('nb de filles ayant choisi une spé socio économique en 2021: ', eff_eco_f_21)
print('nb de garçons ayant choisi une spé socio économique en 2021: ', eff_eco_g_21)
print('nb de filles ayant choisi une spé scinetifique en 2021: ',eff_scient_f_21)
print('nb de garçons ayant choisi une spé scientifique en 2021: ',eff_scient_g_21)
print('nb de filles ayant choisi une spé artistique en 2021: ',eff_art_f_21)
print('nb de garçons ayant choisi une artistique en 2021: ',eff_art_g_21)

#2022
#filtrage des colonnes correspondant aux différentes filières 
df_lit_filles_22 = df_2022[liste_spe_lit_filles]
df_lit_garcons_22 = df_2022[liste_spe_lit_garcons]
df_eco_filles_22 = df_2022[liste_spe_eco_filles]
df_eco_garcons_22 = df_2022[liste_spe_eco_garcons]
df_scient_filles_22 = df_2022[liste_spe_scient_filles]
df_scient_garcons_22 = df_2022[liste_spe_scient_garcons]
df_art_filles_22 = df_2022[liste_spe_art_filles]
df_art_garcons_22 = df_2022[liste_spe_art_garcons]

#calcul des différents effectifs 
#effectif des filles en littéraire
df_tot_lit_f_22 = df_lit_filles_22.sum()
eff_lit_f_22 = df_tot_lit_f_22.sum()
#effectif des garcons en littéraire
df_tot_lit_g_22 = df_lit_garcons_22.sum()
eff_lit_g_22 = df_tot_lit_g_22.sum()
#effectif des filles en eco
df_tot_eco_f_22 = df_eco_filles_22.sum()
eff_eco_f_22 = df_tot_eco_f_22.sum()
#effectif des garcons en eco
df_tot_eco_g_22 = df_eco_garcons_22.sum()
eff_eco_g_22 = df_tot_eco_g_22.sum()
#effectif des filles en scientifique
df_tot_scient_f_22 = df_scient_filles_22.sum()
eff_scient_f_22 = df_tot_scient_f_22.sum()
#effetif des garcons en scientifique
df_tot_scient_g_22 = df_scient_garcons_22.sum()
eff_scient_g_22 = df_tot_scient_g_22.sum()
#effectif des filles en art
df_tot_art_f_22 = df_art_filles_22.sum()
eff_art_f_22 = df_tot_art_f_22.sum()
#effectif des garcons en art
df_tot_art_g_22 = df_art_garcons_22.sum()
eff_art_g_22 = df_tot_art_g_22.sum()

#2023
#filtrage des colonnes correspondant aux différentes filières 
df_lit_filles_23 = df_2023[liste_spe_lit_filles]
df_lit_garcons_23 = df_2023[liste_spe_lit_garcons]
df_eco_filles_23 = df_2023[liste_spe_eco_filles]
df_eco_garcons_23 = df_2023[liste_spe_eco_garcons]
df_scient_filles_23 = df_2023[liste_spe_scient_filles]
df_scient_garcons_23 = df_2023[liste_spe_scient_garcons]
df_art_filles_23 = df_2023[liste_spe_art_filles]
df_art_garcons_23 = df_2023[liste_spe_art_garcons]

#calcul des différents effectifs 
#effectif des filles en littéraire
df_tot_lit_f_23 = df_lit_filles_23.sum()
eff_lit_f_23 = df_tot_lit_f_23.sum()
#effectif des garcons en littéraire
df_tot_lit_g_23 = df_lit_garcons_23.sum()
eff_lit_g_23 = df_tot_lit_g_23.sum()
#effectif des filles en eco
df_tot_eco_f_23 = df_eco_filles_23.sum()
eff_eco_f_23 = df_tot_eco_f_23.sum()
#effectif des garcons en eco
df_tot_eco_g_23 = df_eco_garcons_23.sum()
eff_eco_g_23 = df_tot_eco_g_23.sum()
#effectif des filles en scientifique
df_tot_scient_f_23 = df_scient_filles_23.sum()
eff_scient_f_23 = df_tot_scient_f_23.sum()
#effetif des garcons en scientifique
df_tot_scient_g_23 = df_scient_garcons_23.sum()
eff_scient_g_23 = df_tot_scient_g_23.sum()
#effectif des filles en art
df_tot_art_f_23 = df_art_filles_23.sum()
eff_art_f_23 = df_tot_art_f_23.sum()
#effectif des garcons en art
df_tot_art_g_23 = df_art_garcons_23.sum()
eff_art_g_23 = df_tot_art_g_23.sum()
# -
# On va maintenant représenter ces résultats sous forme de diagramme pour plus de visibilité

# +
#affichage sous forme d'un diagramme baton le nombres de filles et de garçons ayant choisi des matières de filière différentes

categories = ['littéraire', 'eco', 'scientifique', 'art']

#2021
val_f_21 = [eff_lit_f_21, eff_eco_f_21, eff_scient_f_21, eff_art_f_21]
val_g_21 = [eff_lit_g_21, eff_eco_g_21, eff_scient_g_21, eff_art_g_21]

#afficher les deux diagrammes l'un à côté de l'autre
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.bar(categories, val_f_21, color='blue')
ax1.set_title('nbr de filles en fonction de la filière en 2021')
ax1.set_xlabel('Catégories')
ax1.set_ylabel('Valeurs')

ax2.bar(categories, val_g_21, color='green')
ax2.set_title('nbr de garcons en fonction de la filière en 2021')
ax2.set_xlabel('Catégories')
ax2.set_ylabel('Valeurs')

# Définir la même échelle en ordonnée pour les deux graphiques
y_min = 0
y_max = max(max(val_f_21), max(val_g_21)) + 20000
ax1.set_ylim(y_min, y_max)
ax2.set_ylim(y_min, y_max)

plt.tight_layout() 
plt.show()

#2022
val_f_22 = [eff_lit_f_22, eff_eco_f_22, eff_scient_f_22, eff_art_f_22]
val_g_22 = [eff_lit_g_22, eff_eco_g_22, eff_scient_g_22, eff_art_g_22]

#afficher les deux diagrammes l'un à côté de l'autre
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.bar(categories, val_f_22, color='blue')
ax1.set_title('nbr de filles en fonction de la filière en 2022')
ax1.set_xlabel('Catégories')
ax1.set_ylabel('Valeurs')

ax2.bar(categories, val_g_22, color='green')
ax2.set_title('nbr de garcons en fonction de la filière en 2022')
ax2.set_xlabel('Catégories')
ax2.set_ylabel('Valeurs')

# Définir la même échelle en ordonnée pour les deux graphiques
y_min = 0
y_max = max(max(val_f_22), max(val_g_22)) + 20000
ax1.set_ylim(y_min, y_max)
ax2.set_ylim(y_min, y_max)

plt.tight_layout() 
plt.show()

#2023
val_f_23 = [eff_lit_f_23, eff_eco_f_23, eff_scient_f_23, eff_art_f_23]
val_g_23 = [eff_lit_g_23, eff_eco_g_23, eff_scient_g_23, eff_art_g_23]

#afficher les deux diagrammes l'un à côté de l'autre
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.bar(categories, val_f_23, color='blue')
ax1.set_title('nbr de filles en fonction de la filière en 2023')
ax1.set_xlabel('Catégories')
ax1.set_ylabel('Valeurs')

ax2.bar(categories, val_g_23, color='green')
ax2.set_title('nbr de garcons en fonction de la filière en 2023')
ax2.set_xlabel('Catégories')
ax2.set_ylabel('Valeurs')

# Définir la même échelle en ordonnée pour les deux graphiques
y_min = 0
y_max = max(max(val_f_23), max(val_g_23)) + 20000
ax1.set_ylim(y_min, y_max)
ax2.set_ylim(y_min, y_max)

plt.tight_layout() 
plt.show()
# -
# On constate que le nombre de filles en littéraire et en éco est bien supérieur à celui des garçons, tandis que les garçons ont plus tendance à choisir des spécialités scientifiques

# +
#afficher un tableau à double entrée avec les années et les filières pour les filles et les garçons

#filles
data_f = {
    'année': ['2021', '2021', '2021', '2021','2022', '2022', '2022', '2022', '2023', '2023', '2023','2023'],
    'filières': ['littéraire', 'socio économique', 'scientifique', 'artistique', 'littéraire', 'socio économique', 'scientifique', 'artistique', 'littéraire', 'socio économique', 'scientifique', 'artistique'],
    'effectifs': [eff_lit_f_21, eff_eco_f_21, eff_scient_f_21, eff_art_f_21, eff_lit_f_22, eff_eco_f_22, eff_scient_f_22, eff_art_f_22, eff_lit_f_23, eff_eco_f_23, eff_scient_f_23, eff_art_f_23]
}
df_f = pd.DataFrame(data_f)

tableau_effectif_f = pd.pivot_table(df_f, values='effectifs', index='année', columns='filières', fill_value=0)
print("\033[1mEFFECITF DE FILLES AYANT CHOISI UNE DES SPECIALITES APPARTENANT AUX DIFFERENTES FILIERES PAR ANNEE\033[0m")
tableau_effectif_f

# +
#garcons
data_g = {
    'année': ['2021', '2021', '2021', '2021','2022', '2022', '2022', '2022', '2023', '2023', '2023','2023'],
    'filières': ['littéraire', 'socio économique', 'scientifique', 'artistique', 'littéraire', 'socio économique', 'scientifique', 'artistique', 'littéraire', 'socio économique', 'scientifique', 'artistique'],
    'effectifs': [eff_lit_g_21, eff_eco_g_21, eff_scient_g_21, eff_art_g_21, eff_lit_g_22, eff_eco_g_22, eff_scient_g_22, eff_art_g_22, eff_lit_g_23, eff_eco_g_23, eff_scient_g_23, eff_art_g_23]
}
df_g = pd.DataFrame(data_g)

tableau_effectif_g = pd.pivot_table(df_g, values='effectifs', index='année', columns='filières', fill_value=0)
tableau_effectif_f = pd.pivot_table(df_f, values='effectifs', index='année', columns='filières', fill_value=0)
print("\033[1mEFFECITF DE GARCONS AYANT CHOISI UNE DES SPECIALITES APPARTENANT AUX DIFFERENTES FILIERES PAR ANNEE\033[0m")
tableau_effectif_g
# -
# ## Etude du choix des specialités en fonction du secteur (privé/public)

# +
#comparaison entre lycée privé et lycée public

#filtrage des lycées
df_prive = df[df['SECTEUR'] == 'PRIVE SOUS CONTRAT']
df_public = df[df['SECTEUR'] == 'PUBLIC']

#filtrage des années
df_prive_21 = df_prive[df_prive['RENTREE SCOLAIRE'] == 2021]
df_prive_22 = df_prive[df_prive['RENTREE SCOLAIRE'] == 2022]
df_prive_23 = df_prive[df_prive['RENTREE SCOLAIRE'] == 2023]
df_public_21 = df_public[df_public['RENTREE SCOLAIRE'] == 2021]
df_public_22 = df_public[df_public['RENTREE SCOLAIRE'] == 2022]
df_prive_23 = df_public[df_public['RENTREE SCOLAIRE'] == 2023]


#proportion d'élèves dans le privé
eff_tot_prive_21 = df_prive_21['EFFECTIF TOTAL'].sum()
eff_tot_prive_22 = df_prive_22['EFFECTIF TOTAL'].sum()
eff_tot_prive_23 = df_prive_23['EFFECTIF TOTAL'].sum()
prop_prive_21 =  round(eff_tot_prive_21/eff_tot_2021, 2)
prop_prive_22 = round(eff_tot_prive_22/eff_tot_2022, 2)
prop_prive_23 =  round(eff_tot_prive_23/eff_tot_2023, 2)
print("La propotion d'élèves dans le privé en 2021 est de", prop_prive_21)
print("La propotion d'élèves dans le privé en 2022 est de", prop_prive_22)
print("La propotion d'élèves dans le privé en 2023 est de", prop_prive_23)
# -


# La proportion d'élèves dans le privé en 2023 ne semble pas très cohérente avec les deux autres valeurs, il se peut qu'il y ait des valeurs aberrantes dans le dataframe 

# +
#tracé de l'évolution de la proportion d'élèves dans le privé
# Définir les coordonnées des points
x = [2021, 2022, 2023]
y = [prop_prive_21, prop_prive_22, prop_prive_23]
y_min = 0
y_max = 1

# Tracer le graphique
plt.plot(x, y, '-o', label="Proportion")
plt.xlabel("Année")
plt.xticks([2021, 2022, 2023])
plt.ylabel("Proportion")
plt.title("Evolution de la proportion d'élèves dans le privé")
plt.ylim(y_min, y_max) 
plt.legend()
plt.show()

# +
#tracés de l'évolution des proportions de filles et de garçons dans le privé

eff_f_prive_21 = df_prive_21['EFFECTIF TOTAL FILLES'].sum()
eff_g_prive_21 = df_prive_21['EFFECTIF TOTAL GARCONS'].sum()
eff_f_prive_22 = df_prive_22['EFFECTIF TOTAL FILLES'].sum()
eff_g_prive_22 = df_prive_22['EFFECTIF TOTAL GARCONS'].sum()
eff_f_prive_23 = df_prive_23['EFFECTIF TOTAL FILLES'].sum()
eff_g_prive_23 = df_prive_23['EFFECTIF TOTAL GARCONS'].sum()

prop_f_prive_21 = round(eff_f_prive_21/eff_tot_prive_21, 2)
prop_g_prive_21 = round(eff_g_prive_21/eff_tot_prive_21, 2)
prop_f_prive_22 = round(eff_f_prive_22/eff_tot_prive_22, 2)
prop_g_prive_22 = round(eff_g_prive_22/eff_tot_prive_22, 2)
prop_f_prive_23 = round(eff_f_prive_23/eff_tot_prive_23, 2)
prop_g_prive_23 = round(eff_g_prive_21/eff_tot_prive_23, 2)

# Définir les coordonnées des points pour les deux graphiques
x = [2021, 2022, 2023]
y1 = [prop_f_prive_21, prop_f_prive_22, prop_f_prive_23]
y2 = [prop_g_prive_21, prop_g_prive_22, prop_g_prive_23]

# Créer une figure et une grille de sous-graphiques 1x2
plt.figure(figsize=(10, 4))
y_min = 0
y_max = 1

# Premier graphique
plt.subplot(1, 2, 1)  # 1 ligne, 2 colonnes, 1er graphique
plt.plot(x, y1, '-o', label="proportion filles")
plt.xlabel("Année")
plt.ylabel("Proportion")
plt.title("Evolution de la proportion de filles dans le privé")
plt.xticks([2021, 2022, 2023])
plt.ylim(y_min, y_max) 
plt.legend()

# Deuxième graphique
plt.subplot(1, 2, 2)  # 1 ligne, 2 colonnes, 2e graphique
plt.plot(x, y2, '-o', label="proportion garçons", color="orange")
plt.xlabel("Année")
plt.ylabel("Proportion")
plt.title("Evolution de la proportion de garçons dans le privé")
plt.xticks([2021, 2022, 2023])
plt.ylim(y_min, y_max) 
plt.legend()

# Afficher la figure
plt.tight_layout()
plt.show()
# -

# ## Etude du choix des specialités par département

# On va essayer ici de représenter la spécialité la plus choisie par les filles et les garçons par département sous forme d'une carte de France avec chaque département de la couleur de la spécialité la plus choisie

#création d'une liste avec tous les numéros de départements présents dans le dataframe
liste_dep = df['code département'].unique().tolist()

# ### EN 2021

# On commence par créer un dictionnaire avec comme clé le numéro du département et comme valeur la spécialité la plus choisie

# +
#on selectionne les colonnes concernant les filles et les garçons
spe_cols_f = df.iloc[:, 17::2]
spe_cols_g = df.iloc[:, 18::2]

#on transforme le nom des colonnes en liste
liste_spe_f = spe_cols_f.columns.tolist()
liste_spe_g = spe_cols_g.columns.tolist()

# on crée un dictionnaire pour stocker la spécialité la plus populaire par département
spe_populaire_par_departement_f_2021 = {}
spe_populaire_par_departement_g_2021 = {}

# Parcourir les départements de la liste
for dep in liste_dep:
    # Filtrer le DataFrame pour le département actuel
    df_2021_dep = df_2021[df_2021['code département'] == dep]
    eff_max_f = 0
    spe_max_f = None
    eff_max_g = 0
    spe_max_g = None
    # Calculer la somme des effectifs pour chaque spécialité
    for spe in liste_spe_f:
        eff = df_2021_dep[spe].sum()
        if eff > eff_max_f:
            eff_max_f = eff
            spe_max_f = spe

    for spe in liste_spe_g:
        eff = df_2021_dep[spe].sum()
        if eff > eff_max_g:
            eff_max_g = eff
            spe_max_g = spe
    # Stocker le résultat dans le dictionnaire
    spe_populaire_par_departement_f_2021[dep] = spe_max_f
    spe_populaire_par_departement_g_2021[dep] = spe_max_g

# Afficher les spécialités populaires pour chaque département
spe_populaire_par_departement_f_2021
# -

# On utilise ensuite une carte geojson et on associe les clés et le numéro de département pour colorer la carte

# ### 2021 : AFFICHAGE POUR LES FILLES

# +
# Charger les données géographiques des départements français
url = "https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/departements.geojson"
departments = gpd.read_file(url)
departments['code'] = departments['code'].apply(lambda x: x.zfill(3))

# Ajouter une colonne 'specialty' au GeoDataFrame en fonction du dictionnaire
departments['specialty'] = departments['code'].map(spe_populaire_par_departement_f_2021)

# Traiter les départements sans spécialité : leur attribuer "Inconnu" ou une couleur par défaut
departments['specialty'] = departments['specialty'].fillna('Inconnu')

# Associer une couleur unique à chaque spécialité
unique_specialties = departments['specialty'].unique()
# Utiliser une palette qualitative de Seaborn
palette = sns.color_palette("Set2", n_colors=len(unique_specialties))  # Palette douce et distincte
color_map = {specialty: color for specialty, color in zip(unique_specialties, palette)}

# Ajouter une couleur par défaut pour "Inconnu"
color_map['Inconnu'] = 'lightgrey'

# Ajouter une colonne de couleurs
departments['color'] = departments['specialty'].map(color_map)

# Tracer la carte
fig, ax = plt.subplots(1, 1, figsize=(15, 15))
departments.boundary.plot(ax=ax, linewidth=0.5, color='black')  # Tracer les bordures
departments.plot(ax=ax, color=departments['color'])  # Remplir les départements

# on ajoute une légende
for specialty, color in color_map.items():
    ax.plot([], [], color=color, label=specialty, marker='o', linestyle='')  # Ajouter une légende
ax.legend(title="Spécialité", loc="upper left", fontsize=9, title_fontsize=10, bbox_to_anchor=(1, 1))

# on ajoute un titre
plt.title("Spécialité la plus choisie parmi les filles par département en 2021", fontsize=16)
plt.show()
# -

# ### 2021 : AFFICHAGE POUR LES GARCONS

# +
# Charger les données géographiques des départements français
url = "https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/departements.geojson"
departments = gpd.read_file(url)
departments['code'] = departments['code'].apply(lambda x: x.zfill(3))

# Ajouter une colonne 'specialty' au GeoDataFrame en fonction du dictionnaire
departments['specialty'] = departments['code'].map(spe_populaire_par_departement_g_2021)

# Traiter les départements sans spécialité : leur attribuer "Inconnu" ou une couleur par défaut
departments['specialty'] = departments['specialty'].fillna('Inconnu')

# Associer une couleur unique à chaque spécialité
unique_specialties = departments['specialty'].unique()
# Utiliser une palette qualitative de Seaborn
palette = sns.color_palette("Set2", n_colors=len(unique_specialties))  # Palette douce et distincte
color_map = {specialty: color for specialty, color in zip(unique_specialties, palette)}

# Ajouter une couleur par défaut pour "Inconnu"
color_map['Inconnu'] = 'lightgrey'

# Ajouter une colonne de couleurs
departments['color'] = departments['specialty'].map(color_map)

# Tracer la carte
fig, ax = plt.subplots(1, 1, figsize=(15, 15))
departments.boundary.plot(ax=ax, linewidth=0.5, color='black')  # Tracer les bordures
departments.plot(ax=ax, color=departments['color'])  # Remplir les départements

# Ajouter une légende
for specialty, color in color_map.items():
    ax.plot([], [], color=color, label=specialty, marker='o', linestyle='')  # Ajouter une légende
ax.legend(title="Spécialité", loc="upper left", fontsize=9, title_fontsize=10, bbox_to_anchor=(1, 1))

# Ajouter un titre
plt.title("Spécialité la plus choisie parmi les garçons par département en 2021", fontsize=16)
plt.show()
# -
# ### EN 2022

# +
# on crée un dictionnaire pour stocker la spécialité la plus populaire par département
spe_populaire_par_departement_f_2022 = {}
spe_populaire_par_departement_g_2022 = {}

# Parcourir les départements de la liste
for dep in liste_dep:
    # Filtrer le DataFrame pour le département actuel
    df_2022_dep = df_2022[df_2022['code département'] == dep]
    eff_max_f = 0
    spe_max_f = None
    eff_max_g = 0
    spe_max_g = None
    # Calculer la somme des effectifs pour chaque spécialité
    for spe in liste_spe_f:
        eff = df_2022_dep[spe].sum()
        if eff > eff_max_f:
            eff_max_f = eff
            spe_max_f = spe

    for spe in liste_spe_g:
        eff = df_2022_dep[spe].sum()
        if eff > eff_max_g:
            eff_max_g = eff
            spe_max_g = spe
    # Stocker le résultat dans le dictionnaire
    spe_populaire_par_departement_f_2022[dep] = spe_max_f
    spe_populaire_par_departement_g_2022[dep] = spe_max_g
# -


# ### 2022 : AFFICHAGE POUR LES FILLES

# +
# Charger les données géographiques des départements français
url = "https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/departements.geojson"
departments = gpd.read_file(url)
departments['code'] = departments['code'].apply(lambda x: x.zfill(3))

# Ajouter une colonne 'specialty' au GeoDataFrame en fonction du dictionnaire
departments['specialty'] = departments['code'].map(spe_populaire_par_departement_f_2022)

# Traiter les départements sans spécialité : leur attribuer "Inconnu" ou une couleur par défaut
departments['specialty'] = departments['specialty'].fillna('Inconnu')

# Associer une couleur unique à chaque spécialité
unique_specialties = departments['specialty'].unique()
# Utiliser une palette qualitative de Seaborn
palette = sns.color_palette("Set2", n_colors=len(unique_specialties))  # Palette douce et distincte
color_map = {specialty: color for specialty, color in zip(unique_specialties, palette)}

# Ajouter une couleur par défaut pour "Inconnu"
color_map['Inconnu'] = 'lightgrey'

# Ajouter une colonne de couleurs
departments['color'] = departments['specialty'].map(color_map)

# Tracer la carte
fig, ax = plt.subplots(1, 1, figsize=(15, 15))
departments.boundary.plot(ax=ax, linewidth=0.5, color='black')  # Tracer les bordures
departments.plot(ax=ax, color=departments['color'])  # Remplir les départements

# on ajoute une légende
for specialty, color in color_map.items():
    ax.plot([], [], color=color, label=specialty, marker='o', linestyle='')  # Ajouter une légende
ax.legend(title="Spécialité", loc="upper left", fontsize=9, title_fontsize=10, bbox_to_anchor=(1, 1))

# on ajoute un titre
plt.title("Spécialité la plus choisie parmi les filles par département en 2022", fontsize=16)
plt.show()
# -


# ### 2022 : AFFICHAGE POUR LES GARCONS

# +
# Charger les données géographiques des départements français
url = "https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/departements.geojson"
departments = gpd.read_file(url)
departments['code'] = departments['code'].apply(lambda x: x.zfill(3))

# Ajouter une colonne 'specialty' au GeoDataFrame en fonction du dictionnaire
departments['specialty'] = departments['code'].map(spe_populaire_par_departement_g_2022)

# Traiter les départements sans spécialité : leur attribuer "Inconnu" ou une couleur par défaut
departments['specialty'] = departments['specialty'].fillna('Inconnu')

# Associer une couleur unique à chaque spécialité
unique_specialties = departments['specialty'].unique()
# Utiliser une palette qualitative de Seaborn
palette = sns.color_palette("Set2", n_colors=len(unique_specialties))  # Palette douce et distincte
color_map = {specialty: color for specialty, color in zip(unique_specialties, palette)}

# Ajouter une couleur par défaut pour "Inconnu"
color_map['Inconnu'] = 'lightgrey'

# Ajouter une colonne de couleurs
departments['color'] = departments['specialty'].map(color_map)

# Tracer la carte
fig, ax = plt.subplots(1, 1, figsize=(15, 15))
departments.boundary.plot(ax=ax, linewidth=0.5, color='black')  # Tracer les bordures
departments.plot(ax=ax, color=departments['color'])  # Remplir les départements

# on ajoute une légende
for specialty, color in color_map.items():
    ax.plot([], [], color=color, label=specialty, marker='o', linestyle='')  # Ajouter une légende
ax.legend(title="Spécialité", loc="upper left", fontsize=9, title_fontsize=10, bbox_to_anchor=(1, 1))

# on ajoute un titre
plt.title("Spécialité la plus choisie parmi les garçons par département en 2022", fontsize=16)
plt.show()
# -

# ### EN 2023

# +
# on crée un dictionnaire pour stocker la spécialité la plus populaire par département
spe_populaire_par_departement_f_2023 = {}
spe_populaire_par_departement_g_2023 = {}

# Parcourir les départements de la liste
for dep in liste_dep:
    # Filtrer le DataFrame pour le département actuel
    df_2023_dep = df_2023[df_2023['code département'] == dep]
    eff_max_f = 0
    spe_max_f = None
    eff_max_g = 0
    spe_max_g = None
    # Calculer la somme des effectifs pour chaque spécialité
    for spe in liste_spe_f:
        eff = df_2023_dep[spe].sum()
        if eff > eff_max_f:
            eff_max_f = eff
            spe_max_f = spe

    for spe in liste_spe_g:
        eff = df_2023_dep[spe].sum()
        if eff > eff_max_g:
            eff_max_g = eff
            spe_max_g = spe
    # Stocker le résultat dans le dictionnaire
    spe_populaire_par_departement_f_2023[dep] = spe_max_f
    spe_populaire_par_departement_g_2023[dep] = spe_max_g
# -

# ### AFFFICHAGE POUR LES FILLES

# +
# Charger les données géographiques des départements français
url = "https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/departements.geojson"
departments = gpd.read_file(url)
departments['code'] = departments['code'].apply(lambda x: x.zfill(3))

# Ajouter une colonne 'specialty' au GeoDataFrame en fonction du dictionnaire
departments['specialty'] = departments['code'].map(spe_populaire_par_departement_f_2023)

# Traiter les départements sans spécialité : leur attribuer "Inconnu" ou une couleur par défaut
departments['specialty'] = departments['specialty'].fillna('Inconnu')

# Associer une couleur unique à chaque spécialité
unique_specialties = departments['specialty'].unique()
# Utiliser une palette qualitative de Seaborn
palette = sns.color_palette("Set2", n_colors=len(unique_specialties))  # Palette douce et distincte
color_map = {specialty: color for specialty, color in zip(unique_specialties, palette)}

# Ajouter une couleur par défaut pour "Inconnu"
color_map['Inconnu'] = 'lightgrey'

# Ajouter une colonne de couleurs
departments['color'] = departments['specialty'].map(color_map)

# Tracer la carte
fig, ax = plt.subplots(1, 1, figsize=(15, 15))
departments.boundary.plot(ax=ax, linewidth=0.5, color='black')  # Tracer les bordures
departments.plot(ax=ax, color=departments['color'])  # Remplir les départements

# on ajoute une légende
for specialty, color in color_map.items():
    ax.plot([], [], color=color, label=specialty, marker='o', linestyle='')  # Ajouter une légende
ax.legend(title="Spécialité", loc="upper left", fontsize=9, title_fontsize=10, bbox_to_anchor=(1, 1))

# on ajoute un titre
plt.title("Spécialité la plus choisie parmi les filles par département en 2023", fontsize=16)
plt.show()
# -

# ### AFFICHAGE POUR LES GARCONS

# +
# Charger les données géographiques des départements français
url = "https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/departements.geojson"
departments = gpd.read_file(url)
departments['code'] = departments['code'].apply(lambda x: x.zfill(3))

# Ajouter une colonne 'specialty' au GeoDataFrame en fonction du dictionnaire
departments['specialty'] = departments['code'].map(spe_populaire_par_departement_g_2023)

# Traiter les départements sans spécialité : leur attribuer "Inconnu" ou une couleur par défaut
departments['specialty'] = departments['specialty'].fillna('Inconnu')

# Associer une couleur unique à chaque spécialité
unique_specialties = departments['specialty'].unique()
# Utiliser une palette qualitative de Seaborn
palette = sns.color_palette("Set2", n_colors=len(unique_specialties))  # Palette douce et distincte
color_map = {specialty: color for specialty, color in zip(unique_specialties, palette)}

# Ajouter une couleur par défaut pour "Inconnu"
color_map['Inconnu'] = 'lightgrey'

# Ajouter une colonne de couleurs
departments['color'] = departments['specialty'].map(color_map)

# Tracer la carte
fig, ax = plt.subplots(1, 1, figsize=(15, 15))
departments.boundary.plot(ax=ax, linewidth=0.5, color='black')  # Tracer les bordures
departments.plot(ax=ax, color=departments['color'])  # Remplir les départements

# on ajoute une légende
for specialty, color in color_map.items():
    ax.plot([], [], color=color, label=specialty, marker='o', linestyle='')  # Ajouter une légende
ax.legend(title="Spécialité", loc="upper left", fontsize=9, title_fontsize=10, bbox_to_anchor=(1, 1))

# on ajoute un titre
plt.title("Spécialité la plus choisie parmi les garçons par département en 2023", fontsize=16)
plt.show()
# -

# On constate à travers ces cartes que chaque année les garçons choissisent en majorité la spécialité mathématiques, tandis que bien que la majorité des filles choissisent aussi cette spécilaité, c'est un peu plus varié puisque qu'elles sont nombreuses à choisir SES, SVT ou autre matière moins "science dure". 

# ### A travers cette étude, on constate que les spécialités scientifiques sont encore majoritairement choisies par les garçons tandis que plus de filles vont s'orienter vers des spécialités littéraires ou économiques. 
#
# ### Il semble donc important de promouvoir les spécialités scientifiques dans ces classes là pour les filles ainsi que les spécialités littéraires pour les garçons afin de rééquilibrer les effectifs dans chaque filière. 


