"""
    Clase de logica que implementa el piso.
"""

class Piso:

    def __init__(self, localizacion: str, descripcion: str, precio : str, superficie : str, num_habs : str):

        self.localizacion = localizacion
        self.descripcion = descripcion
        self.precio = precio
        self.superficie = superficie
        self.num_habs = num_habs

    # Esta es la funcion que se llamará cuando se tenga que convertir a string.
    def __str__(self):
        string =""
        string  = 'Piso: \n'
        string += '\t '+ self.localizacion + '\n'
        string += '\t\t' + self.superficie + '\n'
        string += '\t\t' + self.num_habs + '\n'
        string += '\t\t' + self.precio + '\n'
        string += '\t\t' + self.descripcion + '\n' 
        return string

    def to_dict(self)->dict:
        dictionary = {}
        dictionary['localizacion'] = self.localizacion
        dictionary['superficie'] = self.superficie
        dictionary['num_habs'] = self.num_habs
        dictionary['precio'] = self.precio
        dictionary['descripcion'] = self.descripcion
        return (dictionary)