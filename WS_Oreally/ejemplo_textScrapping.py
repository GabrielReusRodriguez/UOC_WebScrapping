"""
    Ejemplo de Scraping un fichero txt en utf-8
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

# obtenemos el contenido html de la url
html = urlopen('http://en.wikipedia.org/wiki/Python_(programming_language)')
# Lo parseamos con beautifulSoup
bs = BeautifulSoup(html, 'html.parser')
# Buscamos los divs con el identificador conforme tienen texto
content = bs.find('div', {'id':'mw-content-text'}).get_text()
# Transformamos el contenido a bytes en utf8 (multi-byte)
content = bytes(content, 'UTF-8')
# PAra imprimirlo decodificamos de UTF-8 a la codifcacion interna de Python.
content = content.decode('UTF-8')
print(content)
