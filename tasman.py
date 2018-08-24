from bs4 import BeautifulSoup
import urllib

url = "http://www.tasman.govt.nz/environment/water/rivers/river-flow/stage-river-flow-report/"
htmlContent = urllib.urlopen(url).read()

soup = BeautifulSoup(htmlContent, 'html.parser')
tableRows = soup.find_all('tr')

riverArray = []

for row in tableRows[1:]:
    rowArray = row.find_all('td')
    riverArray.append({
        "siteName": rowArray[0].get_text().encode("ascii"),
        "lastUpdate": rowArray[1].get_text().encode("ascii"),
        "currentFlow": rowArray[4].get_text().encode("ascii"),
        "currentLevel": rowArray[2].get_text().encode("ascii")
    })
