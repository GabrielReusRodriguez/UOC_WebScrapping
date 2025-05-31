"""
    Ejemplo del PDF WebScrapping de Mireia de uso de Beautifulsoup y NavigableString.
    NavigableString es el texto que contiene un tag.
"""

import bs4


HTML_TEXT = '<b>Frase dentro del tag de negrita</b>'

soup = bs4.BeautifulSoup(HTML_TEXT, 'html.parser')
tag = soup.b


print(f"El tipo del contenido del tag es: {type(tag.string)} y su valor es: \'{tag.string}\'")

"""
    La unica forma de cambiar el contenido es con la fuinción replace_with
"""

tag.string.replace_with('NUEVO STRING')
print(f"El tipo del contenido del tag es: {type(tag.string)} y su valor es: \'{tag.string}\'")
