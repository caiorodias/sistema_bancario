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
        
        endereco = (f'{logradouro}, {nr_casa} - {bairro} - {cidade}/{estado}')
        
        usuario = {'nome': nome, 'data de nascimento': data_formatada, 'CPF': cpf, 'Endereço': endereco}
        contas.append(usuario)
        
        #Criar a conta e agencia e limitar a 2 contas por cpf
        
        print('Conta criada com sucesso!')