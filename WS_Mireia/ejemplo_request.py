import requests as rq

urls = ['https://www.gencat.cat', 'https://www.uoc.edu', 'https://www.upf.edu']

for url in urls:
    print(f"URL: {url}", end= '\n\n')
    page = rq.request(method= 'get', url = url)
    print (f"contenido: \n\t status_code : {page.status_code} \n\t contenido: {page.content}", end = '\n\n')