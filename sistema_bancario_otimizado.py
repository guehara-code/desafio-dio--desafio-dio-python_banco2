#endereco string
#logradouro, nro - bairro - cidade/estado

#usuario = ["nome", "data_nascimento", "cpf", "endereco"]
lista_usuarios = [] #lista de usuarios

#conta = ["agencia", "conta", "usuario"]
lista_contas = []

def saque(*, saldo, valor_saque, extrato, limite, numero_saques, limite_saques):
    #argumentos por nome keyword

    if (numero_saques < 3 and valor_saque <= 500):
        if (saldo - valor_saque >=0):
            saldo -= valor_saque
            numero_saques += 1
            extrato += f"Saque    R${valor_saque:.2f}\n"
            print(f"Saque realizado com sucesso. Saldo atual é de: R${saldo:.2f}")
        else:
            print("Saldo insuficiente. Operação não realizada.")
    else:
        if (numero_saques >= 3):
            print(f"Numero de {limite_saques} saques diários excedido. Operação não realizada.")
        elif (valor_saque > 500):
            print(f"Limite máximo de R${limite:.2f} por saque excedido. Operação não realizada.")     

    return saldo, extrato, numero_saques

def deposito(saldo, valor_deposito, extrato, /):
    #argumentos por posicao
    
    if (valor_deposito>0):
        saldo += valor_deposito
        extrato += f"Depósito R${valor_deposito:.2f}\n"
        print(f"Depósito realizado com sucesso. Saldo atual é de: R${saldo:.2f}")
    else:
        print("Valor de deposito não permitido. Operação não realizada.")

    return saldo, extrato

def imprimir_extrato(saldo, /, *, extrato):
    #saldo por posicao e extrato por keyword
    print("Extrato")
    print(extrato)
    print("---------------------")
    print(f"Saldo    R${saldo:.2f}")

def cadastrar_usuario(lista_usuarios):
    cpf = input("Informe CPF do novo usuário: ")
    for usuario in lista_usuarios:
        if cpf == usuario["cpf"]:
            print("Usuario existente. Não pode ser cadastrado novamente.")
            return
    nome = input("Informe nome do novo usuario: ")
    data_nascimento = input("Informe data de nascimento do novo usuário: ")
    endereco = input("Informe endereco do novo usuario: ")
    lista_usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário Criado")


def cadastrar_conta(agencia, conta, lista_usuarios, lista_contas):
    cpf = input("Informe CPF usuário: ")
    for usuario in lista_usuarios:
        if cpf == usuario["cpf"]:
            print("Usuário Encontrado.")
            lista_contas.append({"agencia": agencia, "conta": conta, "cpf": cpf})
            print("Conta Criada.")
            return lista_contas
        else:
            print("Usuário não encontrado. Criação de conta não pode ser realizada.")
            return lista_contas


menu = """

[d]  Depositar
[s]  Sacar
[e]  Extrato
[nu] Novo Usuário
[lu] Listar Usuários
[nc] Nova Conta
[lc] Listar Contas
[q]  Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = "0001"

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        valor_deposito = float(input("Qual o valor a ser depositado?: "))
        # if (valor_deposito>0):
        #     saldo += valor_deposito
        #     extrato += f"Depósito R${valor_deposito:.2f}\n"
        #     print(f"Depósito realizado com sucesso. Saldo atual é de: R${saldo:.2f}")
        # else:
        #     print("Valor de deposito não permitido. Operação não realizada.")
        saldo, extrato = deposito(saldo, valor_deposito, extrato)
    
    elif opcao == "s":
        print("Saque")
        valor_saque = float(input("Qual o valor a ser sacado?: "))
        # if (numero_saques < 3 and valor_saque <= 500):
        #     if (saldo - valor_saque >=0):
        #         saldo -= valor_saque
        #         numero_saques += 1
        #         extrato += f"Saque    R${valor_saque:.2f}\n"
        #         print(f"Saque realizado com sucesso. Saldo atual é de: R${saldo:.2f}")
        #     else:
        #         print("Saldo insuficiente. Operação não realizada.")
        # else:
        #     if (numero_saques >= 3):
        #         print(f"Numero de {LIMITE_SAQUES} saques diários excedido. Operação não realizada.")
        #     elif (valor_saque > 500):
        #         print(f"Limite máximo de R${limite:.2f} por saque excedido. Operação não realizada.")    
        saldo, extrato, numero_saques = saque(saldo=saldo, valor_saque=valor_saque, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)  

    elif opcao == "e":
        # print("Extrato")
        # print(extrato)
        # print("---------------------")
        # print(f"Saldo    R${saldo:.2f}")
        imprimir_extrato(saldo, extrato=extrato)

    elif opcao == "nu":
        print("Cadastrar novo usuário")
        cadastrar_usuario(lista_usuarios)
    
    elif opcao == "lu":
        print("Listar Usuários")
        print(lista_usuarios)
    

    elif opcao == "nc":
        print("Cadastrar nova conta")
        conta = len(lista_contas) + 1
        cadastrar_conta(AGENCIA, conta, lista_usuarios, lista_contas)

    elif opcao == "lc":
        print("Listar Contas")
        print(lista_contas)

    elif opcao == "q":
        break