"""
Clase encargada de obtener las urls
"""

from urllib.request import urlopen, Request
from urllib.error import HTTPError
import http
from .NetworkException import NetworkException

"""
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
            'Accept-Encoding' : 'gzip, deflate, br, zstd',
            'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
            'Connecction': 'keep-alive',
            'User-Agent': USER_AGENT
"""

class URLGetter:

    ACCEPT = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    ACCEPT_ENCODING = 'gzip, deflate, br, zstd'
    ACCEPT_LANGUAGE = 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3'
    CONNECTION = 'keep-alive'
    USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:137.0) Gecko/20100101 Firefox/137.0'

    def __init__(self):
        # Con Accept-Language y user-agent, la url que usaremos de ejemplo, ya funciona por lo que de momento no usaremos mas.
        self.headers = {
#           'Accept'            :   URLGetter.ACCEPT,
#           'Accept-Encoding'   :   URLGetter.ACCEPT_ENCODING,
            'Accept-Language'   :   URLGetter.ACCEPT_LANGUAGE,
#            'Connection'        :   URLGetter.CONNECTION,
            'User-Agent'        :   URLGetter.USER_AGENT

        }
    
#    def get(self, url:str) ->  http.client.HTTPResponse:
    def get(self, url:str):
        try:
            req = Request(url, headers = self.headers)
            html = urlopen(req)
            return html
        except HTTPError as error:
            raise NetworkException(error)
