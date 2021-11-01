# imports
import errno
import requests
import os
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time



##### TRADUCCION ESP-EN PAÍSES #####

paises = {
"ESPAÑA" : "SPAIN",
"ALEMANIA" : "GERMANY",
"REINO UNIDO" : "UK",
"FRANCIA" : "FRANCE",
"ITALIA" : "ITALY",
"PORTUGAL" : "PORTUGAL",
"ESTADOS UNIDOS" : "USA",
"JAPÓN" : "JAPAN",
"CHINA" : "CHINA",
"ANDORRA" : "ANDORRA",
"EMIRATOS ÁRABES UNIDOS" : "UAE",
"AFGANISTÁN" : "AFGHANISTAN",
"ANTIGUA Y BARBUDA" : "OLD AND BEARDED",
"ALBANIA" : "ALBANIA",
"ARMENIA" : "ARMENIA",
"ANGOLA" : "ANGOLA",
"ARGENTINA" : "ARGENTINA",
"AUSTRIA" : "AUSTRIA",
"AUSTRALIA" : "AUSTRALIA",
"AZERBAIYÁN" : "AZERBAIJAN",
"BOSNIA Y HERZEGOVINA" : "BOSNIA AND HERZEGOVINA",
"BARBADOS" : "BARBADOS",
"BANGLADÉS" : "BANGLADESH",
"BÉLGICA" : "BELGIUM",
"BULGARIA" : "BULGARIA",
"BARÉIN" : "BARÉIN",
"BRUNÉI" : "BRUNEI",
"BOLIVIA" : "BOLIVIA",
"BRASIL" : "BRAZIL",
"BAHAMAS" : "BAHAMAS",
"BUTÁN" : "BHUTAN",
"BOTSUANA" : "BOTSWANA",
"BIELORRUSIA" : "BELARUS",
"BELICE" : "BELIZE",
"CANADÁ" : "CANADA",
"REPÚBLICA DEMOCRÁTICA DEL CONGO" : "DEMOCRATIC REPUBLIC OF CONGO",
"REPÚBLICA DEL CONGO" : "CONGO",
"SUIZA" : "SWITZERLAND",
"COSTA DE MARFIL" : "IVORY COAST",
"CHILE" : "CHILE",
"CAMERÚN" : "CAMEROON",
"COLOMBIA" : "COLOMBIA",
"COSTA RICA" : "COSTA RICA",
"CABO VERDE" : "CABO VERDE",
"CHIPRE" : "CYPRUS",
"REPÚBLICA CHECA" : "CZECHIA",
"YIBUTI" : "DJIBOUTI",
"DINAMARCA" : "DENMARK",
"DOMINICA" : "DOMINICA",
"REPÚBLICA DOMINICANA" : "DOMINICAN REPUBLIC",
"ARGELIA" : "ALGERIA",
"ECUADOR" : "ECUADOR",
"ESTONIA" : "ESTONIA",
"EGIPTO" : "EGYPT",
"ETIOPÍA" : "ETHIOPIA",
"FINLANDIA" : "FINLAND",
"FIYI" : "FIJI",
"ESTADOS FEDERADOS DE MICRONESIA" : "MICRONESIA",
"GABÓN" : "GABON",
"GRANADA" : "GRENADA",
"GEORGIA" : "GEORGIA",
"GHANA" : "GHANA",
"GAMBIA" : "GAMBIA",
"GUINEA" : "GUINEA",
"GUINEA ECUATORIAL": "EQUATORIAL GUINEA",
"GRECIA": "GREECE",
"GUATEMALA": "GUATEMALA",
"GUYANA": "GUYANA",
"HONG KONG": "HONG KONG",
"HONDURAS": "HONDURAS",
"CROACIA": "CROATIA",
"HUNGRÍA": "HUNGARY",
"INDONESIA": "INDONESIA",
"IRLANDA": "IRELAND",
"ISRAEL": "ISRAEL",
"INDIA": "INDIA",
"IRAK": "IRAQ",
"IRÁN": "IRAN",
"ISLANDIA": "ICELAND",
"JAMAICA": "JAMAICA",
"JORDANIA": "JORDAN",
"KENIA": "KENYA",
"KIRGUISTÁN": "KYRGYZSTAN",
"CAMBOYA": "CAMBODIA",
"COMORAS": "COMOROS",
"SAN CRISTÓBAL Y NIEVES": "SAINT KITTS AND NEVIS",
"COREA DEL SUR": "S. KOREA",
"KUWAIT":   "KUWAIT",
"KAZAJISTÁN": "KAZAKHSTAN",
"LAOS": "LAOS",
"LÍBANO": "LEBANON",
"SANTA LUCÍA": "SAINT LUCIA",
"LIECHTENSTEIN": "LIECHTENSTEIN",
"SRI LANKA": "SRI LANKA",
"LESOTO": "LESOTHO",
"LITUANIA": "LITHUANIA",
"LUXEMBURGO": "LUXEMBOURG",
"LETONIA": "LATVIA",
"LIBIA": "LIBYA",
"MARRUECOS": "MOROCCO",
"MÓNACO": "MONACO",
"MOLDAVIA": "MOLDOVA",
"MONTENEGRO": "MONTENEGRO",
"ISLAS MARSHALL": "MARSHALL ISLANDS",
"MACEDONIA DEL NORTE": "NORTH MACEDONIA",
"MALÍ": "MALI",
"BIRMANIA - MYANMAR": "BIRMANIA - MYANMAR",
"MONGOLIA": "MONGOLIA",
"MAURITANIA": "MAURITANIA",
"MALTA": "MALTA",
"MAURICIO": "MAURITIUS",
"MALDIVAS": "MALDIVES",
"MALAUI": "MALAWI",
"MÉXICO": "MEXICO",
"MALASIA": "MALAYSIA",
"MOZAMBIQUE": "MOZAMBIQUE",
"NAMIBIA": "NAMIBIA",
"NÍGER": "NIGER",
"NIGERIA": "NIGERIA",
"NICARAGUA": "NICARAGUA",
"PAÍSES BAJOS": "NETHERLANDS",
"NORUEGA": "NORWAY",
"NEPAL": "NEPAL",
"NAURU": "NAURU",
"NUEVA ZELANDA": "NEW ZEALAND",
"OMÁN": "OMAN",
"PANAMÁ": "PANAMA",
"PERÚ": "PERU",
"PAPÚA NUEVA GUINEA": "PAPUA NEW GUINEA",
"FILIPINAS": "PHILIPPINES",
"PAKISTÁN": "PAKISTAN",
"POLONIA": "POLAND",
"ESTADO DE PALESTINA": "PALESTINE",
"PALAOS": "PALAU",
"PARAGUAY": "PARAGUAY",
"CATAR": "QATAR",
"RUMANÍA": "ROMANIA",
"SERBIA": "SERBIA",
"RUSIA": "RUSSIA",
"RUANDA": "RWANDA",
"ARABIA SAUDITA": "SAUDI ARABIA",
"ISLAS SALOMÓN": "SOLOMON ISLANDS",
"SEYCHELLES": "SEYCHELLES",
"SUDÁN": "SUDAN",
"SUECIA": "SWEDEN",
"SINGAPUR": "SINGAPORE",
"ESLOVENIA": "SLOVENIA",
"ESLOVAQUIA": "SLOVAKIA",
"SIERRA LEONA": "SIERRA LEONE",
"SAN MARINO":"SAN MARINO",
"SENEGAL": "SENEGAL",
"SOMALIA": "SOMALIA",
"SURINAM": "SURINAME",
"SUDÁN DEL SUR": "SOUTH SUDAN",
"SANTO TOMÉ Y PRÍNCIPE": "SAO TOME AND PRINCIPE",
"EL SALVADOR": "EL SALVADOR",
"SIRIA":"SYRIA",
"SUAZILANDIA": "SWAZILAND",
"TOGO": "TOGO",
"TAILANDIA": "THAILAND",
"TÚNEZ": "TUNISIA",
"TONGA": "TONGA",
"TURQUÍA": "TURKEY",
"TRINIDAD Y TOBAGO": "TRINIDAD AND TOBAGO",
"TAIWAN": "TAIWAN",
"UCRANIA": "UKRAINE",
"UGANDA": "UGANDA",
"URUGUAY": "URUGUAY",
"UZBEKISTÁN": "UZBEKISTAN",
"SAN VICENTE Y LAS GRANADINAS": "ST. VINCENT GRENADINES",
"VENEZUELA": "VENEZUELA",
"VIETNAM": "VIETNAM",
"SAMOA": "SAMOA",
"SUDÁFRICA": "SOUTH AFRICA",
"ZAMBIA": "ZAMBIA",
"ZIMBABUE": "ZIMBABWE"
}


#################### DATOS REFERENTES A CASOS DE LA COVID-19 ####################

class Coronavirus:

    # Constructor
    def __init__(self,url):
        self.url = url

    # función para obtener datos referentes al coronavirus
    def scrapping_covid(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"}
        covid = requests.get(self.url, headers=headers)
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

        datos_clean = self.data_clean(datos)

        self.data_calculation(datos_clean)

        return datos_clean

    # función para eliminar las filas y columnas que no nos interesan
    # Se sustituyen los "" por 0
    # Se pone en mayúsculas la variable country
    def data_clean(self,datos):

        datos = datos.drop(datos[datos["ID"] == ""].index)
        datos = datos.drop(["ID","Tot Cases 1M pop","Tests 1M pop","1 Case every X ppl", "1 Death every X ppl"
                 ,"1 Test every X ppl", "New Cases/1M pop", "New Deaths/1M pop",
                 "Active Cases/1M pop"], axis=1)
        datos["Total Deaths"] = datos["Total Deaths"].replace("", "0").astype(int)
        datos["Population"] = datos["Population"].replace("", "0").astype(int)
        datos["Country"] = datos["Country"].str.upper()

        return datos

    # Cáculo de nuevos campos para el dataframe
    def data_calculation(self,datos):
        return datos.insert(loc=13, column="% Deaths COVID/Population",value=round((datos["Total Deaths"] / datos["Population"]) * 100, 2))

    # Se eliminan las columnas que no necesitamos, se convierten variables a tipo entero y la variable Country se pasa a mayúsculas

    def data_clean(self,datos):

        datos = datos.drop(datos[datos["ID"] == ""].index)
        datos = datos.drop(["ID", "Tot Cases 1M pop", "Tests 1M pop", "1 Case every X ppl", "1 Death every X ppl"
                               , "1 Test every X ppl", "New Cases/1M pop", "New Deaths/1M pop",
                            "Active Cases/1M pop"], axis=1)
        datos["Total Deaths"] = datos["Total Deaths"].replace("", "0").astype(int)
        datos["Population"] = datos["Population"].replace("", "0").astype(int)
        datos["Country"] = datos["Country"].str.upper()

        return datos

    # Cáculo de nuevos campos para el dataframe
    def data_calculation(self,datos):
        return datos.insert(loc=13, column="% Deaths COVID/Population",
                            value=round((datos["Total Deaths"] / datos["Population"]) * 100, 2))

#################### DATOS REFERENTES DE LAS VACUNAS ####################
class Vacunas:

    #constructor
    def __init__ (self,url):
        self.url = url

    # Conseguir datos de vacunación
    def scrapping_vaccine(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"}
        vaccine = requests.get(self.url, headers=headers)
        soup = BeautifulSoup(vaccine.text, "html.parser")
        rows = soup.find('table', attrs={'id': 'tb1'}).find('tbody').find_all('tr')
        colum = ["Country", "Date vaccinated update", "Administered doses", "Vaccinated people", "Fully vaccinated",
                 "% Fully vaccinated", "fully vaccinated_2"]
        list = []
        final = []
        for row in rows:
            for item in row.find_all('td'):
                list.append(
                    item.text.replace("\n", "").replace(".", "").replace(",", ".").replace(" [+]", "").replace("%","").strip())
            final.append(list)
            list = []

        datos = pd.DataFrame(final, columns=colum)

        data_clean = self.data_clean_vaccine(datos)

        return data_clean

    # Coger las columnas que necesitamos
    # Pasar los países a mayúsculas y en inglés.
    def data_clean_vaccine(self,datos):
        datos["Country"] = datos["Country"].str.upper()

        country = []
        for i in datos["Country"]:
            country.append(paises.get(i))

        datos["Fully vaccinated"] = datos["Fully vaccinated"].replace("", "0").astype(int)
        datos["% Fully vaccinated"] = round(datos["% Fully vaccinated"].replace("", "0").astype(float) / 100, 2)
        datos = datos.drop(["Country", "Administered doses", "Vaccinated people", "fully vaccinated_2"], axis=1)
        datos.insert(loc=0, column="Country", value=country)

        return datos

#################### DATOS REFERENTES AL GDP DE LOS PAISES ####################

class Gdp:

    # constructor
    def __init__(self, url):
        self.url = url

    # Conseguir datos de gdp
    def scrapping_gdp(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"}
        gdp = requests.get(self.url, headers=headers)
        soup = BeautifulSoup(gdp.text, "html.parser")
        rows = soup.find('table', attrs={'id': 'tbA'}).find('tbody').find_all('tr')
        colum = ["Country", "Year_GDP_update", "GDP_Annual (M)", "GDP_Var1", "GDP_Var2", "GDP_Var3", "GDP_Var4", "GDP_Var5"]
        list = []
        final = []
        for row in rows:
            for item in row.find_all('td'):
                list.append(
                    item.text.replace("\n", "").replace(".", "").replace(",", ".").replace(" [+]", "").replace("%","").replace("M€","").strip())
            final.append(list)
            list = []

        datos = pd.DataFrame(final, columns=colum)

        data_clean = self.data_clean_gdp(datos)

        return data_clean

    # Coger las columnas que necesitamos
    # Pasar los países a mayúsculas y en inglés.
    def data_clean_gdp(self, datos):
        datos["Country"] = datos["Country"].str.upper()

        country = []
        for i in datos["Country"]:
            country.append(paises.get(i))

        datos = datos.drop(["Country", "GDP_Var1", "GDP_Var2", "GDP_Var3", "GDP_Var4", "GDP_Var5"], axis=1)
        datos.insert(loc=0, column="Country", value=country)
        idx = datos.groupby(['Country'])['Year_GDP_update'].transform(max) == datos['Year_GDP_update']
        datos = datos[idx]

        return datos

#################### DATOS REFERENTES A LA TEMPERATURA MEDIA DE LOS PAISES ####################

class Temperature:

    # constructor
    def __init__(self, url):
        self.url = url

    def scraping_temperature(self):

        # Accedemos al puglin de googlechrome
        s = Service(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=s)
        browser.maximize_window()

        browser.get(self.url)
        # Asignamos un nombre de usario y una contraseña
        file = open('Resources/config.txt')
        lines = file.readlines()
        username = lines[0]
        password = lines[1]
        time.sleep(1)
        # Accedemos al elemento de nombre usuario
        elementID = browser.find_element(By.NAME, 'wpName')
        # Rellenamos el formulario
        elementID.send_keys(username)
        # Accedemos al elemento de la contraseña
        elementPW = browser.find_element(By.NAME, 'wpPassword')
        time.sleep(1)
        # Rellenamos el formulario
        elementPW.send_keys(password)
        # Accedemos a la parte de búsqueda y escribimos lo que queremos buscar
        elementS = browser.find_element(By.NAME, 'search')
        time.sleep(1)
        elementS.send_keys('List of countries by average yearly temperature')
        # Accedemos al botón de búsqueda y clicamos en el
        time.sleep(4)
        elementB = browser.find_element(By.ID, 'searchButton')
        elementB.click()
        url = browser.current_url
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"}
        temperature = requests.get(url, headers=headers)
        soup = BeautifulSoup(temperature.text, "html.parser")
        # Obtenemos la información de la tabla
        rows = soup.find('table').find('tbody').find_all('tr')
        colum = ["Country", "Temperature_1961_1990"]
        list = []
        final = []
        for row in rows:
            for item in row.find_all('td'):
                list.append(item.text.replace("\n", "").replace(u'\xa0',""))
            final.append(list)
            list = []

        datos = pd.DataFrame(final, columns=colum)
        time.sleep(1)
        browser.quit()

        data_clean = self.data_clean_temperature(datos)

        return data_clean


    def data_clean_temperature(self, datos):

        datos.drop(index=datos.index[0], axis=0, inplace=True)
        datos['Country'] = datos['Country'].str.upper()

        return datos


#################### UNIMOS LOS DATOS DE LOS CASOS DE COVID-19, LAS VACUNAS , GDP Y TEMPERATURA ####################

class InfoCovid(Coronavirus, Vacunas, Gdp, Temperature):

    # constructor
    def __init__(self, covid, vaccine, gdp, temperature):
        self.covid = covid
        self.vaccine = vaccine
        self.gdp = gdp
        self.temperature = temperature

    # Se meten en un mismo dataframe la información referente al coronavirus y las vacunas
    def datos_finales(self):
            df_inner = pd.merge(self.covid, self.vaccine, on='Country', how='inner')
            df_inner_2 = pd.merge(df_inner,self.gdp, on='Country', how='inner')
            df_final = pd.merge(df_inner_2, self.temperature, on='Country', how='left')
            return df_final


#################### EXPORTAR DATOS A UN CSV ####################
def export_csv(datos):
    try:
        os.makedirs('Dataset/')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    datos.to_csv("Dataset/covid_19.csv", index=False)
    return "OK"


######### VISUALIZAR DATOS #########
def visualization(datos):
    plt.bar(datos["Continent"], datos["Total Deaths"])
    plt.ylabel('Total Deaths')
    plt.xlabel('Continent')
    plt.show()

    plt.bar(datos["Continent"], datos["% Fully vaccinated"])
    plt.ylabel('% Fully vaccinated')
    plt.xlabel('Continent')
    plt.show()

