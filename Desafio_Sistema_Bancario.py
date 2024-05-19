menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0 
limite = 1000
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor: .2f}\n"
            print("Operação realizada com sucesso!")
        
        else:
            print("Operação não realizada! Valor inválido.")
        
    elif opcao == "2":
        valor = float(input("Informe o valor para o saque: "))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saques= numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação não realizada. Verifique seu saldo.")
            
        elif excedeu_limite:
            print("Operação não realizada! Limite excedido.")
            
        elif excedeu_saques:
            print("Operação não realizada. Limite diário de saques excedido")
            
        elif valor > 0:
            saldo -=valor
            extrato += f"Saque : R${valor:.2f}\n"
            numero_saques += 1
            print("Operação realizada com sucesso!")
            
        else:
            print("Operação não realizada! O valor informado é inválido.")
        
    elif opcao == "3":
        print("\n==========EXTRATO==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===========================")
        
    elif opcao == "0":
        print("Sistema finalizado!")
        break
    
    else:
        print ("Operação inválida, por favor selecione novamente a operação desejada.")