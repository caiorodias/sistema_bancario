from datetime import datetime

menu_usuario = """

Olá, selecione a opção desejada:

[1] Abrir conta
[2] Já sou cliente

==>"""

contas = []
AGENCIA = '0001'
nr_conta = 0

while True:
    opcao = int(input(menu_usuario))
    
    if opcao == 1:
                
        cpf = int(input('''
        
Crie sua conta!
        
        
Digite seu CPF (Apenas números):
        '''))
        
        nome = input('''
Digite seu nome completo:             
        ''')
        data_nascimento = input('''
Digite sua data de nascimento (dd/mm/aaaa)                 
        ''')
        data_formatada = datetime.strptime(data_nascimento, '%d/%m/%Y')
        
        #Endereço
        logradouro = input('''
Informe seu endereço
        
Logradouro:
        ''')
        nr_casa = input('''
Número da casa:
        ''')
        bairro = input('''
Bairro:               
        ''')
        cidade = input('''
Cidade:               
        ''')
        estado = input('''
Sigla do estado:               
        ''')
        
        nr_conta += 1
        
        endereco = (f'{logradouro}, {nr_casa} - {bairro} - {cidade}/{estado}')
        
        usuario = {'nome': nome, 'data de nascimento': data_formatada, 'cpf': cpf, 'endereço': endereco, 'numero da conta': nr_conta, 'agencia': AGENCIA}
        contas.append(usuario)
        
        #Criar a conta e agencia e limitar a 2 contas por cpf
        conta_criada = usuario['numero da conta']
        
        print('Conta criada com sucesso!')
        print(f'Agência: {AGENCIA}')
        print(f'Conta: {conta_criada}')
        
    elif opcao == 2:
    
        agencia = input('''
Digite o código da sua agência:                        
''')
        conta = input('''
Digite o código da sua conta:
''')
        if agencia == usuario['agencia'] and conta == str(conta_criada):
    
            print('Login realizado')
            
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
        else:
            print('Dados incorretos')
    else:
        print('Opção inválida')