"""
Clase de excepcion Custom.
"""

class NetworkException(Exception):

    def __init__(self, error : Exception):
        self.error = error
