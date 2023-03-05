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
        
        else:
            print('Dados incorretos')
    else:
        print('Opção inválida')