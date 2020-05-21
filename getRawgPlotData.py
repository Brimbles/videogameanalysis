# from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

listofgameids = []
# initialise dataframe
# responsedf = pd.DataFrame()

# dictydic = {'slug': 'somevalue'}
# print(dictydic)

pages = 3

urlheadgameids = 'https://api.rawg.io/api/games?dates=1984-01-01%2C2020-12-31&ordering=-rating&page='
urlheadgamedetails = 'https://api.rawg.io/api/games?ordering=-rating&page='
# params = {"name": 10, "paragraphs": 1, "format": "json"}

# for page in range(1, pages):
#     response = requests.get(urlheadgameids + str(page))
#     # print(type(response))
#     data = (response.json())
#     # print(type(data))
#     resultsinlist = data['results']

#     for item in resultsinlist:
#         # print(item['id'])
#         listofgameids.append(item['id'])

#         # for iditem in listofgameids:
#         #     response = requests.get(urlheadgameids + str(iditem))
#         #     data = response.json()
#         #     # resultsinlist = data['name']
#         #     # print(resultsinlist)
#         #     print(data)

gamedata = {}

for page in range(1, pages):
    response = requests.get(urlheadgameids + str(page))
    data = response.json()
    print(type(data))
    gamedata['results'] = data['results']

df = pd.DataFrame(gamedata)
df.to_csv("x.csv", sep=",", encoding='utf-8', index=False)
