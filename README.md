# Coronavirus-Simulator
A simple coronavirus simulator with variables.

#Données :
A =  #Nombre de personne
M =  #Nombre de malade de base
Pt =  #Probabilité de transmission
Tm =  #Taux de mortalité
D =  #décés
G = #Personne guérie
t = #Debut de la pandémie


#Fonction :

d = (Tm/T)*M; #Nombre de décés par jours
D = D + d; #Nombre de décés total
g = M/T; #Nombre total de personne guérie
P = A-M-D-G; #Population sans maladie
