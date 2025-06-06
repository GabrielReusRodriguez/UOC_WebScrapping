"""
    Ejemplo de raspado de pdf.
"""

from urllib.request import  urlretrieve
from pypdf import PdfReader

url = 'http://pythonscraping.com/pages/warandpeace/chapter1.pdf'
pdfRoute = './data/chapter1.pdf'


urlretrieve( url, pdfRoute )

reader = PdfReader(pdfRoute)

# Para cada página, imprimimos el texto
for page in reader.pages:
    print(page.extract_text())