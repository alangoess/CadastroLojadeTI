import sqlite3
from time import sleep

banco = sqlite3.connect('cadastro_clientes.db')
cursor = banco.cursor()

print('Olá, seja bem-vindo à Clínica do Computador!')
sleep(1)

opcoes = input('Escolha as opções abaixo: \n [1] Avaliação de Máquina \n [2] FeedBack \n ')

if opcoes == '2':

  feedback = input('Digite seu feedback')

else:
    cadastro = input('Você já possui cadastro? \n [1] Sim [2] Não \n ')
if  cadastro == '1':
    
    NomeCliente = input('Qual é o nome do cliente?')
    problema = input('Qual problema a sua máquina está apresentando? ')
    mexeu = input('A máquina já foi aberta alguma vez? ')
    vezes_que_aconteceu = input('Já aconteceu esse tipo de problema alguma vez? ')
    
    sleep(1)

    print('Entendi... O problema apresentado foi anotado! Você terá que deixar a sua máquina com o técnico. O prazo da análise dura em torno de 5 dias úteis.')

    confirmacao = input('Deseja confirmar a Analise da sua máquina? ')
    if confirmacao == 'sim':
        cursor.execute("CREATE TABLE IF NOT EXISTS OrdemDeServiço(Nome text, Problema text, aberta text, Deuproblema text)")
        cursor.execute(f"INSERT INTO OrdemDeServiço VALUES('{NomeCliente}', '{problema}', '{mexeu}', '{vezes_que_aconteceu}')")
        banco.commit()
        
        print('Agendamento feito com sucesso!')
    else:
        print('Que pena, conte para nós o que aconteceu na opção feedback!')


elif cadastro == '2':
    print('Para criar o seu cadastro, precisamos colher algumas informações!')

    Nome = input('Digite o seu nome completo: ')
    Cpf = input('Digite o seu CPF: ')
    Categoria = input('Técnico ou Consumidor Final...')
    print(f"Cadastro criado com sucesso!")
   
    #cursor.execute("DROP TABLE IF EXISTS cadastro")
    cursor.execute("CREATE TABLE IF NOT EXISTS cadastro(Nome text, CPF integer, Categoria text)")
    cursor.execute(f"INSERT INTO cadastro VALUES('{Nome}',{Cpf},'{Categoria}' )")
    banco.commit()


#





 

    


  
    