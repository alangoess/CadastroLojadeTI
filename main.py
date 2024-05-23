import sqlite3
from time import sleep

print('Olá, seja bem-vindo à Clínica do Computador!')
sleep(1)

opcoes = input('Escolha as opções abaixo: \n [1] Cadastro \n [2] Avaliação de Máquina \n [3] Feedback \n ')

if opcoes == '1':
    print('Para criar o seu cadastro, precisamos colher algumas informações!')

    Nome = input('Digite o seu nome completo: ')
    DataNasc = input('Digite a sua data de nascimento: ')
    Cpf = input('Digite o seu CPF: ')

    print(f"Obrigado pelas informações {Nome}")

elif opcoes == '2':
    problema = input('Qual problema a sua máquina está apresentando? ')
    mexeu = input('Você tentou consertar por conta própria? Se sim, o que você fez? ')
    vezes_que_aconteceu = input('Já aconteceu esse tipo de problema alguma vez? ')

    sleep(1)

    print('Entendi... O problema apresentado foi anotado! Você terá que deixar a sua máquina com o técnico. O prazo da análise dura em torno de 5 dias úteis.')

    confirmacao = input('Deseja confirmar a Analise da sua máquina? ')
    if confirmacao == 'sim':
        print('Agendamento feito com sucesso!')
    else:
        print('Que pena, conte para nós o que aconteceu na opção feedback!')

else:
    feedback = input('Nos informe o seu feedback, garanto que será muito útil para a nossa empresa!')
    print('Muito Obrigado pelo seu feedback, iremos sempre tentar melhorar o nosso atendimento para satisfazer nossos clientes!')    
