import mysql.connector

def establecerConexion():
    miConexion = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "contactosPython"
    )
    return miConexion