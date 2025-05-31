"""
    Ejemplo del PDF WebScarping de Maria par trabajar los TAGs con la libreria Beautifulsoup
"""
import bs4
#from bs4 import BeautifulSoup

HTML_TEXT = '<b id="b1" class =" clase1 clase2">Ejemplo de TAG</b>'

def print_dom(beautifulsoup: bs4.BeautifulSoup):
    tag = soup.b
    print(f"Value HTML: \n{soup.prettify()}", end='\n\n')
    print(f"Tag properties:\n")
    print(f"\tTag type: {type(tag)}")
    print(f"\tTag name: {tag.name}")
    print(f"\tTag attributes : {tag.attrs}")
    for attr in tag.attrs:
        if (type(tag[attr]) == bs4.element.AttributeValueList):
            print(f"\t\tAttribute list: {attr} ...")
            for value in tag[attr]:
                print(f"\t\t\t{value}")
        else:
            print(f"\t\t\tAttribute {attr} => \"{tag[attr]}\"")


soup = bs4.BeautifulSoup(HTML_TEXT, 'html.parser')
print(f"Value HTML: \n{soup.prettify()}", end='\n\n')
# Ahora accedemos al tag y a los atributos del tag
tag = soup.b
print(f"Tag properties:\n")
print(f"\tTag type: {type(tag)}")
print(f"\tTag name: {tag.name}")
print(f"\tTag attributes : {tag.attrs}")
for attr in tag.attrs:
    if (type(tag[attr]) == bs4.element.AttributeValueList):
        print(f"\t\tAttribute list: {attr} ...")
        """
            tag[attr] es una lista por lo que si quiero modificar un miembro de esa lista, 
            necesito el indice dentro de la lista, no solo el valor que nos devuelve el for in...
            Para eso convierto la lista en un enumerate y puedo obtener tanto el valor como el indice dentro de la lista.
        """
        for index, value in enumerate(tag[attr]):
            print(f"\t\t\t{value}")
            # Concateno el _1 al valor que tenia
            value += "_1"
            tag[attr][index] =  value
    else:
        print(f"\t\t\tAttribute {attr} => \"{tag[attr]}\"")
        tag[attr] = tag[attr] + "_2"
# Por último, añado un tag nuevo
tag['estudiante'] = 'gabriel'
tag['empleado'] = 'gabriel'
# Elimino el attributo empleado con del.
del tag['empleado']
print(f"Post - modifiedd \n\n")
print_dom(soup)