'''
Crie um programa que recebe 2 números reais como entrada e um operador matemático. 
De acordo com o operador matemático fornecido, o progrma deve calcular e apresentar o resultado da operação.

exemplo de entrada: 1 2 +
soma é 3
'''

print("Digite o 1º número:")
n1 = int (input())

print("Digite o 2º número:")
n2 = int (input())

print("Digite um operador matamático(+, -, * ou /):")
op = input()

if op == "+":
    soma = n1 + n2
    print(f"Soma dos valores: {soma}")
elif op == "-":
    sub = n1 - n2
    print(f"Subtração dos valores: {sub}")
elif op == "/":
    div = n1 / n2
    print(f"Divisão dos valores: {div}")
else:
    multi = n1 * n2
    print(f"Multiplicação dos valores: {multi}")