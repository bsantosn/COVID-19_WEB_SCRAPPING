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
            list.append(item.text.replace("\n", "").replace(",", "").strip())
        final.append(list)
        list = []

    datos = pd.DataFrame(final, columns=colum)


    return datos

#función para eliminar las filas y columnas que no nos interesan
#Se substituyen los "" por 0
#Se pone en mayúsculas la variable country
def data_clean(datos):

    datos = datos.drop(datos[datos["ID"] == ""].index)
    datos = datos.drop(["ID","Tot Cases 1M pop","Tests 1M pop","Continent","1 Case every X ppl", "1 Death every X ppl"
             ,"1 Test every X ppl", "New Cases/1M pop", "New Deaths/1M pop",
             "Active Cases/1M pop"], axis=1)
    datos["Total Deaths"] = datos["Total Deaths"].replace("", "0").astype(int)
    datos["Population"] = datos["Population"].replace("", "0").astype(int)
    datos["Country"] = datos["Country"].str.upper()
    return datos

#cáculo de nuevos campos para el dataframe
def data_calculation(datos):
    return datos.insert(loc=12, column="% Deaths COVID/Population",value=round((datos["Total Deaths"] / datos["Population"]) * 100, 2))


#función para exportar los datos a un csv
def export_csv(datos):

    datos.to_csv("covid.csv",index=False)
    return "OK"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #1. Obtenemos los datos referentes al covid-19
    print("Tabla con los datos iniciales:\n",scrapping_covid())
    datos = scrapping_covid()

    #2. Preparamos los datos con las columnas y filas que nos interesan para el análisis
    print("Preparación de datos:\n",data_clean(datos))
    datos_covid = data_clean(datos)

    #3. Nuevos campos calculados
    print("Se insertan nuevos campos calculados\n")
    data_calculation(datos_covid)

    #4. Exportamos los datos a un csv
    print("Exportados los datos al csv covid.csv: ",export_csv(datos_covid))


