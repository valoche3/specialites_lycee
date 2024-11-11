# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
#
# #Charger le dataset
# df = pd.read_csv("fr-en-effectifs-specialites-triplettes-1ere-generale.csv", delimiter=';')  # Ajustez le délimiteur si nécessaire
#
# #Afficher les premières lignes et les informations générales
# print(df.head())
# print(df.info())
#
# #Vérifier les valeurs manquantes
# print(df.isnull().sum())


# +
# Remplacer les valeurs manquantes (exemple : remplacer par la moyenne ou la médiane)
df = df.fillna(df.mean())  # ou df.fillna(df.median()), selon le besoin

# Convertir les colonnes de type objet en type numérique si nécessaire
# Par exemple, si une colonne 'Effectifs' est en texte, on la convertit :
df['EFFECTIF TOTAL'] = pd.to_numeric(df['EFFECTIF TOTAL'], errors='coerce')

# -

# Statistiques de base
print(df.describe())


#calcul de l'effectif total (mixte, fille, garcon) sur la france chaque année
df_2021 = df[df['RENTREE SCOLAIRE'] == 2021]
eff_tot_2021 = df_2021['EFFECTIF TOTAL'].sum()
print("l'effectif total en 2021 est de", eff_tot_2021, 'eleves')
eff_filles_2021 = df_2021['EFFECTIF TOTAL FILLES'].sum()
print("l'effectif total féminin en 2021 est de", eff_filles_2021, 'eleves')
eff_garcons_2021 = df_2021['EFFECTIF TOTAL GARCONS'].sum()
print("l'effectif total masculin en 2021 est de", eff_garcons_2021, 'eleves')
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

#filtrage des colonnes correspondant aux différentes filières 
df_lit_filles = df_2021[liste_spe_lit_filles]
df_lit_garcons = df_2021[liste_spe_lit_garcons]
df_eco_filles = df_2021[liste_spe_eco_filles]
df_eco_garcons = df_2021[liste_spe_eco_garcons]
df_scient_filles = df_2021[liste_spe_scient_filles]
df_scient_garcons = df_2021[liste_spe_scient_garcons]
df_art_filles = df_2021[liste_spe_art_filles]
df_art_garcons = df_2021[liste_spe_art_garcons]

#calcul des différents effectifs 
df_tot_lit_f = df_lit_filles.sum()
eff_lit_f = df_tot_lit_f.sum()
print('nb de filles ayant choisi une spé littéraire : ', eff_lit_f)
df_tot_lit_g = df_lit_garcons.sum()
eff_lit_g = df_tot_lit_g.sum()
print('nb de garçons ayant choisi une spé littéraire : ', eff_lit_g)
df_tot_eco_f = df_eco_filles.sum()
eff_eco_f = df_tot_eco_f.sum()
print('nb de filles ayant choisi une spé socio économique : ', eff_eco_f)
df_tot_eco_g = df_eco_garcons.sum()
eff_eco_g = df_tot_eco_g.sum()
print('nb de filles ayant choisi une spé socio économique : 'eff_eco_g)
df_tot_scient_f = df_scient_filles.sum()
eff_scient_f = df_tot_scient_f.sum()
print(eff_scient_f)
df_tot_scient_g = df_scient_garcons.sum()
eff_scient_g = df_tot_scient_g.sum()
print(eff_scient_g)
df_tot_art_f = df_art_filles.sum()
eff_art_f = df_tot_art_f.sum()
print(eff_art_f)
df_tot_art_g = df_art_garcons.sum()
eff_art_g = df_tot_art_g.sum()
print(eff_art_g)

# +
categories = ['littéraire', 'eco', 'scientifique', 'art']
val_f = [eff_lit_f, eff_eco_f, eff_scient_f, eff_art_f]
val_g = [eff_lit_g, eff_eco_g, eff_scient_g, eff_art_g]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.bar(categories, val_f, color='blue')
ax1.set_title('nbr de filles en fonction de la filière')
ax1.set_xlabel('Catégories')
ax1.set_ylabel('Valeurs')

ax2.bar(categories, val_g, color='green')
ax2.set_title('nbr de garcons en fonction de la filière')
ax2.set_xlabel('Catégories')
ax2.set_ylabel('Valeurs')

# Définir la même échelle en ordonnée pour les deux graphiques
y_min = 0
y_max = max(max(val_f), max(val_g)) + 20000
ax1.set_ylim(y_min, y_max)
ax2.set_ylim(y_min, y_max)

plt.tight_layout() 
plt.show()

# -




