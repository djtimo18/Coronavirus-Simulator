# -*- coding: utf-8 -*-
"""

Ecrit par Tim
"""
from math import *


#MENU DU SIMULATEUR

print("Bienvenue dans le simulateur de pandémie du nom de Coronavirus :");
print("Choisissez des variables pour la simulations :");
C = input("Nombre de contact quotidien : ");
T = input("Durée de la maladie en jours : ");
T = int(T); #"Durée de la maladie
C = int(C); #Nombre de contact quotidien

#Valeur numérique
A = 70000000; #Nombre de personne
M = 2000; #Nombre de malade de base
Pt = 0.005; #Probabilité de transmission
Tm = 0.03; #Taux de mortalité
D = 0; #décés
G = 0 #Personne guérie
t = 0; #Debut de la pandémie
#Fonction :
d = (Tm/T)*M; #Nombre de décés par jours
D = D + d; #Nombre de décés total
g = M/T; #Nombre total de personne guérie
P = A-M-D-G; #Population sans maladie




#Algorythme de simulation :
for i in range(0, T):
    t = t + 1;
    M = M + M * C*Pt*(P/A)-d-g;
    d = (Tm/T)*M;
    D = D + d;
    g = M/T;
    P = A-M-D-G;
    print(f"Apres {round(t,2)} jours, le nombre de malade est de {round(M,0)} et le nombre de mort est de {round(D,0)} si le nombre de contact par jours est de {round(C,0)}")
    T = T + 1;
    
    
