"""
    Ejemplo de scarpping de un fichero doc.
"""

from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
from bs4 import BeautifulSoup

# Obtengo el contenido de la url.
wordFile = urlopen('http://pythonscraping.com/pages/AWordDocument.docx').read()
# Obtengo los byhtes de lo leido
wordFile = BytesIO(wordFile)
# Descomprimo los bytes leidos
document = ZipFile(wordFile)
xml_content = document.read('word/document.xml')

# Aqui tenemos un documento XML por lo que lo parseamos con beautifulsoup.
wordObj = BeautifulSoup(xml_content.decode('utf-8'), 'xml')
# Buscamos los elementos XML t con namespace w
textStrings = wordObj.findAll('w:t')

# Para cada elemento encontrado, printamos
for textElem in textStrings:
    print(textElem.text)