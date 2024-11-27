#%%


def ex01():
    def entrada():
        """
            Função que recebe e retorna o nome e sobrenome do usuário.
        """
        nome = input("Digite o nome: ")
        sobrenome = input("Digite o sobrenome: ")
        return nome, sobrenome

    nome, sobrenome = entrada()
    print(f"{nome} {sobrenome}")


#%%


def ex02():
    def entrada():
        """
            Função que recebe e retorna o nome e sobrenome do usuário.
        """
        nome = input("Digite o nome e sobrenome: ")
        nome = nome.split()    
        return nome  

    def valida_nome(nome):
        """
            Função que valida o nome e sobrenome do usuário.

            args:
                nome: lista - lista com nome e sobrenome 
        """
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
        """
            Função que recebe e retorna o nome do usuário.
        """
        nome = input("Digite o nome e sobrenome: ")
        nome = nome.split()
        return nome

    nome = entrada()
    print(f"{nome[1].upper()}, {nome[0]}")


#%%


def ex04():
    def entrada():
        """
            Função que recebe a data do usuário e retorna em uma lista de inteiros.
        """
        data = input("Digite a data (DD/MM/AAAA): ")
        data = data.split("/")
        data[0] = int(data[0])
        data[1] = int(data[1])
        data[2] = int(data[2])
        return data
        
    data = entrada()
    print(f"Dia: {data[0]}, Mês: {data[1]}, Ano: {data[2]}")


#%%


def ex05():
    def entrada():
        """
            Função que recebe a data do usuário.
        """
        data = input("Digite a data (DD/MM/AAAA): ")
        data = data.split("/")
        valida_data(data)

    def valida_data(data):
        """
            Função que valida a qunatidade de dias de cada mês.

            args:
                data: lista - lista com dia, mês e ano
        """
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
        """
            Função que recebe e retorna a data do usuário
        """
        data = input("Digite a data (DD/MM/AAAA): ")
        data = data.split("/")
        data[1] = nome_do_mes(data[1])
        return (f"{data[0]} de {data[1]} de {data[2]}")
    
    def nome_do_mes(mes):
        """
            Função que retorna o nome do mês.

            args:
                mes: str - mês em formato de string
        """
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
        """
            Função que recebe e retorna a palavra do usuário.
        """
        palavra = input("Digite uma palavra: ")
        return palavra

    def verifica_palindromo(palavra):
        """
            Função que verifica se a palavra é um palíndromo.

            args:
                palavra: str - palavra a ser verificada
        """
        if palavra == palavra[::-1]:
            print(f"'{palavra}' é um palíndromo")
        else:
            print(f"'{palavra}' não é um palíndromo")

    palavra = entrada()
    verifica_palindromo(palavra)


#%%


def ex08():
    def entrada():
        """
            Função que recebe e retorna a frase do usuário.
        """
        frase = (input("Digite uma frase: ")).lower()
        return frase

    def conta_pares(frase):
        """
            Função que conta a quantidade de vogais na frase.

            args:
                frase: str - frase a ser verificada    
        """
        pares = 0
        for letra in frase:
            if letra in "aeiou":
                pares += 1
        print(f"A frase possui {pares} vogais")

    frase = entrada()
    conta_pares(frase)


#%%


def ex09():
    def entrada():
        """
            Função que recebe e retorna o telefone do usuário.
        """
        fone = input("Digite o telefone: ")
        return fone

    def valida_telefone(fone):
        """
            Função que valida a quantidade de caracteres do telefone.

            args:
                fone: str - telefone a ser validado
        """
        if len(fone) == 11:
            print(f"({fone[:2]}) {fone[2:7]}-{fone[7:]}")
        else:
            print("O número deve possuir 11 dígitos")

    fone = entrada()
    valida_telefone(fone)


#%%


def ex10():
    def entrada():
        """
            Função que recebe e retorna o número do dia do usuário.
        """
        dia = input("Entre com um número: ")
        return dia

    def nome_do_dia(dia):
        """
            Função que retorna o nome do dia.

            args:
                dia: str - número do dia da semana
        """
        match dia:
            case "1": print("Domingo")
            case "2": print("Segunda-feira")
            case "3": print("Terça-feira")
            case "4": print("Quarta-feira")
            case "5": print("Quinta-feira")
            case "6": print("Sexta-feira")
            case "7": print("Sábado")
            case _: print("Número inválido")

    dia = entrada()
    nome_do_dia(dia)


#%%


def ex11():
    def entrada():
        """
            Função que recebe e retorna o CPF do usuário.
        """
        cpf = input("Digite o CPF: ")
        return cpf

    def valida_cpf(cpf):
        """
            Função que valida a quantidade de caracteres do CPF.

            args:
                cpf: str - CPF a ser validado
        """
        if len(cpf) == 11:
            print(f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}")
        else:
            print("O CPF deve possuir 11 dígitos")

    cpf = entrada()
    valida_cpf(cpf)


#%%


def ex12():
    def entrada():
        """
            Função que recebe e retorna a frase do usuário.
        """
        frase = input("Digite uma frase: ")
        return frase

    def inverte_frase(frase):
        """
            Função que inverte a frase.

            args:
                frase: str - frase a ser invertida
        """
        frase_invertida = ""
        for letra in frase:
            frase_invertida = letra + frase_invertida
        print(frase_invertida)

    frase = entrada()
    inverte_frase(frase)


#%%


def ex13():
    def entrada():
        """
            Função que recebe e retorna a frase do usuário.
        """
        frase = input("Digite uma frase: ")
        return frase

    frase = entrada()
    print(frase[::-1])


#%%


def ex14():
    def entrada():
        """
            Função que recebe e retorna a frase do usuário.
        """
        frase = input("Digite uma frase: ")
        return frase

    frase = entrada()
    print(f"Cinco primeiros: {frase[:5]}")
    print(f"Cinco últimos: {frase[-5:]}")


#%%


def ex15():
    def entrada():
        """
            Função que recebe e retorna os dados do usuário.
        """
        dados = input("Digite dados separados por ';': ")
        return dados

    def atualiza_dados(dados):
        """
            Função que substitui ';' por ','.

            args:
                dados: str - dados a serem atualizados
        """
        dados = dados.replace(";", ",")
        return dados

    dados = entrada()
    dados_atualizados = atualiza_dados(dados)
    print(dados_atualizados)


#%%


def ex16():
    def entrada():
        """
            Função que recebe e retorna os números do usuário.
        """
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        return n1, n2

    def calcula_media(n1, n2):
        """
            Função que calcula a média de dois números.

            args:
                n1: int - primeiro número
                n2: int - segundo número
        """
        media = (n1 + n2) / 2
        return media

    n1, n2 = entrada()
    media = calcula_media(n1, n2)
    print(f"A média dos números é {media}")


#%%


ex01()
#ex02()
#ex03()
#ex04()
#ex05()
#ex06()
#ex07()
#ex08()
#ex09()
#ex10()
#ex11()
#ex12()
#ex13()
#ex14()
#ex15()
#ex16()
