from time import *
import os
import csv
import requests
from bs4 import BeautifulSoup



def tempstrajet() :


    # Récupération des villes
    departville = input('Choisir la ville de départ\n')
    arriveville = input("Choisir la ville d'arriver\n")

    # Récupération des informations (distance)
    url = "https://www.bonnesroutes.com/distance/?from="+ departville + "&to=" + arriveville
    requete = requests.get(url)
    data = BeautifulSoup(requete.content)
    # kilometres = data.find_all("td", {"class": "value"})
    # convertedInt = int(kilometres)
    kilometres = 582


    # Convertir les kilomètres en temps HH:MM
    tempssec = (kilometres/90) * 3600
    temps = strftime("%H : %M",localtime(tempssec))
    
    # Resultat retourné
    print(departville, arriveville, kilometres, temps)



tempstrajet()


