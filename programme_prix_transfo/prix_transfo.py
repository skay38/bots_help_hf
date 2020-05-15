# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 15:13:41 2019

@author: Durieu
"""

import get_prices

nom_min=["viande","poisson","pain","fruit","legume","fromage","miel","lait","oeuf","epice","tonneau","bouteille_vin","bouteille_cidre","bijoux","poterie","vetement","bougie","livre","parfum","fourrure","teinture","potion","plante","cire","encre","perle","armure","arme","tunique","arc","arme_de_siege","navire_de_guerre","bois","bois_precieux","peau","cuir","pierre","gemme","argile","fer","corde","fleur","foin","ble","farine","orge","lin","chanvre","chevre","vache","poule","chevaux","bateau","navire_de_fret","charrette","zeppelin"]
noms_transfo=["Poisson","Pain","Fromage","Lait","Oeuf","Epice","Tonneau de bière","Bouteille de vin","Bouteille de cidre","Bijoux","Poterie","Vêtement","Bougie","Livre","Parfum","Fourrure","Teinture","Potion de soin","Encre","Armure","Arme","Tunique","Arc","Arme de siège","Navire de guerre","Corde","Farine","Chèvre","Vache","Poule","Chevaux","Bateau de pêche","Navire de fret","Charrette","Zeppelin"]

nom = ['Viande',
 'Poisson',
 'Pain',
 'Fruit',
 'Légume',
 'Fromage',
 'Miel',
 'Lait',
 'Oeuf',
 'Epice',
 'Tonneau de bière',
 'Bouteille de vin',
 'Bouteille de cidre',
 'Bijoux',
 'Poterie',
 'Vêtement',
 'Bougie',
 'Livre',
 'Parfum',
 'Fourrure',
 'Teinture',
 'Potion de soin',
 'Plante médicinale',
 'Cire d’abeille',
 'Encre',
 'Perle noire',
 'Armure',
 'Arme',
 'Tunique',
 'Arc',
 'Arme de siège',
 'Navire de guerre',
 'Bois',
 'Bois précieux',
 'Peau de bête',
 'Cuir',
 'Pierre',
 'Gemme',
 'Argile',
 'Fer',
 'Corde',
 'Fleur',
 'Foin',
 'Blé',
 'Farine',
 'Orge',
 'Lin',
 'Chanvre',
 'Chèvre',
 'Vache',
 'Poule',
 'Chevaux',
 'Bateau de pêche',
 'Navire de fret',
 'Charrette',
 'Zeppelin']

dict_rendement = {
        1: 0.71,
        2: 0.71,
        3: 0.71,
        4: 0.71,
        5: 0.71,
        6: 0.71,
        7: 0.71,
        8: 0.81,
        9: 0.71,
        10: 0.71,
        11: 0.71,
        12: 0.81,
        13: 0.71,
        14: 0.91,
        15: 0.71,
        16: 0.71,
        17: 0.71,
        18: 0.71,
        19: 0.71,
        20: 0.71,
        21: 0.71,
        22: 0.71,
        23: 0.71,
        24: 0.71,
        }

dict_prix = get_prices.get_all_prices()

#dict_prix = {'Viande': 25,
# 'Poisson': 25,
# 'Pain': 25,
# 'Fruit': 25,
# 'Légume': 25,
# 'Fromage': 25,
# 'Miel': 25,
# 'Lait': 25,
# 'Oeuf': 25,
# 'Epice': 25,
# 'Tonneau de bière': 25,
# 'Bouteille de vin': 25,
# 'Bouteille de cidre': 25,
# 'Bijoux': 25,
# 'Poterie': 25,
# 'Vêtement': 25,
# 'Bougie': 25,
# 'Livre': 25,
# 'Parfum': 25,
# 'Fourrure': 25,
# 'Bois': 25,
# 'Bois précieux': 25,
# 'Peau de bête': 25,
# 'Cuir': 25,
# 'Pierre': 25,
# 'Gemme': 25,
# 'Argile': 25,
# 'Fer': 25,
# 'Corde': 25,
# 'Fleur': 25,
# 'Foin': 25,
# 'Blé': 25,
# 'Farine': 25,
# 'Orge': 25,
# 'Lin': 25,
# 'Chanvre': 25,
# 'Teinture': 25,
# 'Potion de soin': 25,
# 'Plante médicinale': 25,
# 'Cire d’abeille': 25,
# 'Encre': 25,
# 'Perle noire': 25,
# 'Armure': 25,
# 'Arme': 25,
# 'Tunique': 25,
# 'Arc': 25,
# 'Arme de siège': 25,
# 'Navire de guerre': 25,
# 'Chèvre': 25,
# 'Vache': 25,
# 'Poule': 25,
# 'Chevaux': 25,
# 'Bateau de pêche': 25,
# 'Navire de fret': 25,
# 'Charrette': 25,
# 'Zeppelin': 25}

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

mat_prod[1][cherche("Bateau de pêche")] = 0.01
mat_prod[2][cherche("Farine")] = 1
mat_prod[cherche("Fromage")][cherche("Chèvre")] = 0.01
mat_prod[cherche("Lait")][cherche("Vache")] = 0.01
mat_prod[cherche("Oeuf")][cherche("Poule")] = 0.02
mat_prod[cherche("Epice")][cherche("Navire de fret")] = 0.005
mat_prod[cherche("Tonneau de bière")][cherche("Orge")] = 5
mat_prod[cherche("Bouteille de vin")][cherche("Fruit")] = 10
mat_prod[cherche("Bouteille de cidre")][cherche("Fruit")] = 10
mat_prod[cherche("Bijoux")][cherche("Gemme")] = 5
mat_prod[cherche("Bijoux")][cherche("Bois précieux")] = 5
mat_prod[cherche("Poterie")][cherche("Argile")] = 10
mat_prod[cherche("Vêtement")][cherche("Lin")] = 5
mat_prod[cherche("Vêtement")][cherche("Teinture")] = 1
mat_prod[cherche("Bougie")][cherche("Cire d’abeille")] = 3
mat_prod[cherche("Livre")][cherche("Cuir")] = 5
mat_prod[cherche("Livre")][cherche("Encre")] = 1
mat_prod[cherche("Parfum")][cherche("Fleur")] = 10
mat_prod[cherche("Fourrure")][cherche("Peau de bête")] = 5
mat_prod[cherche("Teinture")][cherche("Fleur")] = 5
mat_prod[cherche("Potion de soin")][cherche("Plante médicinale")] = 5
mat_prod[cherche("Encre")][cherche("Perle noire")] = 5
mat_prod[cherche("Armure")][cherche("Fer")] = 30
mat_prod[cherche("Arme")][cherche("Fer")] = 20
mat_prod[cherche("Tunique")][cherche("Cuir")] = 10
mat_prod[cherche("Arc")][cherche("Bois")] = 10
mat_prod[cherche("Arme de siège")][cherche("Bois")] = 100
mat_prod[cherche("Arme de siège")][cherche("Corde")] = 100
mat_prod[cherche("Arme de siège")][cherche("Fer")] = 100
mat_prod[cherche("Arme de siège")][cherche("Pierre")] = 100
mat_prod[cherche("Navire de guerre")][cherche("Bois")] = 600
mat_prod[cherche("Navire de guerre")][cherche("Corde")] = 100
mat_prod[cherche("Navire de guerre")][cherche("Fer")] = 200
mat_prod[cherche("Navire de guerre")][cherche("Cuir")] = 200
mat_prod[cherche("Corde")][cherche("Chanvre")] = 1
mat_prod[cherche("Farine")][cherche("Blé")] = 1
mat_prod[cherche("Chèvre")][cherche("Foin")] = 200
mat_prod[cherche("Vache")][cherche("Foin")] = 200
mat_prod[cherche("Poule")][cherche("Légume")] = 50
mat_prod[cherche("Chevaux")][cherche("Foin")] = 300
mat_prod[cherche("Bateau de pêche")][cherche("Bois")] = 100
mat_prod[cherche("Bateau de pêche")][cherche("Corde")] = 100
mat_prod[cherche("Navire de fret")][cherche("Bois")] = 300
mat_prod[cherche("Navire de fret")][cherche("Corde")] = 100
mat_prod[cherche("Navire de fret")][cherche("Fer")] = 100
mat_prod[cherche("Navire de fret")][cherche("Cuir")] = 200
mat_prod[cherche("Charrette")][cherche("Bois")] = 50
mat_prod[cherche("Charrette")][cherche("Corde")] = 10
mat_prod[cherche("Charrette")][cherche("Fer")] = 50
mat_prod[cherche("Charrette")][cherche("Chevaux")] = 1
mat_prod[cherche("Zeppelin")][cherche("Bois")] = 100
mat_prod[cherche("Zeppelin")][cherche("Corde")] = 400
mat_prod[cherche("Zeppelin")][cherche("Fer")] = 100
mat_prod[cherche("Zeppelin")][cherche("Cuir")] = 600

mat_prod2[cherche("Viande")][22] = True
mat_prod2[cherche("Poisson")][19] = True
mat_prod2[cherche("Pain")][3] = True
mat_prod2[cherche("Fruit")][22] = True
mat_prod2[cherche("Légume")][10] = True
mat_prod2[cherche("Fromage")][0] = True
mat_prod2[cherche("Miel")][9] = True
def ajoute(char,l):
    for i in range(0,len(l)):
        mat_prod2[cherche(char)][l[i]-1] = True

ajoute("Lait",[7])
ajoute("Oeuf",[22])
ajoute("Epice",[12])
ajoute("Tonneau de bière",[3])
ajoute("Bouteille de vin",[21])
ajoute("Bouteille de cidre",[14])
ajoute("Bijoux",[19])
ajoute("Poterie",[18])
ajoute("Vêtement",[8])
ajoute("Bougie",[2])
ajoute("Livre",[5])
ajoute("Parfum",[12])
ajoute("Fourrure",[3])
ajoute("Teinture",[5])
ajoute("Potion de soin",[6])
ajoute("Plante médicinale",[16])
ajoute("Cire d’abeille",[10])
ajoute("Encre",[14])
ajoute("Perle noire",[20])
ajoute("Armure",[4,15,17])
ajoute("Arme",[3,15,17])
ajoute("Tunique",[6,19,21])
ajoute("Arc",[6,18,23])
ajoute("Arme de siège",[15])
ajoute("Navire de guerre",[20])
ajoute("Bois",[1, 24, 21])
ajoute("Bois précieux",[10])
ajoute("Peau de bête",[18])
ajoute("Cuir",[2, 24])
ajoute("Pierre",[7,13])
ajoute("Gemme",[13])
ajoute("Argile",[19])
ajoute("Fer",[9,13,14])
ajoute("Corde",[22])
ajoute("Fleur",[24])
ajoute("Foin",[9,11])
ajoute("Blé",[11])
ajoute("Farine",[8])
ajoute("Orge",[9])
ajoute("Lin",[22])
ajoute("Chanvre",[16])
ajoute("Chèvre",[7])
ajoute("Vache",[1])
ajoute("Poule",[16])
ajoute("Chevaux",[2,17])
ajoute("Bateau de pêche",[12])
ajoute("Navire de fret",[8])
ajoute("Charrette",[4])
ajoute("Zeppelin",[5])

def quoi(ressource):
    liste=mat_prod[cherche(ressource)]
    liste_i=[]
    for i in range(0,56):
        if liste[i] != 0:
            liste_i.append(nom[i])
    return(liste_i)
    
coef=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0.2,1,1,1,1,0.33,0.5,1,0.5,0.2,0.2,0.2,0.2,0.01,0.01,1,0.5,0.5,1,0.5,0.2,1,1,1,1,1,1,1,0.5,0.5,1,0.1,0.1,0.2,0.1,0.05,0.01,0.05,0.01]
coef[33]=0.33
coef[cherche("Bateau de pêche")]=0.02
coef[cherche("Charrette")] = 0.015

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
        if b1<b2:
            h=l[i]
            l[i]=l[i+1]
            l[i+1]=h
            i=0
        else:
            i+=1
    return(l)

def liste_gain(nbr_partisans):
    for k in noms_transfo:
        tot_f=0
        tot_p=(prix_base[cherche(k)]+prix_base[cherche(k)]*dict_prix[k]/100)
        list_ressources=quoi(k)
        for l in list_ressources:
            tot_f+=(prix_base[cherche(l)]+prix_base[cherche(l)]*dict_prix[l]/100)*mat_prod[cherche(k)][cherche(l)]
        list_gain.append((k,(tot_p-tot_f-tot_p*0.02)*nbr_partisans*coef[cherche(k)],tot_f*nbr_partisans*coef[cherche(k)],100*(tot_p-tot_f-tot_p*0.01)*nbr_partisans*coef[cherche(k)]/(tot_f*nbr_partisans*coef[cherche(k)])))

def best_vente(nbr_partisans):
    liste_gain(nbr_partisans)
    l=tri_bulle_double(list_gain)
    print("Pour "+str(nbr_partisans)+" partisans :")
    for k in l :
        a,b,c,d=k
        print(a+" : "+str(round(b))+" PO, investis :"+str(round(c))+" soit "+str(round(d,2))+"% de gain")


def ressources_on_territory(i):
    liste_ressources = []
    for j, territoires in enumerate(mat_prod2):
        if territoires[i]:
            liste_ressources.append(nom[j])
    return liste_ressources

NOMBRE_PARTISANS = 42800

def liste_best_territoire(penurie):
    liste_territoire = []
    liste_gain(NOMBRE_PARTISANS)
    for k in range(24):
        gain_temp = 0
        po_investis_temp = 0
        liste_terr_temp = []
        liste_ressource = ressources_on_territory(k)
        for ressource in liste_ressource:
            if ressource not in penurie:
                if ressource in noms_transfo:
                    re, gain, investi, pourcent = list_gain[noms_transfo.index(ressource)]
                    if gain > 0:
                        investis = round(investi * dict_rendement[k + 1])
                        gain_temp += round(gain * dict_rendement[k + 1])
                        po_investis_temp += investis
                        liste_terr_temp.append((ressource, investis))
                else:
                    gain_temp += round((prix_base[cherche(ressource)] * (1 + dict_prix[ressource]/100 - 0.02)) * NOMBRE_PARTISANS * coef[cherche(ressource)] * dict_rendement[k + 1])
                    liste_terr_temp.append((ressource, 0))
        liste_territoire.append((k, gain_temp, po_investis_temp, liste_terr_temp, gain_temp + po_investis_temp))
    return liste_territoire

def best_territoire(penurie):
    liste_territoire = liste_best_territoire(penurie)
    i = 0
    while i < len(liste_territoire) - 1:
        if liste_territoire[i + 1][1] > liste_territoire[i][1]:
            temp = liste_territoire[i + 1]
            liste_territoire[i + 1] = liste_territoire[i]
            liste_territoire[i] = temp
            i = 0
        else:
            i += 1
    return liste_territoire

def render_best_territoire(penurie):
    best_territoires = best_territoire(penurie)
    for (territoire, gain, investis, ressources, total) in best_territoires:
        print('territoire {0} : gain de {2} pour un investissement de {1}. (total : {4} po)\n'
              'Ressources produites : {3}\n'.format(territoire + 1, investis, gain, ressources, total))

render_best_territoire(["Argile", "Bois", "Perle noire"])