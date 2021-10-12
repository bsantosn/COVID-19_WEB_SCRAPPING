#imports

import requests
import csv
import pandas as pd
from bs4 import BeautifulSoup

#función para obtener datos referentes al coronavirus

def scrapping_covid():
    covid = requests.get("https://www.worldometers.info/coronavirus/")
    soup = BeautifulSoup(covid.text, "html.parser")
    rows = soup.find('table', attrs={'id': 'main_table_countries_today'}).find('tbody').find_all('tr')
    colum = ["ID", "Country",
             "Total Cases", "New Cases", "Total Deaths", "New Deaths",
             "Total Recovered", "New Recovered", "Active Cases", "Serious Critical"
             ,"Tot Cases 1M pop", "Deaths 1M pop", "Total Tests"
             ,"Tests 1M pop", "Population", "Continent", "1 Case every X ppl", "1 Death every X ppl"
             ,"1 Test every X ppl", "New Cases/1M pop", "New Deaths/1M pop",
             "Active Cases/1M pop"]
    list = []
    final = []
    for row in rows:
        for item in row.find_all('td'):
            list.append(item.text.replace("\n", "").replace(",", "."))
        final.append(list)
        list = []

    datos = pd.DataFrame(final, columns=colum)
    datos = datos.drop(datos[datos["ID"] == ""].index)

    return datos


def export_csv(datos):

    datos.to_csv("covid.csv")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print("Tabla con los datos iniciales:\n",scrapping_covid())
    print("Exportados los datos al csv: covid.csv")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
