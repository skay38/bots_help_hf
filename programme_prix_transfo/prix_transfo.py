# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 15:13:41 2019

@author: Durieu
"""

nom=["viande","poisson","pain","fruit","legume","fromage","miel","lait","oeuf","epice","tonneau","bouteille_vin","bouteille_cidre","bijoux","poterie","vetement","bougie","livre","parfum","fourrure","teinture","potion","plante","cire","encre","perle","armure","arme","tunique","arc","arme_de_siege","navire_de_guerre","bois","bois_precieux","peau","cuir","pierre","gemme","argile","fer","corde","fleur","foin","ble","farine","orge","lin","chanvre","chevre","vache","poule","chevaux","bateau","navire_de_fret","charrette","zeppelin"]
noms_transfo=["poisson","pain","fromage","lait","oeuf","epice","tonneau","bouteille_vin","bouteille_cidre","bijoux","poterie","vetement","bougie","livre","parfum","fourrure","teinture","potion","encre","armure","arme","tunique","arc","arme_de_siege","navire_de_guerre","corde","farine","chevre","vache","poule","chevaux","bateau","navire_de_fret","charrette","zeppelin"]

mat_prod = []
mat_prod2 = []

for i in range(0,56):
    mat_prod.append([])
    mat_prod2.append([])
    for j in range(0,56):
        mat_prod[i].append(0)
    for k in range(0,24):
        mat_prod2[i].append(False)

def cherche(char):
    for i in range(0,len(nom)):
        if nom[i] == char:
            return(i)
    return(len(nom)+1)

mat_prod[1][cherche("bateau")] = 0.01
mat_prod[2][cherche("farine")] = 1
mat_prod[cherche("fromage")][cherche("chevre")] = 0.01
mat_prod[cherche("lait")][cherche("vache")] = 0.01
mat_prod[cherche("oeuf")][cherche("poule")] = 0.02
mat_prod[cherche("epice")][cherche("navire_de_fret")] = 0.005
mat_prod[cherche("tonneau")][cherche("orge")] = 5
mat_prod[cherche("bouteille_vin")][cherche("fruit")] = 10
mat_prod[cherche("bouteille_cidre")][cherche("fruit")] = 10
mat_prod[cherche("bijoux")][cherche("gemme")] = 5
mat_prod[cherche("bijoux")][cherche("bois_precieux")] = 5
mat_prod[cherche("poterie")][cherche("argile")] = 10
mat_prod[cherche("vetement")][cherche("lin")] = 5
mat_prod[cherche("vetement")][cherche("teinture")] = 1
mat_prod[cherche("bougie")][cherche("cire")] = 3
mat_prod[cherche("livre")][cherche("cuir")] = 5
mat_prod[cherche("livre")][cherche("encre")] = 1
mat_prod[cherche("parfum")][cherche("fleur")] = 10
mat_prod[cherche("fourrure")][cherche("peau")] = 5
mat_prod[cherche("teinture")][cherche("fleur")] = 5
mat_prod[cherche("potion")][cherche("plante")] = 5
mat_prod[cherche("encre")][cherche("perle")] = 5
mat_prod[cherche("armure")][cherche("fer")] = 30
mat_prod[cherche("arme")][cherche("fer")] = 20
mat_prod[cherche("tunique")][cherche("cuir")] = 10
mat_prod[cherche("arc")][cherche("bois")] = 10
mat_prod[cherche("arme_de_siege")][cherche("bois")] = 100
mat_prod[cherche("arme_de_siege")][cherche("corde")] = 100
mat_prod[cherche("arme_de_siege")][cherche("fer")] = 100
mat_prod[cherche("arme_de_siege")][cherche("pierre")] = 100
mat_prod[cherche("navire_de_guerre")][cherche("bois")] = 600
mat_prod[cherche("navire_de_guerre")][cherche("corde")] = 100
mat_prod[cherche("navire_de_guerre")][cherche("fer")] = 200
mat_prod[cherche("navire_de_guerre")][cherche("cuir")] = 200
mat_prod[cherche("corde")][cherche("chanvre")] = 1
mat_prod[cherche("farine")][cherche("ble")] = 1
mat_prod[cherche("chevre")][cherche("foin")] = 200
mat_prod[cherche("vache")][cherche("foin")] = 200
mat_prod[cherche("poule")][cherche("legume")] = 50
mat_prod[cherche("chevaux")][cherche("foin")] = 300
mat_prod[cherche("bateau")][cherche("bois")] = 100
mat_prod[cherche("bateau")][cherche("corde")] = 100
mat_prod[cherche("navire_de_fret")][cherche("bois")] = 300
mat_prod[cherche("navire_de_fret")][cherche("corde")] = 100
mat_prod[cherche("navire_de_fret")][cherche("fer")] = 100
mat_prod[cherche("navire_de_fret")][cherche("cuir")] = 200
mat_prod[cherche("charrette")][cherche("bois")] = 50
mat_prod[cherche("charrette")][cherche("corde")] = 10
mat_prod[cherche("charrette")][cherche("fer")] = 50
mat_prod[cherche("charrette")][cherche("chevaux")] = 1
mat_prod[cherche("zeppelin")][cherche("bois")] = 100
mat_prod[cherche("zeppelin")][cherche("corde")] = 400
mat_prod[cherche("zeppelin")][cherche("fer")] = 100
mat_prod[cherche("zeppelin")][cherche("cuir")] = 600

def quoi(ressource):
    liste=mat_prod[cherche(ressource)]
    liste_i=[]
    for i in range(0,56):
        if liste[i] != 0:
            liste_i.append(nom[i])
    return(liste_i)
    
coef=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0.2,1,1,1,1,0.33,0.5,1,0.5,0.2,0.2,0.2,0.2,0.01,0.01,1,0.5,0.5,1,0.5,0.2,1,1,1,1,1,1,1,0.5,0.5,1,0.1,0.1,0.2,0.1,0.05,0.01,0.05,0.01]
coef[33]=0.33
coef[cherche("bateau")]=0.02

list_gain=[]
prix_base=[10,40,30,10,10,30,10,30,20,50,120,120,120,430,120,180,70,190,120,120,60,160,30,20,120,20,320,220,120,120,6500,12500,10,30,20,10,20,50,10,10,20,10,10,10,20,20,20,10,2200,2200,550,3200,3300,8500,4700,16500]
pourcent=[]

def prix(fichier):
    fich=open(fichier,'r')
    for k in fich.read().split('\n'):
        pourcent.append(int(k.split(' ')[1])/100)

def tri_bulle_double(l):
    i=0
    while(i<len(l)-1):
        a1,b1,c1,d1=l[i]
        a2,b2,c2,d2=l[i+1]
        if d1<d2:
            h=l[i]
            l[i]=l[i+1]
            l[i+1]=h
            i=0
        else:
            i+=1
    return(l)

def liste_gain(fichier,nbr_partisans):
    prix(fichier)
    for k in noms_transfo:
        tot_f=0
        tot_p=(prix_base[cherche(k)]+prix_base[cherche(k)]*pourcent[cherche(k)])
        list_ressources=quoi(k)
        for l in list_ressources:
            tot_f+=(prix_base[cherche(l)]+prix_base[cherche(l)]*pourcent[cherche(l)])*mat_prod[cherche(k)][cherche(l)]
        list_gain.append((k,(tot_p-tot_f-tot_p*0.01)*nbr_partisans*coef[cherche(k)],tot_f*nbr_partisans*coef[cherche(k)],100*(tot_p-tot_f-tot_p*0.01)*nbr_partisans*coef[cherche(k)]/(tot_f*nbr_partisans*coef[cherche(k)])))

def best_vente(fichier,nbr_partisans):
    liste_gain(fichier,nbr_partisans)
    l=tri_bulle_double(list_gain)
    print("Pour "+str(nbr_partisans)+" partisans :")
    for k in l :
        a,b,c,d=k
        print(a+" : "+str(b)+" PO, investis :"+str(c)+" soit "+str(d)+"% de gain")
