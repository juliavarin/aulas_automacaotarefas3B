'''
Crie um programa que recebe como entrada dois números reais. 
O programa deve imprimir as quatro operações matemáticas entre os dois números (soma, subtração, divisão e multiplicação)
'''
print("Digite o 1º número:")
n1 = float (input())

print("Digite o 2º número:")
n2 = float (input())

soma = n1 + n2
sub = n1 - n2
div = n1 / n2
multi = n1 * n2

print(f"\nSoma: {soma}\nSubtração: {sub}\nDivisão: {div}\nMultiplicação: {multi}")
