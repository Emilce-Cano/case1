
from calculadora.utils import pedir_opcion, pedir_numero, resultado
from calculadora.operaciones import sumar, restar, multiplicar, dividir


while True:

    opcion = pedir_opcion()
        
    a = pedir_numero("Ingrese el primer numero: ")
    b = pedir_numero("Ingrese el segundo numero: ")
    
    match opcion:
            case "1":
                result = sumar(a,b)
                resultado(result)
            case "2":
                result = restar(a,b)
                resultado(result)
            case "3":
                result = multiplicar(a,b)
                resultado(result)
            case "4":
                result = dividir(a, b)
                resultado(result)
                
        
            
    otra = input("desea realizar otra operacion s/n ?")
    if otra != "s":
            print("hasta la proxima")
            break
        