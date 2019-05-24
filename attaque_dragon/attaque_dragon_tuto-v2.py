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

def connexion():
    driver = webdriver.Chrome()
    driver.get("http://www.heroicfantasy.eu/")
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

def nbr_pa(driver):
    return(int(driver.find_element_by_xpath("//*[@id='pa']").text[:-3].replace(' ','')))

def attaque_dragon():
    driver=connexion()
    while nbr_pa(driver)>100:
        t=0
        for i in range(1,25):
            deplacer(driver,i)
            print(i)
            driver.find_element_by_xpath("/html/body/div[1]/a[4]/div").click()
            driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/div[2]/a[2]/div").click()
            for k in driver.find_elements_by_tag_name("strong"):
                if k.text=="Chasse au Dragon":
                    print(driver.find_element_by_xpath("//*[@id='pnj6']/div[2]/div/div[1]/div[7]").text)
                    k.click()
                    driver.find_element_by_xpath("/html/body/div[9]/div[3]/div/button[1]").click()
                    driver.find_element_by_xpath("/html/body/div[1]/div[1]").click()
                    t=1
                    break
            if t==1:
                break
            else:
                driver.find_element_by_xpath("/html/body/div[1]/div[1]").click()

attaque_dragon()
        