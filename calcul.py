import os
import csv
import requests
from bs4 import BeautifulSoup

departville = input('Choisir la ville de départ\n')
arriveville = input("Choisir la ville d'arriver\n")


url = "https://www.bonnesroutes.com/distance/?from="+ departville + "&to=" + arriveville
requete = requests.get(url)
data = BeautifulSoup(requete.content)
kilometres = data.find_all("td", {"class": "distance"})






print(departville, arriveville, kilometres.string)