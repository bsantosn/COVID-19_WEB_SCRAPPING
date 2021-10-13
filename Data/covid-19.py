#imports

import requests
import csv
import pandas as pd
from bs4 import BeautifulSoup


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

    datos_clean = data_clean(datos)

    data_calculation(datos_clean)

    return datos_clean

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


#################### DATOS REFERENTES A VACUNAS DE LA COVID-19 ####################

#Conseguir datos de vacunación
def scrapping_vaccine():
    vaccine = requests.get("https://datosmacro.expansion.com/otros/coronavirus-vacuna/")
    soup = BeautifulSoup(vaccine.text, "html.parser")
    rows = soup.find('table', attrs={'id': 'tb1'}).find('tbody').find_all('tr')
    colum = ["Country", "Date vaccinated", "Administered doses", "Vaccinated people", "Fully vaccinated", "% Fully vaccinated","fully vaccinated_2"]
    list = []
    final = []
    for row in rows:
        for item in row.find_all('td'):
            list.append(item.text.replace("\n", "").replace(".", "").replace(",", ".").replace(" [+]","").strip())
        final.append(list)
        list = []

    datos = pd.DataFrame(final, columns=colum)

    data_clean = data_clean_vaccine(datos)

    return data_clean


# Coger las columnas que necesitamos
# Pasar los paises a mayúsculas y en inglés.
def data_clean_vaccine(datos):
    datos["Country"] = datos["Country"].str.upper()

    country = []
    for i in datos["Country"]:
        country.append(paises.get(i))

    datos = datos.drop(["Country", "Administered doses", "Vaccinated people", "fully vaccinated_2"], axis=1)
    datos.insert(loc=0, column="Country", value=country)

    return datos

#################### UNIMOS LOS DATOS DE LOS CASOS DE COVID-19 Y LAS VACUNAS ####################
def datos_finales(covid,vaccine):
    df_inner = pd.merge(covid, vaccine, on='Country', how='inner')
    return df_inner


#################### EXPORTAR DATOS A UN CSV ####################
def export_csv(datos):

    datos.to_csv("covid_19.csv",index=False)
    return "OK"


if __name__ == '__main__':
    #1. Obtenemos los datos referentes al covid-19
    datos_covid = scrapping_covid()
    print("Tabla con los datos iniciales de casos de coronavirus:\n",datos_covid)

    #2. datos referentes a la vacunación
    datos_vaccine = scrapping_vaccine()
    print("Tabla con los datos iniciales de vacunados:\n",datos_vaccine)

    #3. Unión de los datos del covid-19 y vacunas
    dataset = datos_finales(datos_covid, datos_vaccine)
    print("Datos finales:\n",dataset)

    #4.Exportamos los datos a un csv
    print("Exportados los datos al fichero covid.csv con resultado: ",export_csv(dataset))


