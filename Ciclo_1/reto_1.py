def nota_quices(codigo: str, nota1: int, nota2: int, nota3: int, nota4: int, nota5: int) -> str:
    ''' Nota quices
    :Parámetros:
     codigo (str): codigo único alfanumérico del estudiante
     nota (int): Nota de los quices reto semestre (0 - 100)
     Retorno:
     String: de la forma "El promedio ajustado del estudiante {codigo} es: {promedio}" dónde, el promedio se
    calcula eliminando la peor nota y se reporta con dos decimales utilizando la escala numérica de 0 a 5
     '''
    valor_min = min(nota1, nota2, nota3, nota4, nota5)
    promedio = (nota1 + nota2 + nota3 + nota4 + nota5 - valor_min)/4
    return "El promedio ajustado del estudiante {} es: {}".format(codigo, round(promedio/20, 2))


print(nota_quices("AA0010276", 19, 90, 38, 55, 68))
print(nota_quices("IS00201620", 37, 10, 50, 19, 79))
print(nota_quices("BIO2201810", 45, 46, 33, 74, 22))
print(nota_quices("IQ102201810", 57, 100, 87, 93, 21))
print(nota_quices("MA00201520", 5, 14, 76, 91, 5))
