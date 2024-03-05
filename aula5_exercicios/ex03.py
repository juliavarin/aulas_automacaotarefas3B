'''
Crie um programa que execute repetidamente o programa do ex2, 
após apresentação do resultado o programa deve perguntar se o usuário deseja continuar, se a resposta for N (não) o programa deve terminar.
'''
res = True
while res == True:
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

    print("Pretende continuar:")
    resposta = str(input())

    if resposta == "s":
        res = True
    elif resposta == "n":
        break


