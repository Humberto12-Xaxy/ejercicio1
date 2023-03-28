from Coche import Coche

def funcion(a:int, b:int, c:int):
    return a + b + c


if __name__ == '__main__':
    micoche = Coche()
    micoche.agregar_puerta()
    micoche.agregar_puerta()
    micoche.agregar_puerta()
    micoche.agregar_puerta()
    print(f'Puertas: {micoche.puertas}')

    resultado = funcion(3, 4, 5)
    print(f'Resultado funcion: {resultado}')