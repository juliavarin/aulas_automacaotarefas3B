#Estrutura de repetição

'''
Utilizado para repetir  uma instrução um determinado numero de vezes
'''
for x in range(1,3):
    nome = input('Digite o nome do aluno: \n')
    nota = int(input('Digite a nota do aluno: \n'))
    if nota >= 6:
        print(nome, "foi aprovado", nota)
    else:
        print(f"{nome} foi reprovado com {nota: .2f}")