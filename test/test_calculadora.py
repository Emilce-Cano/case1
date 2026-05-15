import pytest
from calculadora.operaciones import sumar, dividir

#esto serian casos de prueba, es decir, lo que se va a probar| 
#en este caso la suma y la division, se pueden agregar mas casos de prueba para cada operacion,
#por ejemplo, para la suma se pueden agregar casos de prueba para sumar numeros negativos,
# numeros decimales, etc.
def test_sumar_positivos(numero):
    a,b = numero
    assert sumar(a,b) == 12
    
# def test_sumar_negativos():
#     assert sumar(-2, -6) == -8
    

