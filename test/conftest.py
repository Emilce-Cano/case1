import pytest

#conftest es un archivo de configuración para pytest, en el que se pueden definir fixtures, hooks, etc.

#fixture es una función que se ejecuta antes de cada prueba, y que puede ser utilizada para preparar el entorno de prueba, por ejemplo, para crear objetos, abrir conexiones a bases de datos, etc.
#como defino una fixture? con el decorador @pytest.fixture, y luego la función que define la fixture, por ejemplo:

# @pytest.fixture
# def db():
#     db = Database()
#     db.connect()
#     yield db
#     db.disconnect()
#es un decorativo que indica que la función es una fixture, y luego la función que define la fixture, en este caso, se crea una instancia de la clase Database, se conecta a la base de datos, se devuelve la instancia de la base de datos con yield, y luego se desconecta de la base de datos después de que se haya ejecutado la prueba.
# como utilizo esta funsion en mis pruebas? simplemente la incluyo como argumento en la función de prueba, por ejemplo:
@ pytest.fixture
def numero():
    return 10,2
    
