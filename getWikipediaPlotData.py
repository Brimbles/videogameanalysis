from bs4 import BeautifulSoup, element, UnicodeDammit
import urllib.request
import csv
import pandas as pd


# prepare the url to which we will apend each video game title
urlhead = 'https://en.wikipedia.org/wiki/'

# with open('vgsales SAMPLE.csv') as file:

line_number = 2
with open('vgsales SAMPLE.csv') as f:
    mycsv = csv.reader(f)
    # # print(f' csv reader type? = ' + str(type(mycsv)))
    # mycsv = list(mycsv)
    # # print(f' csv list type? = ' + str(type(mycsv)))
    # print(mycsv[1:])
    df = pd.DataFrame(mycsv)
    new_header = df.iloc[0]  # grab the first row for the header
    df = df[1:]  # take the data less the header row
    df.columns = new_header  # set the header row as the df header

    print(df)


# df = df.iloc[:, 1]  # get all rows from column 2 (name of game)
# print(df1)
# for each l in mycsv:
#     print(mycsv[line_number][1])
# text = mycsv[line_number][1]
# print(f' text variable type? = ' + str(type(text)))

for index, row in df.iterrows():
    # print(row['Name'])
    namecolunicode = row['Name'].encode('utf-8')
    urlheadunicode = urlhead.encode('utf-8')
    surl = urlheadunicode + namecolunicode

    # surl = surl.replace(" ", "_")
    print(surl)
    r = urllib.request.urlopen(surl.decode('ASCII')).read()
    # r = urllib.request.urlopen(surl).read()
    soup = BeautifulSoup(r,  features="html.parser")
    # soupdf = pd.dataframe(soup)
    # soupdf.to_csv("soupcsv.csv", sep=",", encoding='utf-8')
    print(soup)
