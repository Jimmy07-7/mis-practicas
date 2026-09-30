import datetime


def saludar():
    print("Hola, Bienvenidos")

def mostrar_hora():
    hora_actual = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"La hora actual es: {hora_actual}")

def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    print(f"El área del triángulo es: {area}")

def saludar_persona(nombre, edad):
    print(f"Hola {nombre}, tienes {edad} años")
    
    #empieza la actividad

#sin parametros
def mostrar_motivacion():
    print("Sigue practicando")

def despedir():
    print("Adios, nos vemos luego")
    
#con parametros
def convertir_celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C equivalen a {fahrenheit}°F")

def calcular_descuento(precio, porcentaje):
    descuento = precio * (porcentaje / 100)
    precio_final = precio - descuento
    print(f"Precio original: ${precio} | Con {porcentaje}% de descuento: ${precio_final}")

# Ejecución de las Funciones 

saludar()
mostrar_hora()
calcular_area_triangulo(10, 5)
saludar_persona("Luis", 28)

# Actividad
mostrar_motivacion()
despedir()
convertir_celsius_a_fahrenheit(100)
calcular_descuento(1500, 40)