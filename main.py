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
        return nome  

    def valida_nome(nome):
        if (len(nome[0]) < 2):
            print("O nome deve possuir ao menos 2 caracteres.")
            return
        elif (len(nome[1]) < 2):
            print("O sobrenome deve possuir ao menos 2 caracteres.")
            return
        else:
            print(f"{nome[0]} {nome[1]}")

    nome = entrada()
    valida_nome(nome)


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
        data[0] = int(data[0])
        data[1] = int(data[1])
        data[2] = int(data[2])
        print(f"Dia: {data[0]}, Mês: {data[1]}, Ano: {data[2]}")

    entrada()


#%%


def ex05():
    def entrada():
        data = input("Digite a data (DD/MM/AAAA): ")
        data = data.split("/")
        valida_data(data)

    def valida_data(data):
        match data[1]:
            case "01" | "03" | "05" | "07" | "08" | "10" | "12":
                if (int(data[0]) > 31):
                    print("Data inválida")
                else:
                    print("Data válida")
            case "04" | "06" | "09" | "11":
                if (int(data[0]) > 30):
                    print("Data inválida")
                else:
                    print("Data válida")
            case "02":
                if (int(data[2]) % 4 == 0):
                    if (int(data[0]) > 29):
                        print("Data inválida")
                    else:
                        print("Data válida")
                else:
                    if (int(data[0]) > 28):
                        print("Data inválida")
                    else:
                        print("Data válida")
            case _:
                print("Data inválida")

    entrada()


#%%


def ex06():
    def entrada():
        data = input("Digite a data (DD/MM/AAAA): ")
        data = data.split("/")
        data[1] = nome_do_mes(data[1])
        return (f"{data[0]} de {data[1]} de {data[2]}")
    
    def nome_do_mes(mes):
        match mes:
            case "1": return "janeiro"
            case "2": return "fevereiro"
            case "3": return "março"
            case "4": return "abril"
            case "5": return "maio"
            case "6": return "junho"
            case "7": return "julho"
            case "8": return "agosto"
            case "9": return "setembro"
            case "10": return "outubro"
            case "11": return "novembro"
            case "12": return "dezembro"
            case _: print("Mês inválido ")

    data = entrada()
    print(data)


#%%


def ex07():
    def entrada():
        palavra = input("Digite uma palavra: ")
        return palavra

    def verifica_palindromo(palavra):
        if palavra == palavra[::-1]:
            print(f"'{palavra}' é um palíndromo")
        else:
            print(f"'{palavra}' não é um palíndromo")

    palavra = entrada()
    verifica_palindromo(palavra)


#%%


#ex01()
#ex02()
#ex03()
#ex04()
ex05()
#ex06()
#ex07()
