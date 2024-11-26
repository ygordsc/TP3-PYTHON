#%%

def ex01():
    def entrada():
        nome = input("Digite o nome: ")
        sobrenome = input("Digite o sobrenome: ")
        print(f"{nome} {sobrenome}")

    entrada()

#%%

def ex02():
    def entrada():
        nome = input("Digite o nome e sobrenome: ")
        nome = nome.split()
        if (len(nome[0]) < 2):
            print("O nome deve possuir ao menos 2 caracteres.")
            return
        elif (len(nome[1]) < 2):
            print("O sobrenome deve possuir ao menos 2 caracteres.")
            return
        else:
            print(f"{nome[0]} {nome[1]}")

    entrada()

#%%

def ex03():
    def entrada():
        nome = input("Digite o nome e sobrenome: ")
        nome = nome.split()
        print(f"{nome[1].upper()}, {nome[0]}")

    entrada()

#%%

def ex04():
    def entrada():
        data = input("Digite a data (DD/MM/AAAA): ")
        data = data.split("/")
        print(f"Dia: {data[0]}, Mês: {data[1]}, Ano: {data[2]}")

    entrada()

#%%

def verifica_palindromo(palavra):
    if palavra == palavra[::-1]:
        print(f"'{palavra}' é um palíndromo")
    else:
        print(f"'{palavra}' não é um palíndromo")

palavra = input("Digite uma palavra: ")
verifica_palindromo(palavra)

#ex01()
ex02()
#ex03()
#ex04()

