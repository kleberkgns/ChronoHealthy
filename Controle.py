import time

# Método OK
def definir_prog():
    print('\n'+8*'=--='+'\n')
    programacao = []
    exercicios = []
    cond1 = True
    while cond1 == True:
        programaNome = str(input('Programa: '))
        cond2 = True
        while cond2 == True:
            print(32*'-'+'\n')
            exercicioNome = str(input('Exercicio: '))
            print('Tempo de exercicio')
            m = int(input('Minutos: '))
            s = int(input('Segundos: '))
            exercicios.append(exercicioNome)
            exercicios.append([m, s])
            print(32*'-'+'\n')
            validacao = False
            while validacao != True:
                print('Deseja adicionar mais exercicios?')
                escolha = int(input('1 - Sim\n'
                                    '2 - Não\n'))
                if escolha != 1 and escolha != 2:
                    print('Escolha inválida!\n'+32*'-')
                    validacao = False
                else:
                    if escolha == 1:
                        cond2 = True
                    if escolha == 2:
                        cond2 = False
                    validacao = True
            cond1 = False
        programacao.append(programaNome)
        programacao.append(exercicios)
    for i in range(0, len(programacao)): # Verificação do que irá ser gravado no arquivo
        print(programacao[i])

    gravar(programacao)

def iniciar_prog():
    abrir_arq()

def cronometro():

    for m in range(0,60):
        for s in range(0,60):
            time.sleep(1)
            print('Relógio {}:{}'.format(m, s))# Teste
            lista = []
            lista.append(m)
            lista.append(s)
            print(lista)
            if lista == [0, 5]:#parametros de tempo extraídos da lista do arquivo texto
                break
        if lista == [0, 5]:#repete-se para quebrar o ciclo externo
            break

def gravar(programacao):
    exercicios = str(programacao)
    file = open('programacao.txt', 'a')
    file.writelines(exercicios+'\n') # Grava uma programação por linha no arquivo
    file.close()

def abrir_arq():
    file = open('programacao.txt', 'r')
    print(file.readlines())
    file.close()

def textoMenu():
    opcao = input(32*'='+'\n'+
                  '1- Definir programação\n'
                  '2- Iniciar programação\n'
                  '3- Cronometro\n'
                  '-> ')
    return opcao

def menu():
    opcao = textoMenu()
    while opcao != 1 and opcao != 2 and opcao != 3:

        if opcao == '1':
            definir_prog()
            print()
            opcao = textoMenu()

        if opcao == '2':
            iniciar_prog()
            print()
            opcao = textoMenu()

        if opcao == '3':
            cronometro()
            print()
            opcao = textoMenu()

        else:
            print(15*'='+'\nOpção inválida!\n'+15*'=')
            print('\nInsira uma opção do Menu abaixo:\n')
            opcao = textoMenu()

# Método que recebe uma condição booleana True para executar um menu de escolha binária (Sim ou não)

def escolha(cond):
    while cond == True:
        escolha = int(input('1 - Sim\n'
                            '2 - Não\n'))
        if escolha != 1 and escolha != 2:
            print('Escolha inválida!')
        else:
            if escolha == 1:
                cond = True
            if escolha == 2:
                cond = False
        print()
    return cond


# Main Program
menu()