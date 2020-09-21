import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


hockey_stats = 'http://www.collegehockeystats.net/1920/textstats/wism'

page = requests.get(hockey_stats)
#ddlQuery > table > tbody > tr > td.rcbInputCell.rcbInputCellLeft
soup = BeautifulSoup(page.text, 'html.parser')
table = soup.find("pre").contents[0]

data = []

for i in table:
    data.append(i)

dataFrame = pd.DataFrame(data = data, columns = ['Data'])

# Converting Pandas DataFrame
# into CSV file
dataFrame.to_csv(r'C:\Users\GRIFKAD1\Desktop\test.csv')



# table = table.replace("-", "")
# table = table.replace("|", "")
# li = list(table.split(" "))
print(li)
print(table)
for i in table:
    print(i)
# text parsers


domains = soup.find_all("pre", class_="tiny")

print(results)
print(results.prettify())
table = soup.find_all('td', attrs = {'class': 'game-details'}, text=True)[0].text
play = soup.find_all('td', attrs = {'class': 'game-details'})
time = soup.find_all('td', attrs = {'class': 'time-stamp'})

print(soup)

pbp = []
t = []

for i,times in zip(play, time):
    pbp.append(i.text)
    t.append(times.text)

df = pd.DataFrame(
    {'Time': t,
     'Play': pbp,
    })
# df = pd.DataFrame(pbp, columns=['Play'])
print(df)
# for i in play:
#     x = 'Markus' in i.text
#     if x == True:
#         pbp.append(i.text)


# print(play.prettify())
# print(play)
# play = soup.select('#gp-quarter-1 > table > tbody > tr:nth-child(1) > td.game-details') # play.text # play[0].text.strip()
