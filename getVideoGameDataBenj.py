from bs4 import BeautifulSoup, element
import urllib.request
import pandas as pd  # mostly for using dataframes
import numpy as np  # mostly for numpy arrays. NumPy is the fundamental package for scientific computing with Python. It contains among other things: a powerful N-dimensional array object


pages = 3

urlhead = 'http://www.vgchartz.com/gamedb/?page='
urltail = '&console=&region=All&developer=&publisher=&genre=&boxart=Both&ownership=Both'
urltail += '&results=1000&order=Sales&showtotalsales=0&showtotalsales=1&showpublisher=0'
urltail += '&showpublisher=1&showvgchartzscore=0&shownasales=1&showdeveloper=1&showcriticscore=1'
urltail += '&showpalsales=0&showpalsales=1&showreleasedate=1&showuserscore=1&showjapansales=1'
urltail += '&showlastupdate=0&showothersales=1&showgenre=1&sort=GL'

for page in range(1, pages):
    surl = urlhead + str(page) + urltail
    r = urllib.request.urlopen(surl).read()
    soup = BeautifulSoup(r,  features="html.parser")
    # print(f"Page: {page}")  # this is to show progress in the terminal
