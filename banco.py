menu = """Olá, Informe a operação que deseja realizar
      [d] Depositar
      [s] Sacar
      [e] Extrato
      [q] Sair
      
      """
saldo = 0.0
extrato = ""
saque = 0.0
deposito = 0.0
numero_saques = 0
saque_total_diario = 0.0
LIMITE_SAQUE = 500.00
QTDE_LIMITE_SAQUES = 3
LIMITE_DIARIO = 1500.0

while True:
    opcao = input(menu)
    
    if opcao =="d":
        print("Informe o valor a ser depositado:")
        print(f"Seu saldo atual é de: R${saldo}")
        deposito = float(input())
        if  deposito > 0.0:
            saldo += deposito
            extrato += f"Valor deposito: R${deposito}\n"
            print(f"Seu saldo atual é de: R${saldo}")
        else:
            print("Valor invalido")
    elif opcao == "s":
        print(f"Seu saldo atual é de:R${saldo}")
        saque = float(input("Informe o valor a ser sacado:"))
        excedeu_saldo = saque > saldo
        excedeu_limite = saque > LIMITE_SAQUE
        excedeu_saques = numero_saques > QTDE_LIMITE_SAQUES
        excedeu_limite_diario = saque_total_diario > LIMITE_DIARIO
        
        if excedeu_saldo:
            print(f"Saque falhou, sem saldo suficiente. Saldo atual é de: R${saldo}") 
        elif excedeu_limite:
            print(f"Saque falhou, saldo maior que o limite. Limite atual R${LIMITE_SAQUE}")
        elif excedeu_saques:
            print(f"Saque falhou, limite de saques execidos. Limite atual é de {QTDE_LIMITE_SAQUES} saques diarios")
        elif excedeu_limite_diario:
            print(f"Saque falhou, valor limite de saques execidos. Limite atual é de R${LIMITE_DIARIO}  diarios")
        elif saque >0:
            saldo -= saque
            print(f"Salque de R${saque} efetuado com sucesso!") 
            print(f"Seu saldo atual é de:R${saldo}")
            extrato += f"Valor sacado: R${saque}\n"
            numero_saques += 1
            saque_total_diario +=saque
        else:
            print(f"Saque falhou,verifique o regras e condiçoes")
    elif opcao == "e":
        print("\n ====================Extrato====================")
        print("Nao foram realizadas transacoes no perido."if not extrato else extrato) 
        print(f"\nSaldo atual é de R${saldo}")     
        print("\n ========================================")  
    elif opcao == "q":
        break
