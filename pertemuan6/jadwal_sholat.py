from bs4 import BeautifulSoup
import requests

def jadwal_sholat(url):
    contents = requests.get(url=url)
    
    response = BeautifulSoup(contents.text, "html.parser")
    data = response.find_all("tr", class_="table_adzan")

    sholat = {}

    i = 0
    for val in data:
        if(i == 1):
            sholat["subuh"] = val.get_text()
        elif(i == 2):
            sholat["subuh"] = val.get_text()
        elif(i == 3):
            sholat["subuh"] = val.get_text()
        elif(i == 4):
            sholat["subuh"] = val.get_text()
        elif(i == 5):
            sholat["subuh"] = val.get_text()

        i += 1
    
    return sholat