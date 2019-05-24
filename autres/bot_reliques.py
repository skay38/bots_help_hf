# -*- coding: utf-8 -*-
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from multiprocessing import Queue
import time

path_webdriver=os.getcwd()
os.environ["PATH"] += os.pathsep + path_webdriver
mult_achat=int(input("Combien de fois on achète le nbr de ressources ?"))
pseudo=input("Quel pseudo ?")
MDP=input("Quel mot de passe ?")
nb_offrandes=int(input("Combien d'offrandes par heure ?"))
NOMS_RESSOURCES=['Poisson', 'Pain', 'Fruit', 'Légume', 'Fromage', 'Miel', 'Lait', 'Oeuf', 'Epice', 'Foin', 'Blé', 'Farine', 'Orge', 'Lin', 'Chanvre', 'Chèvre', 'Vache', 'Poule', 'Chevaux', 'Vêtement', 'Fourrure', 'Plante médicinale', 'Cire d’abeille', 'Bateau de pêche', 'Navire de fret', 'Zeppelin', 'Bois', 'Bois précieux', 'Peau de bête', 'Cuir', 'Gemme', 'Argile', 'Fer', 'Fleur', 'Armure', 'Arme', 'Tunique', 'Arc', 'Arme de siège', 'Navire de guerre']
nb_serie_offrande=int(input("Combien de série d'offrandes ? (-1 pour infini)"))

def connexion(pseudo):
    driver = webdriver.Chrome()
    driver.get("http://www.heroic-fantasy.fr/")
    elem = driver.find_element_by_name("pseudo")
    elem.send_keys(Keys.BACK_SPACE)
    elem.send_keys(Keys.BACK_SPACE)
    elem.send_keys(Keys.BACK_SPACE)
    elem.send_keys(Keys.BACK_SPACE)
    elem.send_keys(Keys.BACK_SPACE)
    elem.send_keys(Keys.BACK_SPACE)
    elem.send_keys(pseudo)
    elem = driver.find_element_by_name("mdp")
    elem.send_keys(Keys.BACK_SPACE)
    elem.send_keys(Keys.BACK_SPACE)
    elem.send_keys(Keys.BACK_SPACE)
    elem.send_keys(Keys.BACK_SPACE)
    elem.send_keys(Keys.BACK_SPACE)
    elem.send_keys(Keys.BACK_SPACE)
    elem.send_keys(MDP)
    elem.send_keys(Keys.ENTER)
    return(driver)

def achats_ressources_offrandes(driver):
    elem=driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/div/div[2]/div/div/div[4]/div[2]/div/div/div[2]/div[2]/strong").text
    if int(elem.split(' / ')[0])<int(elem.split(' / ')[1]):
        nbr_achat=int(elem.split(' / ')[1])*mult_achat
        elem=driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/div/div[2]/div/div/div[4]/div[2]/div/a")
        driver.execute_script("return arguments[0].scrollIntoView();",elem)
        elem.click()
        driver.find_element_by_xpath("//*[@id='acheter1']").click()
        elem = driver.find_element_by_xpath("//*[@id='acheterQuantite']")
        k=20
        while k>0:
            elem.send_keys(Keys.BACK_SPACE)
            k-=1
        elem.send_keys(nbr_achat)
        elem.send_keys(Keys.ENTER)
    driver.find_element_by_xpath("/html/body/div[1]/div[1]").click()
    elem=driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/div/div[2]/div/div/div[4]/div[3]/div/div/div[2]/div[2]/strong").text
    if int(elem.split(' / ')[0])<int(elem.split(' / ')[1]):
        nbr_achat=int(elem.split(' / ')[1])*mult_achat
        elem=driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/div/div[2]/div/div/div[4]/div[3]/div/a")
        driver.execute_script("return arguments[0].scrollIntoView();",elem)
        elem.click()
        driver.find_element_by_xpath("//*[@id='acheter1']").click()
        elem = driver.find_element_by_xpath("//*[@id='acheterQuantite']")
        k=20
        while k>0:
            elem.send_keys(Keys.BACK_SPACE)
            k-=1
        elem.send_keys(nbr_achat)
        elem.send_keys(Keys.ENTER)
    driver.find_element_by_xpath("/html/body/div[1]/div[1]").click()

def id_ressource(ressource):
    for i in range(len(NOMS_RESSOURCES)):
        if NOMS_RESSOURCES[i]==ressource:
            return(i)
    return(-1)

def ajout(l_gain,gain):
    for k in l_gain:
        i=0
        while i<len(gain):
            if gain[i][0]==k[0]:
                gain[i][1]+=k[1]
                break
            i+=1
        if i==len(gain):
            gain.append([k[0],k[1]])

def enregistre(gains,pertes,tot):
    if tot==0:
        chaine="Gains :"
        for k in gains:
            chaine=chaine+" "+str(k[1])+" "+k[0]
        chaine=chaine+" --- Pertes :"
        for k in pertes:
            chaine=chaine+" "+str(k[1])+" "+k[0]
        chaine=chaine+'\n'
        fich=open("Enregistrement.txt",'a')
        fich.write(chaine)
        fich.close()
    else:
        chaine="Gains Totaux :"
        for k in gains:
            chaine=chaine+" "+str(k[1])+" "+k[0]
        chaine=chaine+" --- Pertes Totales :"
        for k in pertes:
            chaine=chaine+" "+str(k[1])+" "+k[0]
        chaine=chaine+'\n'
        fich=open("Enregistrement.txt",'a')
        fich.write(chaine)
        fich.close()
    

def offrandes(driver):
    k=nb_offrandes
    gains=[]
    pertes=[]
    while k>0:
        l_gains=[]
        l_pertes=[]
        k-=1
        achats_ressources_offrandes(driver)
        elem = driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/div/div[2]/div/div/div[5]/div[2]/input")
        driver.execute_script("return arguments[0].scrollIntoView();",elem)
        elem.click()
        l_gains.append((driver.find_element_by_xpath("//*[@id='info']/div/table/tbody/tr[1]/td[2]/div/div[2]/div[2]/div[4]/div[2]/div[3]/div[2]/div[1]").text,int(driver.find_element_by_xpath("//*[@id='info']/div/table/tbody/tr[1]/td[2]/div/div[2]/div[2]/div[4]/div[2]/div[3]/div[2]/div[2]/strong").text.split(' ')[1])))
        l_gains.append((driver.find_element_by_xpath("//*[@id='info']/div/table/tbody/tr[1]/td[2]/div/div[2]/div[2]/div[4]/div[2]/div[4]/div[2]/div[1]").text,int(driver.find_element_by_xpath("//*[@id='info']/div/table/tbody/tr[1]/td[2]/div/div[2]/div[2]/div[4]/div[2]/div[4]/div[2]/div[2]/strong").text.split(' ')[1])))
        l_pertes.append((driver.find_element_by_xpath("//*[@id='info']/div/table/tbody/tr[1]/td[2]/div/div[2]/div[2]/div[4]/div[1]/div[3]/div[2]/div[1]").text,int(driver.find_element_by_xpath("//*[@id='info']/div/table/tbody/tr[1]/td[2]/div/div[2]/div[2]/div[4]/div[1]/div[3]/div[2]/div[2]/strong").text.split(' ')[1])))
        l_pertes.append((driver.find_element_by_xpath("//*[@id='info']/div/table/tbody/tr[1]/td[2]/div/div[2]/div[2]/div[4]/div[1]/div[4]/div[2]/div[1]").text,int(driver.find_element_by_xpath("//*[@id='info']/div/table/tbody/tr[1]/td[2]/div/div[2]/div[2]/div[4]/div[1]/div[4]/div[2]/div[2]/strong").text.split(' ')[1])))
        enregistre(l_gains,l_pertes,0)
        ajout(l_gains,gains)
        ajout(l_pertes,pertes)
    enregistre(gains,pertes,1)

def main():
    if nb_serie_offrande==-1:
        while True:
            time_temp=time.time()
            driver=connexion(pseudo)
            offrandes(driver)
            driver.close()
            l=(time_temp-time.time()+3600)/60
            for k in range(int(l)):
                print(str(int(l)-k)+" min avant la prochaine offrande")
                time.sleep(60)
    else:
        k=0
        while k<nb_serie_offrande:
            time_temp=time.time()
            driver=connexion(pseudo)
            offrandes(driver)
            driver.close()
            l=(time_temp-time.time()+3600)/60
            for k in range(int(l)):
                print(str(int(l)-k)+" min avant la prochaine offrande")
                time.sleep(60)
            k+=1

main()