#função 1
def CalcularAreaTriangulo(base, altura):
    area = (base * altura) / 2
    return area

#função 2
def login (usuario, senha):
    if usuario == 'admin' and senha == '123':
        return True
    else:
        return False

#chamar a função
#print(login("admin", '123'))

#area = CalcularAreaTriangulo(100,50)
#print('A area do triangulo é ', area)