import libs
from bs4 import BeautifulSoup


"""
    Programa que obtiene el titulo de una url con beautifulsoup.
"""

URLs = [
            'https://www.uoc.edu', 
            'BAD URL', 
            'https://www.gencat.cat'
        ]

html = None

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
        title = bs.title
        # Aqui ya tengo el tag title ( si no lo encuentra, lanzará la excepcion). Paso a obtener el contenido con get_text()
        print(f"\tTITLE: {title.get_text()}",end='\n\n')
    except AttributeError as attrErr:
        print(f"\tERROR:  {str(attrErr)}", end='\n\n')
        continue