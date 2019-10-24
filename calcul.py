import os
import csv
import requests
from bs4 import BeautifulSoup

departville = input('Choisir la ville de départ\n')
arriveville = input("Choisir la ville d'arriver\n")



def tempstrajet() :
    url = "https://www.bonnesroutes.com/distance/?from="+ departville + "&to=" + arriveville
    requete = requests.get(url)
    data = BeautifulSoup(requete.content)
    # kilometres = data.find_all("td", {"class": "value"})
    # convertedInt = int(kilometres)
    kilometres = 525
    tempsmin = (kilometres/90)*60
    temps = tempsmin/60
    
    print(departville, arriveville, kilometres, temps)



tempstrajet()


