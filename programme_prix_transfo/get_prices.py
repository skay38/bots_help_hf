# //*[@id="acheter1"]/div[2]/div[1]
# //*[@id="acheter31"]/div[2]/div[1]
# //*[@id="acheter1"]/div[5]/strong
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

path_webdriver=os.getcwd()
os.environ["PATH"] += os.pathsep + path_webdriver

pseudo=input("Quel pseudo ?")
MDP=input("Quel mot de passe ?")

LISTE_RESSOURCES = ['Viande',
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
 'Chèvre',
 'Vache',
 'Poule',
 'Chevaux',
 'Bateau de pêche',
 'Navire de fret',
 'Charrette',
 'Zeppelin']

dict_prix = {'Viande': 25,
 'Poisson': 25,
 'Pain': 25,
 'Fruit': 25,
 'Légume': 25,
 'Fromage': 25,
 'Miel': 25,
 'Lait': 25,
 'Oeuf': 25,
 'Epice': 25,
 'Tonneau de bière': 25,
 'Bouteille de vin': 25,
 'Bouteille de cidre': 25,
 'Bijoux': 25,
 'Poterie': 25,
 'Vêtement': 25,
 'Bougie': 25,
 'Livre': 25,
 'Parfum': 25,
 'Fourrure': 25,
 'Bois': 25,
 'Bois précieux': 25,
 'Peau de bête': 25,
 'Cuir': 25,
 'Pierre': 25,
 'Gemme': 25,
 'Argile': 25,
 'Fer': 25,
 'Corde': 25,
 'Fleur': 25,
 'Foin': 25,
 'Blé': 25,
 'Farine': 25,
 'Orge': 25,
 'Lin': 25,
 'Chanvre': 25,
 'Teinture': 25,
 'Potion de soin': 25,
 'Plante médicinale': 25,
 'Cire d’abeille': 25,
 'Encre': 25,
 'Perle noire': 25,
 'Armure': 25,
 'Arme': 25,
 'Tunique': 25,
 'Arc': 25,
 'Arme de siège': 25,
 'Navire de guerre': 25,
 'Chèvre': 25,
 'Vache': 25,
 'Poule': 25,
 'Chevaux': 25,
 'Bateau de pêche': 25,
 'Navire de fret': 25,
 'Charrette': 25,
 'Zeppelin': 25}

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

def get_all_prices():
    driver = connexion()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[1]/a[3]/div").click()
    
    tot = 0
    end = False
    while not end:
        time.sleep(1)
        for i in range(1,31):
            k = 30 * tot + i
            try:
                ressource = driver.find_element_by_xpath("//*[@id='acheter{0}']/div[2]/div[1]".format(k)).text
            except:
                end = True
                break
            try:
                prix = int(driver.find_element_by_xpath("//*[@id='acheter{0}']/div[5]".format(k)).text[:-1])
            except:
                prix = 0
            if not ressource in dict_prix:
                dict_prix[ressource] = prix
            else:
                dict_prix[ressource] = min(dict_prix[ressource], prix)
        driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/div/div[6]/div/div/div[3]/a").click()
        tot += 1
    driver.close()
    return dict_prix

#liste_ressource = ""
#for key in dict_prix:
#    liste_ressource = liste_ressource + key + '\n'
#
#f = open('liste_ressource.txt', 'w')
#f.write(liste_ressource)
#f.close()