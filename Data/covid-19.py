#imports
import requests
import csv
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

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

    #constructor
    def __init__(self,url):
        self.url = url

    #función para obtener datos referentes al coronavirus
    def scrapping_covid(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"}
        covid = requests.get(self.url,headers=headers)
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

    #función para eliminar las filas y columnas que no nos interesan
    #Se sustituyen los "" por 0
    #Se pone en mayúsculas la variable country
    def data_clean(self,datos):

        datos = datos.drop(datos[datos["ID"] == ""].index)
        datos = datos.drop(["ID","Tot Cases 1M pop","Tests 1M pop","1 Case every X ppl", "1 Death every X ppl"
                 ,"1 Test every X ppl", "New Cases/1M pop", "New Deaths/1M pop",
                 "Active Cases/1M pop"], axis=1)
        datos["Total Deaths"] = datos["Total Deaths"].replace("", "0").astype(int)
        datos["Population"] = datos["Population"].replace("", "0").astype(int)
        datos["Country"] = datos["Country"].str.upper()

        return datos

    #Cáculo de nuevos campos para el dataframe
    def data_calculation(self,datos):
        return datos.insert(loc=13, column="% Deaths COVID/Population",value=round((datos["Total Deaths"] / datos["Population"]) * 100, 2))

    #Se eliminan las columnas que no necesitamos, se convierten variables a tipo entero y la variable Country se pasa a mayúsculas
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
        vaccine = requests.get(self.url,headers=headers)
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
    # Pasar los paises a mayúsculas y en inglés.
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


#################### UNIMOS LOS DATOS DE LOS CASOS DE COVID-19 Y LAS VACUNAS ####################
class InfoCovid(Coronavirus,Vacunas):

    #constructor
    def __init__(self,covid,vaccine):
        self.covid = covid
        self.vaccine = vaccine

    # Se meten en un mismo dataframe la información referente al coronavirus y las vacunas
    def datos_finales(self):
            df_inner = pd.merge(self.covid, self.vaccine, on='Country', how='inner')
            return df_inner


#################### EXPORTAR DATOS A UN CSV ####################
def export_csv(datos):

    datos.to_csv("covid_19.csv",index=False)
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


if __name__ == '__main__':
    #1. Obtenemos los datos referentes al covid-19
    covid = Coronavirus("https://www.worldometers.info/coronavirus/")
    datos_covid = covid.scrapping_covid()
    print("Tabla con los datos iniciales de casos de coronavirus:\n",datos_covid)

    #2. Datos referentes de la vacunación
    vacuna = Vacunas("https://datosmacro.expansion.com/otros/coronavirus-vacuna/")
    datos_vaccine = vacuna.scrapping_vaccine()
    print("Tabla con los datos iniciales de vacunados:\n",datos_vaccine)

    # 3. Unión de los datos del covid-19 y vacunas
    infocovid = InfoCovid(datos_covid,datos_vaccine)
    dataset = infocovid.datos_finales ()
    print ( "Datos finales:\n" , dataset)

    # 4.Exportamos los datos a un csv
    print("Exportados los datos al fichero covid.csv con resultado:", export_csv(dataset))

    # 5. Visualizar datos
    print("Visualizar datos:\n ", visualization(dataset))
