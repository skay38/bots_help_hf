# -*- coding: utf-8 -*-
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from multiprocessing import Queue
import time

path_webdriver=os.getcwd()
os.environ["PATH"] += os.pathsep + path_webdriver

pseudo=input("Quel pseudo ?")
MDP=input("Quel mot de passe ?")
mult_achat=50

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

def nbr_partisans(driver):
    return(int(driver.find_element_by_xpath("//*[@id='partisan']").text))

def achats_ressources_distribution(driver):
    elem=driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/div/div[2]/div/div/div[3]/div[2]/div/div/div[2]/div[2]/strong").text
    if int(elem.split(' / ')[0].replace(' ',''))<int(elem.split(' / ')[1].replace(' ','')):
        nbr_achat=int(elem.split(' / ')[1].replace(' ',''))*mult_achat
        elem=driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/div/div[2]/div/div/div[3]/div[2]/div/a")
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
        try:
            if "Vous n’avez pas toutes les pièces d’or" in driver.find_element_by_xpath("//*[@id='info']/div/table/tbody/tr[1]/td[2]/div/p").text or "Pour éviter les dérives du commerce abusif, les échanges entres deux joueurs sont limités par heure." in driver.find_element_by_xpath("//*[@id='info']/div/table/tbody/tr[1]/td[2]/div/p").text:
                return(0)
            else:
                driver.find_element_by_xpath("/html/body/div[1]/div[1]").click()
        except:
            driver.find_element_by_xpath("/html/body/div[1]/div[1]").click()
    elem=driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/div/div[2]/div/div/div[3]/div[3]/div/div/div[2]/div[2]/strong").text
    if int(elem.split(' / ')[0].replace(' ',''))<int(elem.split(' / ')[1].replace(' ','')):
        nbr_achat=int(elem.split(' / ')[1].replace(' ',''))*mult_achat
        elem=driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/div/div[2]/div/div/div[3]/div[3]/div/a")
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
        try:
            if "Vous n’avez pas toutes les pièces d’or" in driver.find_element_by_xpath("//*[@id='info']/div/table/tbody/tr[1]/td[2]/div/p").text or "Pour éviter les dérives du commerce abusif, les échanges entres deux joueurs sont limités par heure." in driver.find_element_by_xpath("//*[@id='info']/div/table/tbody/tr[1]/td[2]/div/p").text:
                return(0)
            else:
                driver.find_element_by_xpath("/html/body/div[1]/div[1]").click()
        except:
            driver.find_element_by_xpath("/html/body/div[1]/div[1]").click()
    elem=driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/div/div[2]/div/div/div[3]/div[4]/div/div/div[2]/div[2]/strong").text
    if int(elem.split(' / ')[0].replace(' ',''))<int(elem.split(' / ')[1].replace(' ','')):
        nbr_achat=int(elem.split(' / ')[1].replace(' ',''))*mult_achat
        elem=driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/div/div[2]/div/div/div[3]/div[4]/div/a")
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
        try:
            if "Vous n’avez pas toutes les pièces d’or" in driver.find_element_by_xpath("//*[@id='info']/div/table/tbody/tr[1]/td[2]/div/p").text or "Pour éviter les dérives du commerce abusif, les échanges entres deux joueurs sont limités par heure." in driver.find_element_by_xpath("//*[@id='info']/div/table/tbody/tr[1]/td[2]/div/p").text:
                return(0)
            else:
                driver.find_element_by_xpath("/html/body/div[1]/div[1]").click()
        except:
            driver.find_element_by_xpath("/html/body/div[1]/div[1]").click()
    elem=driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/div/div[2]/div/div/div[3]/div[5]/div/div/div[2]/div[2]/strong").text
    if int(elem.split(' / ')[0].replace(' ',''))<int(elem.split(' / ')[1].replace(' ','')):
        nbr_achat=int(elem.split(' / ')[1].replace(' ',''))*mult_achat
        elem=driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/div/div[2]/div/div/div[3]/div[5]/div/a")
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
        try:
            if "Vous n’avez pas toutes les pièces d’or" in driver.find_element_by_xpath("//*[@id='info']/div/table/tbody/tr[1]/td[2]/div/p").text or "Pour éviter les dérives du commerce abusif, les échanges entres deux joueurs sont limités par heure." in driver.find_element_by_xpath("//*[@id='info']/div/table/tbody/tr[1]/td[2]/div/p").text:
                return(0)
            else:
                driver.find_element_by_xpath("/html/body/div[1]/div[1]").click()
        except:
            driver.find_element_by_xpath("/html/body/div[1]/div[1]").click()
    return(1)

def distributions(driver):
    while nbr_partisans(driver)<500:
        t=achats_ressources_distribution(driver)
        if t==1:
            elem = driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/div/div[2]/div/div/div[3]/div[6]/div[2]/input")
            driver.execute_script("return arguments[0].scrollIntoView();",elem)
            elem.click()
    driver.find_element_by_xpath("/html/body/div[1]/div[1]").click()

driver=connexion()
while True:
    distributions(driver)
    driver.find_element_by_xpath("/html/body/div[1]/a[4]/div").click()
    driver.find_element_by_xpath("//*[@id='Recru1']").click()
    driver.find_element_by_xpath("//*[@id='newTroupe']/div[2]/div[6]/div[2]/img").click()
    driver.find_element_by_xpath("/html/body/div[8]/div[3]/div/button[1]/span").click()
    driver.find_element_by_xpath("/html/body/div[1]/div[1]").click()