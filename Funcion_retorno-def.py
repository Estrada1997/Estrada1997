# Estructuras de control de Phyton - (def)
'''Funcion con retorno del valor'''
def calificacion(cal):
    suma = 0
    for n in cal:
        suma += n
    return suma / len(cal)

# llama a la funcion
listado = [13, 2, 17, 8, 5]
promedio = calificacion(listado)
print('Sus calificaciones son: {} y como resultado de su promedio final es: = {}'.format(listado, promedio))