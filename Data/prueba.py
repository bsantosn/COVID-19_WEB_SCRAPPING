#imports

import requests
import csv
import pandas as pd
from bs4 import BeautifulSoup


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    world_population = requests.get("https://www.worldometers.info/world-population/")
    soup = BeautifulSoup(world_population.text,"html.parser")
    rows = soup.find('table', attrs={'id':'popbycountry'}).find('tbody').find_all('tr')
    ListWorldPop = ["ID","Country","Population","Yearly Change","Next Change","Density","Land Area","Migrants","Fert","Med. Age","Urban","World"]
    list =[]
    final =[]
    for row in rows:
       for item in row.find_all('td'):
           list.append(item.text)
       final.append(list)
       list = []

    print(final)
    datos = pd.DataFrame(final,columns=ListWorldPop)
    #datos["World"] = datos["Country"]
    print(datos)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
