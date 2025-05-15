from database.Conexion import establecerConexion
def guardarContacto(Contacto):
    conexion = establecerConexion()
    cursor = conexion.cursor()
    sql = "INSERT INTO contactos (nombre, apellido, correo, telefono, pais) VALUES (%s, %s, %s, %s, %s)"
    valores = (Contacto.getNombre(), Contacto.getApellido(), Contacto.getCorreo(), Contacto.getTelefono(), Contacto.getPais())
    cursor.execute(sql, valores)
    conexion.commit()
    conexion.close()