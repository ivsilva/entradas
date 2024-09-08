#   aplicação para saber quntas pessoas foram a minha festa
#qtd = []
#people = input("Digite um numero!!!\n ")
#qtd.append(people)
#len(qtd)
#print(str(qtd) + ' Pessoas participaram do seu evento!!!')

#### com while chatgpt

qtd =  [ ]
print('Bem Vindo Ao Sistema de Gestão de Entradas')

while True: 
    people = input('Digite um Numero (Ou "sair" Para Finalizar o Programa)\n')
    if people.lower() == 'sair':
        print('Programa Finalizado, Obrigado. ')

        break

    try:
        qtd.append(int(people))
    except ValueError:
        print('Por Favor, Insira um valor Valido ou "sair" para finalizar') 
               
qtd_pessoas = sum(qtd)
print(f'{qtd_pessoas} Pessoas Participaram Do Seu Evento!!!')    
