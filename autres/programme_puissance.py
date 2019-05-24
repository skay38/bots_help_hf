# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 12:58:43 2019

@author: Durieu
"""
import copy

NOMS=["Archer","Soldat","Eclaireur","AS","Dragon","Grognard","Assassin","Nomade","Gorzagh","Cavalier Pourpre","Necromancien","MM","Vampire","Demon Ancien","Elfe","GDN","Haut Chevalier","Magicien","Troll","Esprit des eaux","Nymphe"]
TACTIQUES=['b','r','j','b','b','r','b','b','r','j','r','j','b','j','j','j','r','b','r','r','j']
PUISSANCES=[10,20,80,100,10000,10,400,50,100,200,300,1000,1500,3000,50,100,200,300,1000,1500,3000]
tab_nbr=[]
for k in NOMS:
    tab_nbr.append(int(input("Combien de "+k+" ?")))
alignement=int(input("Quel alignement ? (0:marchand, 1:nomade,2:gorzagh...)"))


def cherche(char,nom):
    for i in range(0,len(nom)):
        if nom[i] == char:
            return(i)
    return(len(nom)+1)

if alignement!=0:
    if alignement<5:
        alignement+=6
        PUISSANCES[alignement]*=2
    else:
        alignement+=9
        PUISSANCES[alignement]*=2

puissance_globale=[]
for i in range(len(PUISSANCES)):
    puissance_globale.append(PUISSANCES[i]*tab_nbr[i])

def maxi2(tab):
    i1=0
    i2=0
    max1=tab[0]
    max2=0
    for i in range(1,len(tab)):
        if tab[i]>=max1:
            max2=max1
            i2=i1
            i1=i
            max1=tab[i]
        elif tab[i]>=max2:
            max2=tab[i]
            i2=i
    return(i1,i2)

i1,i2=maxi2(puissance_globale)

puissance_globale_max=copy.deepcopy(puissance_globale)
puissance_globale_min=copy.deepcopy(puissance_globale)

if i1==0:
    puissance_globale_max[i1]*=2
    if i2==0:
        puissance_globale_min[i2]*=2
    elif i2==5:
        puissance_globale_min[i2]*=2
elif i1==5:
    puissance_globale_max[i1]*=2
    if i2==0:
        puissance_globale_min[i2]*=2
    elif i2==5:
        puissance_globale_min[i2]*=2
elif i2==0:
    puissance_globale_min[i2]*=2
elif i2==5:
    puissance_globale_min[i2]*=2
def somme(tab):
    tot=0
    for k in tab:
        tot+=k
    return(tot)

for i in range(len(TACTIQUES)):
    if TACTIQUES[i]=='b':
        TACTIQUES[i]="Bleue"
    elif TACTIQUES[i]=='j':
        TACTIQUES[i]="Jaune"
    else:
        TACTIQUES[i]="Rouge"

puissance_tot_max=somme(puissance_globale_max)
puissance_tot_min=somme(puissance_globale_min)

print("puissance 1 : "+str(puissance_tot_max)+" avec une tactique "+TACTIQUES[i1]+'\n'+"puissance 2 : "+str(puissance_tot_min)+" avec une tactique "+TACTIQUES[i2])
