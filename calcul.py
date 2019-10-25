from time import *
import os
import csv
import requests
from bs4 import BeautifulSoup



def tempstrajet() :
    
    # Déclaration de variables utiles
    a = 7200
    nbpause = 0

    # Récupération des villes
    departville = input('Choisir la ville de départ\n')
    arriveville = input("Choisir la ville d'arriver\n")
    
    #Distance (en km) et temps (en seconde) d'accélération et de décélération 
    distanceacceldecel = 7.5 * 2
    tempsacceldecel = 9 * 60 * 2

    # Récupération des informations (distance)
    url = "https://www.bonnesroutes.com/distance/?from="+ departville + "&to=" + arriveville
    requete = requests.get(url)
    data = BeautifulSoup(requete.content)
    # kilometres = data.find_all("td", {"class": "value"})
    # convertedInt = int(kilometres)
    kilometres = 582

    # Convertir les kilomètres en temps HH:MM
    tempssec = ((kilometres - distanceacceldecel)/90) * 3600
    tempstotalsec = tempssec + tempsacceldecel
    tempstotalsecbase = tempstotalsec
    
    # Boucle du nombre de pause
    while a < tempstotalsecbase :
        if a < tempstotalsecbase :
            tempstotalsec + 7200
            a + 7200
            nbpause + 1
            # return temps;
    
    temps = strftime("%H : %M",localtime(tempstotalsec))

    


    # Resultat retourné
    print(departville, arriveville, kilometres, temps, nbpause)



tempstrajet()


