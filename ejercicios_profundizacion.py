#!/usr/bin/env python
'''
Tipos de variables [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.3

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.3"


def ej1():
    # Ejercicios de práctica con números
    print('Nuestra primera calculadora')
    '''
    Realice un calculadora, se ingresará por línea de comando dos
    números reales y se deberá calcular todas las operaciones entre ellos:
    - Suma
    - Resta
    - Multiplicación
    - División
    - Exponente/Potencia

    - Para todos los casos se debe imprimir en pantalla el resultado aclarando
      la operación realizada en cada caso y con que números
      se ha realizado la operación
      ej: La suma entre 4.2 y 6.5 es 10.7

    '''
    print('Ingrese el primer número decimal a operar:')
    numero_1 = float(input())
    print("numero ingresado", numero_1)

    print('Ingrese el segundo número decimal a operar:')
    numero_2 = float(input())
    print("numero ingresado", numero_2)

    suma = numero_1 + numero_2
    resta = numero_1 - numero_2
    division = numero_1 / numero_2
    multiplicacion = numero_1 * numero_2
    potencia = numero_1**numero_2
    print("la suma entre", numero_1, "y", numero_2, "da un total de", suma)
    print("la resta entre", numero_1, "y", numero_2, "da un total de", resta)
    print("la division entre", numero_1, "y", numero_2, "da un total de", division)
    print("la multiplicacion entre", numero_1, "y", numero_2, "da un total de", multiplicacion)
    print("la potencia entre", numero_1, "y", numero_2, "da un total de", potencia)



def ej2():
    print('Ejercicios de práctica numérica y cadenas')
    '''
    Realice un programa que consulte por consola:
    - El nombre completo de la persona
    - El DNI de la persona
    - La edad de la persona
    - La altura de la persona

    Finalmente el programa debe imprimir dos líneas de texto por separado
    - En una línea imprimir el nombre completo y el DNI, aclarando de que
      campo se trata cada uno
            Ej: Nombre Completo: Nombre Apellido , DNI:35205070,
    - En la segunda línea se debe imprimir el nombre completo, edad y
      altura de la persona
      Nuevamente debe aclarar el campo de cada uno, para el que lo lea
      entienda de que se está hablando.

    '''
    print('Ingrese su nombre/s y apellido:')
    nombre = str(input())
    print('Ingrese su DNI:')
    dni = int(input())
    print('Ingrese su edad:')
    edad = int(input())
    print('Ingrese su altura:')
    altura = float(input())

    print("el nombre es", nombre, "y el documento", dni)
    print("su altura es", edad, "y el documento", altura)


def ej3():
    print('Ejercicios de práctica con cadenas')

    '''
    Realice un programa que determine cual sería el apellido de una persona
    si se ingresaran los dos nombres completos de sus padres.
    Dicha persona deberá tener los apellidos de ambos padres

    - Primero el programa debe consultar el nombre completo del padre_1
    - Luego el programa debe consultar el nombre completo del padre_2
    - Luego debe consultar el nombre del hijo/a
    - Debe extraer los apellidos de los padres
    - Luego formar el nombre completo del hijo/a utilizando los apellidos
      de sus padres
      y el nombre ingresado de dicha persona
    - Imprimir en pantalla el resultado

    NOTA: Para extraer el apellido del nombre completo recomendamos usar
    el método "split"
    Mostraremos un ejemplo:

    direccion_completa = 'Monroe 2716'
    calle, altura = direccion_completa.split(' ')

    Les dejo por su cuenta a que busquen un poco más acerca de este método
    que seguramente utilizarán mucho de acá en adelante.
    Les dejamos un link con algunos ejemplos más:
    https://www.pythonforbeginners.com/dictionary/python-split

    Cualquier duda con el método split pueden consultarla por el campus

    '''
    print('Ingrese el nombre y apellido de su padre:')
    nombre_padre = str(input())
    print('Ingrese el nombre y apellido de su madre:')
    nombre_madre = str(input())
    print('Ingrese su nombre:')
    nombre_hijo = str(input())

    nombre_padre.split(" ")
    nombre_madre.split(" ")

    name_padre,surname_padre = nombre_padre.split(" ")
    name_madre,surname_madre = nombre_madre.split(" ")

    print("su nombre completo es:", nombre_hijo,surname_padre,surname_madre)



def ej4():
    # Ejercicios de práctica con cadenas
    print('Comencemos a ponernos serios')
    '''
    Realice un programa que determine si una persona_2
    es pariente de la persona_1
    Para facilitar el ejercicio solo ingresar un nombre
    y un apellido por persona
    Ingresar dichos datos como Nombre Apellido, es decir,
    primero el nombre y luego el apellido, separado por un espacio.
    - El programa debe consultar primero el nombre completo de la persona_1
    - Luego debe consultar el nombre completo de la persona_2
    - Debe extraer el apellido de la persona_2
    - Luego preguntar si apellido de la persona_2 está contenido
      en el nombre completo de la persona_1
    - En caso de contenerlo, son parientes
    - Imprimir en pantalla el resultado

    NOTA: Para extraer el apellido del nombre recomendamos
    usar el método "split"
    Mostraremos un ejemplo:

    direccion_completa = 'Monroe 2716'
    calle, altura = direccion_completa.split(' ')

    Les dejo por su cuenta a que busquen un poco más acerca
    de este método que seguramente utilizarán mucho de acá en adelante.
    Les dejamos un link con algunos ejemplos más:
    https://www.pythonforbeginners.com/dictionary/python-split

    Cualquier duda con el método split pueden consultarla por el campus
    '''
    print('Ingrese el primer nombre y apellido:')
    nombre_1 = str(input())
    print('Ingrese el segundo nombre y apellido:')
    nombre_2 = str(input())
    
    nombre_1.split(" ")
    nombre_2.split(" ")

    name_1,surname_1 = nombre_1.split(" ")
    name_2,surname_2 = nombre_2.split(" ")

    if surname_1 == surname_2:
      print("Existe parentezco")
    else:
      print("no hay parentezco")


def ej5():
    # Ejercicios de práctica con cadenas
    print('Ahora si! buena suerte!')
    '''
    Realice un programa que reciba por consola su nombre completo
    e imprima en pantalla su nombre en los siguientes formatos:
    - Todas las letras en minúsculas
    - Todas las letras en mayúsculas
    - Solo la primera letra del nombre en mayúscula

    NOTA: Para realizar este ejercicio deberá usar los siguientes métodos
    de strings:
    - lower
    - upper
    - capitalize

    Puede buscar en internet como usar en Python estos métodos.
    Les dejamos el siguiente link que posee casos de uso de algunos de ellos:

    Link de referencia:
    https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/

    Cualquier duda con estos métodos pueden consultarla por el campus
    '''
    print('Ingrese su nombre y apellido completo:')
    nombre_completo = str(input())

    print(nombre_completo.lower())
    print(nombre_completo.upper())
    print(nombre_completo.capitalize())


if __name__ == '__main__':
    print("Ejercicios de práctica")
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()
