def menu():
    menu = """
==========MENU==========
[1] Depositar
[2] Sacar
[3] Extrato
-
[4] Registrar Cliente
[5] Criar Conta Corrente
-
[6] Listar Clientes
[7] Listar Contas
-
[0] Sair
========================
=> """
    return input(menu)

def registrar_cliente(usuarios):

    cpf = (str(input("Digite seu cpf (apenas números): ")))
    
    #isdigit() checa se o valor inserido possúi apenas números
    if cpf.isdigit() == False:
        print("Caractéres inválidos, por favor insira apenas números.")
        return usuarios
    
    #Checagem de CPF já existente registrado
    for chave in usuarios:
        if chave == cpf:
            print("CPF Já registrado, finalizando sessão...")
            return usuarios
    
    nome = (str(input("Digite seu nome completo: ")))

    data_nascimento = (str(input("Digite sua data de nascimento (dd-mm-aaaa): ")))

    endereco = (str(input("Digite seu endereço (logradouro - nro - bairro - cidade/sigla estado): ")))

    #Todas as informações recebidas são armazenadas dentro de um dicionário no dicionário usuarios
    #onde a chave deste dicionário novo é o CPF
    
    usuarios[cpf] = {"Nome": nome, "Data de nascimento": data_nascimento, "Endereço": endereco}

    print(f"Cliente {nome} registrado com sucesso!")

    #A função retorna as alterações para o dicionário usuarios
    return usuarios

def criar_conta_corrente(usuarios, contas, n_contas, N_AGENCIA):
    
    cliente = (str(input("Informe o CPF do cliente a ser vinculado nesta conta (apenas números): ")))
    
    #Checagem do CPF e se o Cliente existe
    if cliente.isdigit() == False:
        print("Caractéres inválidos, por favor insira apenas números.")
        return contas, n_contas
    if usuarios.get(cliente) == None:
        print("Cliente não encontrado")
        return contas, n_contas
    
    nome = usuarios[cliente]["Nome"]
    n_contas += 1
    contas[n_contas] = {"Agência": N_AGENCIA, "Cliente": f"{nome} ({cliente})"}
    
    print(f"Conta Nro '{n_contas}' criada com sucesso no nome de {nome}")
    
    #A função retorna as alterações para o dicionário contas e também a contagem do numero de contas
    return contas, n_contas

def listar_clientes(usuarios):
    for chave in usuarios:
        print(f"CPF: {chave} | Nome: {usuarios[chave]["Nome"]} | Data de nascimento: {usuarios[chave]["Data de nascimento"]} | Endereço: {usuarios[chave]["Endereço"]} | \n")
    
    #Essa função não retorna nada
    return None

def listar_contas(contas):
    for chave in contas:
        print(f"Agência: {contas[chave]["Agência"]} | Nro: '{chave}' | Cliente: {contas[chave]["Cliente"]} |\n")
    #Essa função não retorna nada
    return None

def deposito(saldo, extrato, /):
    
    valor = float(input("Informe o valor do depósito: "))

    #Verificando se o valor digitado é válido, o depósito é efetuado
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")

    #Adicionado o retorno da função
    return saldo, extrato

def saque(*, saldo, extrato, limite, numero_saques, LIMITE_SAQUES):
    
    valor = float(input("Informe o valor do saque: "))
    
    #Checagens do saldo e seus limites, retorna verdadeiro ou falso para checagem de condições posteriormente
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    #Caso uma exceção seja atingida o programa retornará uma mensagem informando tal exceção
    if excedeu_saldo:
        print("Operção falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    #Passando a verificação de exceções a função efetua o saque também verificando se o valor digitado é válido
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    #Adicionado o retorno da função
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):

    #No fim das funções anteriores ao realizar a movimentação na conta, era adicionada uma linha contendo o valor no extrato,
    #essas movimentações serão exibidas aqui, junto do saldo final
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato) #If not verificando se há ou não extratos
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    
    #Essa função não retorna nada
    return None
    
def main():

    usuarios = {}
    contas = {}
    n_contas = 0
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    N_AGENCIA = "0001"

    while True:

        opcao = menu()
    
        #É necessário reatribuir os valores com o retorno da função ( valor = funcao() ) para que as alterações sejam aplicadas
        #exceto no extrato e listas, onde nada é alterado e apenas exibido
        if opcao == "1":
            saldo, extrato = deposito(saldo, extrato)

        elif opcao == "2":
            saldo, extrato, numero_saques = saque(saldo=saldo, extrato=extrato, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            usuarios = registrar_cliente(usuarios)

        elif opcao == "5":
            contas, n_contas = criar_conta_corrente(usuarios, contas, n_contas, N_AGENCIA)

        elif opcao == "6":
            listar_clientes(usuarios)

        elif opcao == "7":
            listar_contas(contas)

        elif opcao == "0":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()