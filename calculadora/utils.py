def pedir_opcion():
    
    print("\n =========Bienvenido a la calculadora========")
    while True:
        print("\n Opciones: ")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
            
        opcion = input("elija la opcion del 1 - 4): \n")
        
        opcion_valida = {
            "1": "suma",
            "2": "resta",
            "3": "multiplicacion",
            "4": "division"
        }
        try: 
            opcion_valida[opcion]
            return opcion
        except KeyError:
            print("opcion invalida, elige la opcion correcta")
            
            
def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: ingrese un numero valido")   
            
            
def resultado(result):
    if result is not None:
        print(f"el resultado es: {result}")
    else:
        print("No se pudo realizar la operacion")   