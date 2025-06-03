from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from .NetworkError import *

"""
    Funcion para descargar los recursos de la url que le pasamos.
"""
def urlGet(url: str):
    try:
        html = urlopen(url= url)
        return html
    except (ValueError, HTTPError, URLError) as error:
        err = NetworkError(error)
        #err.verbose()
        raise err
    """
    except ValueError as valErr:
        err = NetWorkError(valErr)
        err.verbose()
        raise err
    except HTTPError as httpErr:
        print (f"HTTP ERROR: {str(httpErr)}")
        raise httpErr
    except URLError as urlErr:
        print (f"URL ERROR: {str(urlErr)}")
        raise urlErr
    """
    return None
