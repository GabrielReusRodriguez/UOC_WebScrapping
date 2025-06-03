import libs
from bs4 import BeautifulSoup


"""
    Programa que obtiene todos los enlaces de las urls consultadas
"""

URLs = [
            'https://www.github.com', 
            'https://www.google.es'
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
        tags = bs.find_all('a')
        # Aqui ya tengo el tag title ( si no lo encuentra, lanzará la excepcion). Paso a obtener el contenido con get_text()
        print(f"\tLINKS:\n")
        for tag in tags:
            print(f"\t{tag}",end='\n')
    except AttributeError as attrErr:
        print(f"\tERROR:  {str(attrErr)}", end='\n\n')
        continue