"""
    Clase de excepcion por temas relacionados con red.
"""
class NetworkError(Exception):
    
    def __init__(self, err:Exception):
        self.error = err

    def verbose(self):
        print(f"\tERROR: {str(self.error)}", end='\n')