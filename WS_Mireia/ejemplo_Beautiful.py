"""
Ejemplo de parseo de una página con BeautifulSoup  del PDF  WebScarping de Mireia
"""

import requests as rq
from bs4 import BeautifulSoup

urls = ['https://www.gencat.cat', 'https://www.uoc.edu']

for url in urls:
    # Primero descargamos la url.
    page = rq.get(url)
    """
        Luego pasamos el contenido de la web por la clase BeautifulSoup. Primero le paso el contenido y el segundo parametro es el parser que quiero
        by default es html.parser pero se lo indico.
    """
    soup = BeautifulSoup(page.content, 'html.parser')
    # Imprimimos la url pero con espacios y hecho bonito.
    print(f" url: {url}\n content parseado: \n{soup.prettify()}", end= '\n\n')
    input("Press enter to continue...")