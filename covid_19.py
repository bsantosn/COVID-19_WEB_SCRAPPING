from utils import *

if __name__ == '__main__':
    # 1. Obtenemos los datos referentes al covid-19
    covid = Coronavirus("https://www.worldometers.info/coronavirus/")
    datos_covid = covid.scrapping_covid()
    print("Tabla con los datos iniciales de casos de coronavirus:\n", datos_covid)

    # 2. Datos referentes de la vacunación
    vacuna = Vacunas("https://datosmacro.expansion.com/otros/coronavirus-vacuna/")
    datos_vaccine = vacuna.scrapping_vaccine()
    print("Tabla con los datos iniciales de vacunados:\n", datos_vaccine)
    
    # 3. Datos referentes de la vacunación al pib
    gdp = Gdp("https://datosmacro.expansion.com/pib")
    datos_gdp = gdp.scrapping_gdp()
    print("Tabla con los datos iniciales del PIB:\n", datos_gdp)

    # 4. Datos referentes de a la temperatura
    temperature = Temperature("https://en.wikipedia.org/w/index.php?title=Special:UserLogin")
    datos_temperature = temperature.scraping_temperature()
    print("Tabla con los datos iniciales de la temperatura media:\n", datos_temperature)

    # 5. Unión de los datos del covid-19 , vacunas y pib
    infocovid = InfoCovid(datos_covid, datos_vaccine, datos_gdp, datos_temperature)
    dataset = infocovid.datos_finales()
    print("Datos finales:\n", dataset)

    # 6.Exportamos los datos a un csv
    print("Exportados los datos al fichero covid.csv con resultado:", export_csv(dataset))

    # 7. Visualizar datos
    print("Visualizar datos:\n ", visualization(dataset))
