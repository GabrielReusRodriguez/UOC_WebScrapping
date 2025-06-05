import os
from urllib.request import urlretrieve, urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup

downloadDir = './data'
baseUrl = 'https://pythonscraping.com/'

# Obtenemos la url base para generar las urls
baseNetloc = urlparse(baseUrl).netloc

# En este funcion creamos la url a descargar con la url base + el recurso 
def getAbsoluteURL(source):
    if urlparse(baseUrl).netloc == '':
        return baseUrl + source
    return source


# creamos la estructura de carpetas EN LOCAL segun la estructura de la web.º
def getDownloadPath(fileUrl):
    parsed = urlparse(fileUrl)
    netloc = parsed.netloc.strip('/')
    path = parsed.path.strip('/')
    localfile = f'{downloadDir}/{netloc}/{path}'
    
    # Si por lo que sea la carpeta NO existe, la creamos.
    localpath = '/'.join(localfile.split('/')[:-1])
    if not os.path.exists(localpath):
        os.makedirs(localpath)
    return localfile

# Cargamos la url base
html = urlopen(baseUrl)
# Parseamos la web
bs = BeautifulSoup(html, 'html.parser')
# Obtenemos todo lo que tenga src 
downloadList = bs.findAll(src=True)
# para cada  elemento... aplico la descarfa.
for download in downloadList:
    fileUrl = getAbsoluteURL(download['src'])
    if fileUrl is not None:
        try:
            urlretrieve(fileUrl, getDownloadPath(fileUrl))
            print(fileUrl)
        except Exception as e:
            print(f'Could not retrieve {fileUrl} Error: {e}')