def menu():
    menu = """

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova Conta
    [5] Lista de Contas
    [6] Novo Usuário

    [0] Sair
    => """
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor: .2f}\n"
        print("\n Operação realizada com sucesso!")
        
    else:
        print("\n Operação não realizada! Valor inválido.")
        
    return saldo, extrato


def sacar (*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    
    if excedeu_saldo:
        print("\n Operação não realizada. Verifique seu saldo.")
        
    elif excedeu_limite:
        print("\n Operação não realizada! Limite excedido.")
        
    elif excedeu_saques: 
        print("\n Operação não realizada. Limite diário excedido")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f} \n"
        numero_saques += 1
        print("\n Operação realizada com sucesso!")
        
    else:
        print("\n Operação não realizada! O valor informado é inválido.")
        
    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    print("\n==========EXTRATO==========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\n Saldo: R$ {saldo:.2f}")
    print("===========================")
    
    
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número):")
    usuario = filtrar_usuario (cpf, usuarios)
    
    if usuario:
        print("CPF e Usuário já cadastrato!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe sua data de nascimento: ")
    endereco = input("Informe o endereço (logradouro, n° - bairro - cidade/Estado): ")
    
    usuarios.append({"nome": nome, "data_nascimento":data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrato, fluxo de criação de conta encerrado!")
    
    
def listar_contas(contas):
    for conta in contas: 
        linha = f"""
            Agência: {conta["agencia"]}
            C/C: {conta["numero_conta"]}
            Titular: {conta["usuario"]["nome"]}
        
        """
        print("="*100 + linha)
                
        
def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 1000
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True:
        opcao = menu()
        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
            
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "2":
            valor  = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
            )
        
        elif opcao == "3":
            exibir_extrato(saldo, extrato = extrato)
            
        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
                
        elif opcao == "5":
            listar_contas(contas)
            
        elif opcao == "6":
            criar_usuario(usuarios)
            
        elif opcao == "0":
            print("Obrigado por usar nosso sistema bancário. Até a prómima!\n \n")
            break
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
            


main()        
    
