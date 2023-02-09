menu = '''
    Olá, selecione a opção:
    
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair

=> '''

saldo = 0
limite = 500
operacoes = []
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    opcao = int(input(menu))
        
    if opcao == 1:
        
        print('-----------------DEPÓSITO-----------------')
        valor_deposito = int(input('Informe qual o valor do depósito em reais:  '))
        
        if valor_deposito <= 0:
            print('Insira um valor válido')
            
        else:
            
            saldo += valor_deposito
            
            print(f'''
Depósito realizado com sucesso!
Seu saldo atual é R$ {saldo:.2f}
                  ''')
            
            """ adicionar ao extrato """
            operacoes.append({'Tipo': 'Depósito', 'Valor': valor_deposito})
        
    elif opcao == 2:
        
        if numero_saques >= LIMITE_SAQUES:
            
            print('Você já realizou a quantidade limite de saques diário.')
            continue
        
        else:
            
            print('-----------------SAQUE-----------------')
            print(f'Seu saldo atual é {saldo}')
            valor_saque = int(input('Informe qual valor deseja sacar:  '))
        
        if valor_saque > saldo:
            
            print('Saldo insuficiente.')
            
        else:
            
            if valor_saque > limite:
                print('Valor que deseja sacar ultrapassa limite diário.')
                
            else:
                
                saldo -= valor_saque                    
                print('Saque realizado, retire o dinheiro na boca do caixa.')
                print(f'Saldo atual {saldo}')
                numero_saques += 1
                """ adicionar ao extrato """
                operacoes.append({'Tipo': 'Saque', 'Valor': valor_saque})
                
                
    elif opcao == 3:
        
        print('-----------------EXTRATO-----------------')
        for i in operacoes:
            print(i)
        print(f'Seu saldo atual é {saldo:.2f}.')
        
    elif opcao == 0:
        
        break
    
    else:
        
        print('Opção inválida!')