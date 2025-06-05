""" 
    Este programa sirve para descargar una imagen de la url y dejarla en el disco.
"""

from urllib.request import urlretrieve, urlopen
from bs4 import BeautifulSoup

URL = 'http://www.pythonscraping.com'

html = urlopen(URL)
bs = BeautifulSoup(html, 'html.parser')
imageLocation = bs.find('img', {'alt': 'python-logo'})['src']
urlretrieve(imageLocation, './data/logo.jpg')

