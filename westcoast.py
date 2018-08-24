from bs4 import BeautifulSoup
import urllib

url = "http://data.wcrc.govt.nz/cgi-bin/HydWebServer.cgi"
htmlContent = urllib.urlopen(url).read()

soup = BeautifulSoup(htmlContent, 'html.parser')

tableRows = soup.find('table').find(
    'table').find_all('table')[4].find_all('tr')

riverArray = []

for row in tableRows[4:]:
    rowArray = row.find_all('td')
    riverArray.append({
        "siteName": rowArray[0].get_text().encode("ascii").strip(),
        "lastUpdate": rowArray[1].get_text().encode("ascii").strip(),
        "currentFlow": rowArray[4].get_text().encode("ascii").strip(),
        "currentLevel": rowArray[2].get_text().encode("ascii").strip()
    })
