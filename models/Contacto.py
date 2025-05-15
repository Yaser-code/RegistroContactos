class Contacto:
    def __init__(self, nombre, apellido, correo, telefono, pais):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__correo = correo
        self.__telefono = telefono
        self.__pais = pais
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getCorreo(self):
        return self.__correo
    def getTelefono(self):
        return self.__telefono
    def getPais(self):
        return self.__pais
    
    def setNombre(self, nombre):
        self.__nombre = nombre
    def setApellido(self, apellido):
        self.__apellido = apellido
    def setCorreo(self, correo):
        self.correo = correo
    def setTelefono(self, telefono):
        self.__telefono = telefono
    def setPais(self, pais):
        self.__pais = pais