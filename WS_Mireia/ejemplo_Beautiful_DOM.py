# Ejemplo de navegacion DOM  del PDF WebScrapping de Mireia.

import bs4
import requests as rq

URL = 'http://www.gencat.cat'

page = rq.get(URL)
if page.status_code != 200:
    print(f"ERROR descargando la url {URL}")
soup = bs4.BeautifulSoup(page.content, 'html.parser')
# Printamos el contenido parseado
print(f"CONtenido parseado: \n {soup.prettify()}", end = '\n\n')
print(f"Accedemos por tags...", end= '\n\n')
print(f"TITLE: {soup.title}")
print(f"\tname: {soup.title.name}")
print(f"\tcontenido: {soup.title.string}")
print(f"\tparent: {soup.title.parent.name}")
print(f"", end="\n\n")
# Si obtenemos el primer tag a.
print(f" Obtenemos  el primer tag a (links): \n {soup.a}", end = '\n\n')
# Obtengo TODOS los links
print(f" Obtengo TODOS los links {soup.find_all('a')}", end =  '\n\n')

print(f"Obtengo los hijos del head:")
for child in soup.head.children:
    print(f" Child: {child}")
