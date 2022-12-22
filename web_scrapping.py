from bs4 import BeautifulSoup as bs
import requests 
import pandas as pd
bright_stars_url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page = requests.get(bright_stars_url)
soup = bs(page.text,'html.praser')
star_table = soup.find('table')
templist = []
table_rows = star_table.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    templist.append(row)
star_name = []
distance = []
mass = []
radius = []
lum = []
for i in range(1,len(templist)):
    star_name.append(templist[i][1])
    distance.append(templist[i],[3])
    mass.append(templist[i][5])
    radius.append(templist[i][6])
    lum.append(templist[i],[7])
df2 = pd.DataFrame(list(zip(star_name,distance,mass,radius,lum)),columns=['star_name','distance','mass','radius','luminosity'])
df2.to_csv('bright_stars.csv')

