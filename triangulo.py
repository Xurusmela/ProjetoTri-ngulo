# Validation um triangulo.

# Entrada
a = float(input('Digite o valor do lado a: '))
b = float(input('Digite o valor do lado b: '))
c = float(input('Digite o valor do lado c: '))

# Processamento e Saída
if (b - c) < a < b + c and (a - c) < b < a + c and (a - b) < c < a + b:
    print(f'{a}, {b}, {c}, formam um triângulo.')
else:
    print(f'{a}, {b}, {c}, não formam um triângulo.')



