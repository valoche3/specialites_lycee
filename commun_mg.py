import pandas as pd
import numpy as np
import geopandas as gpd
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
print("\033[1meffectifs 2021\033[0m")
df_2021 = df[df['RENTREE SCOLAIRE'] == 2021]
eff_tot_2021 = df_2021['EFFECTIF TOTAL'].sum()
print("l'effectif total en 2021 est de", eff_tot_2021, 'eleves')
eff_filles_2021 = df_2021['EFFECTIF TOTAL FILLES'].sum()
print("l'effectif total féminin en 2021 est de", eff_filles_2021, 'eleves')
eff_garcons_2021 = df_2021['EFFECTIF TOTAL GARCONS'].sum()
print("l'effectif total masculin en 2021 est de", eff_garcons_2021, 'eleves')
print('')

#2022
print("\033[1meffectifs 2022\033[0m")
df_2022 = df[df['RENTREE SCOLAIRE'] == 2022]
eff_tot_2022 = df_2022['EFFECTIF TOTAL'].sum()
print("l'effectif total en 2022 est de", eff_tot_2022, 'eleves')
eff_filles_2022 = df_2022['EFFECTIF TOTAL FILLES'].sum()
print("l'effectif total féminin en 2022 est de", eff_filles_2022, 'eleves')
eff_garcons_2022 = df_2022['EFFECTIF TOTAL GARCONS'].sum()
print("l'effectif total masculin en 2022 est de", eff_garcons_2022, 'eleves')
print('')

#2023
print("\033[1meffectifs 2023\033[0m")
df_2023 = df[df['RENTREE SCOLAIRE'] == 2023]
eff_tot_2023 = df_2023['EFFECTIF TOTAL'].sum()
print("l'effectif total en 2023 est de", eff_tot_2023, 'eleves')
eff_filles_2023 = df_2023['EFFECTIF TOTAL FILLES'].sum()
print("l'effectif total féminin en 2023 est de", eff_filles_2023, 'eleves')
eff_garcons_2023 = df_2023['EFFECTIF TOTAL GARCONS'].sum()
print("l'effectif total masculin en 2023 est de", eff_garcons_2023, 'eleves')
# +
#l'objectif ici est de répartir les différentes spécialités par filières (scientifique, littéraire, eco et sociale, art) et voir la répartitions des filles et des garcons dans ces filières

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


# +
#tracé de l'évolution de la proportion d'élèves dans le privé
# Définir les coordonnées des points
x = [2021, 2022, 2023]
y = [prop_prive_21, prop_prive_22, prop_prive_23]
y_min = 0
y_max = 1

# Tracer le graphique
plt.plot(x, y, '-o', label="Proportion")
plt.xlabel("Axe X")
plt.xticks([2021, 2022, 2023])
plt.ylabel("Axe Y")
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

# +
#ETUDE DES TRIPLETTES

#détermination de la triplette la plus choisie par département et affichage sur une carte de France
# liste des départements
liste_dep = df_2021['code département'].unique()
print(liste_dep)
# -

print(df.dtypes.head(10))

# Identifier les colonnes contenant les triplettes pour les filles et les garçons
triplette_cols_f = df.iloc[:, 55::2] 
triplette_cols_g = df.iloc[:, 56::2]
liste_triplette_f = triplette_cols_f.columns.tolist()
liste_triplette_g = triplette_cols_g.columns.tolist()
# +
# Créer un dictionnaire pour stocker la triplette la plus populaire par département
triplette_populaire_par_departement_f = {}
triplette_populaire_par_departement_g = {}

# Parcourir les départements de la liste
for dep in liste_dep:
    # Filtrer le DataFrame pour le département actuel
    df_2021_dep = df_2021[df_2021['code département'] == dep]
    eff_max_f = 0
    triplette_max_f = None
    eff_max_g = 0
    triplette_max_g = None
    # Calculer la somme des effectifs pour chaque triplette
    for triplette in liste_triplette_f:
        eff = df_2021_dep[triplette].sum()
        if eff > eff_max_f:
            eff_max_f = eff
            triplette_max_f = triplette

    for triplette in liste_triplette_g:
        eff = df_2021_dep[triplette].sum()
        if eff > eff_max_g:
            eff_max_g = eff
            triplette_max_g = triplette
    # Stocker le résultat dans le dictionnaire
    triplette_populaire_par_departement_f[dep] = triplette_max_f
    triplette_populaire_par_departement_g[dep] = triplette_max_g

# Afficher les triplette populaires pour chaque département
triplette_populaire_par_departement_g
# +
valeurs_df = pd.DataFrame(list(triplette_populaire_par_departement_f.items()), columns=['code_departement', 'triplette fav'])
departements = gpd.read_file('contour-des-departements.geojson')
# Fusionner les données géographiques avec les valeurs
departements = departements.merge(valeurs_df, left_on='code_insee', right_on='code_departement', how='left')

# Tracer la carte avec des couleurs en fonction des valeurs
fig, ax = plt.subplots(1, 1, figsize=(10, 10))
departements.plot(column='triplette', cmap='viridis', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)

# Afficher la carte
plt.title("Carte des départements colorée par valeur")
plt.show()
# -



