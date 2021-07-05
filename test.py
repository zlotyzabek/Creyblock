import ast

lista = ['[0, 4, -1, 0]']

print(lista)

lista = [ast.literal_eval(lista[0])]

print(lista)