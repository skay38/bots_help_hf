# -*- coding: utf-8 -*-
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from multiprocessing import Queue
import time
from random import randrange

fich=open("fich_tresors.txt",'r')
TAB_MOTS=fich.read().split('\n')
fich.close()
path_webdriver=os.getcwd()
os.environ["PATH"] += os.pathsep + path_webdriver

pseudo=input("Quel pseudo ?")
MDP=input("Quel mot de passe ?")

def connexion():
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

def deplacer(driver,i):
    Select(driver.find_element_by_xpath("//*[@id='depRegion']")).select_by_index(i-1)
    driver.find_element_by_xpath("//*[@id='depButton']").click()

def deplacer1(driver,i):
    driver.find_element_by_xpath("//*[@id='depNoble']").send_keys(Keys.ARROW_DOWN)
    Select(driver.find_element_by_xpath("//*[@id='depRegion']")).select_by_index(i-1)
    driver.find_element_by_xpath("//*[@id='depButton']").click()
    
def verif_mot(tab_lettre):
    for k in TAB_MOTS:
        l=1
        for i in tab_lettre:
            if i not in k or len(k)!=len(tab_lettre):
                l=0
                break
        for i in k:
            if i not in tab_lettre:
                l=0
                break
        if l==1:
            return k
    return('0')

def swap(i,j,driver):
    try:
        driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/div[1]/a[4]/div").click()
    except:
        driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/div[2]/a[4]/div").click()
    source=driver.find_element_by_xpath("//*[@id='sortable']/div["+str(i)+"]/div")
    dest=driver.find_element_by_xpath("//*[@id='sortable']/div["+str(j)+"]/div")
    ActionChains(driver).drag_and_drop(source,dest).perform()

def cherche_tresor(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/div[1]/a[4]/div").click()
    except:
        driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/div[2]/a[4]/div").click()
    tab_lettre=[]
    i=1
    while True:
        try:
            tab_lettre.append(driver.find_element_by_xpath("//*[@id='sortable']/div["+str(i)+"]/div").text.lower())
            i+=1
        except:
            break
    mot=verif_mot(tab_lettre)
    print(mot)
    if mot=='0':
        print("mot inconnu !")
        print(tab_lettre)
        driver.close()
        return 0
    else:
        for r in range(len(mot)):
            for k in range(r,len(mot)):
                if tab_lettre[k]==mot[r]:
                    swap(k+1,r+1,driver)
                    tab_lettre=tab_lettre[0:r]+[mot[r]]+tab_lettre[r:k]+tab_lettre[k+1:]
                    break
        return 1

def tresors():
    driver=connexion()
    while True:
        try:
            driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/div[2]/a[4]/div").click()
        except:
            try:
                driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/div[3]/a[4]/div").click()
            except:
                driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/div[1]/a[4]/div").click()
        x1=int(driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/div/div[2]/div[1]/strong").text.split(' : ')[1].split(' / ')[0])
        x2=int(driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/div/div[2]/div[1]/strong").text.split(' : ')[1].split(' / ')[1])
        if x1==x2:
            nb=cherche_tresor(driver)
            if nb==0:
                break
            else:
                driver.find_element_by_xpath("//*[@id='tresorConfirm']").click()
                try:
                    driver.find_element_by_xpath("/html/body/div[8]/div[3]/div/button[1]/span").click()
                except:
                    try:
                        driver.find_element_by_xpath("/html/body/div[8]/div[3]/div/button[2]/span").click()
                    except:
                        driver.find_element_by_xpath("/html/body/div[9]/div[3]/div/button[1]/span").click()
                driver.find_element_by_xpath("/html/body/div[1]/div[1]").click()
        else:
            driver.find_element_by_xpath("/html/body/div[1]/div[1]").click()
            tot=abs(x1-x2)
            while tot>0:
                driver.find_element_by_xpath("/html/body/div[1]/div[1]").click()
                deplacer1(driver,1+randrange(24))
                tot-=1

tresors()