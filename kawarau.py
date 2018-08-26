from bs4 import BeautifulSoup
import urllib2

importantRivers = ["Kawarau at Chards Road",
                   "Nevis at Wentworth Station", "Shotover at Bowens Peak"]

url = "http://water.orc.govt.nz/WaterInfo/Summary.aspx"
htmlContent = urllib2.urlopen(url).read()

soup = BeautifulSoup(htmlContent, 'html.parser')
tableRows = soup.find('table', {'id': 'Kawarau-rainfall'}).find_all('tr')

riverArray = []

for row in tableRows[2:]:
    rowArray = row.find_all('td')
    siteName = rowArray[0].get_text().encode("ascii").strip()

    if siteName in importantRivers:
        riverArray.append({
            "siteName": siteName,
            "lastUpdate": rowArray[1].get_text().encode("ascii").strip(),
            "currentFlow": rowArray[2].get_text().encode("ascii").strip(),
            "currentLevel": rowArray[3].get_text().encode("ascii").strip()
        })
