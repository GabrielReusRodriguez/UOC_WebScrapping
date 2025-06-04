import libs
from bs4 import BeautifulSoup
import re

"""
    Programa que obtiene  tags segun una expresion regular.
"""

URLs = [
            'https://www.kernel.org', 
            'https://www.google.es'
        ]

html = None

"""
    Para las expresiones regulares importamos la libreria de python re. Primero tenemos que compilarla con la expresion regular que queramos.
    Usaremos una expresion regular para obtener los enlaces a ficheros .html
    [\\d\\w]+ significa que tiene que haber o iun numero o un caracter repetidos > 1 vez .  A continuación va un . \\. ( xq el piunto es cualquier caracter asi que hay que escaparlo)
"""
regularExpression = re.compile(r'[\d\w]+\.html')

# Para cada url del array...
for url in URLs:
    print(f"URL: {url}", end="\n")
    # Obtengo el contenido de la url OJO con las excepciones!!
    try:
        html = libs.urlGet(url)
    except libs.NetworkError as err:
        print(f"{err.verbose()}", end='\n\n')
        continue
    # Creo la instancia de BEautifulsoup para el contenido. Hemos de usar try por si ese tag NO existe.
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        tags = bs.find_all('a', {'href': regularExpression})
        # Aqui ya tengo el tag title ( si no lo encuentra, lanzará la excepcion). Paso a obtener el contenido con get_text()
        print(f"\tLINKS HTML:\n")
        for tag in tags:
            print(f"\t{tag}",end='\n')
    except AttributeError as attrErr:
        print(f"\tERROR:  {str(attrErr)}", end='\n\n')
        continue
