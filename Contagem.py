import time
def definir_prog():
    '''program = input('Insira um nome para essa programação\n')
    QE = int(input('Quantos exercícios voce quer fazer?\n'))
    exercicios = []
    for i in range(0, QE):
        nome = input('Insira o nome do exercício:\n')
        print('insira o tempo:')
        m = int(input('Minutos: '))
        s = int(input('Segundos: '))
        tempo = []
        tempo.append(m)
        tempo.append(s)
        exercicios.append(nome)
        exercicios.append(tempo)
        ciclo = int(input('Quantos ciclos de repetição?\n'))
    print('Os exercícios são {}'.format(exercicios))#teste'''
    exercicios = []
    exercicios.append('frog')
    exercicios.append([0, 15])
    gravar(exercicios)


def iniciar_prog():
    abrir_arq()


def cronometro():

    for m in range(0,60):
        for s in range(0,60):
            time.sleep(1)
            print('Relógio {}:{}'.format(m, s))
            lista = []
            lista.append(m)
            lista.append(s)
            print(lista)
            if lista == [0, 5]:#parametros de tempo extraídos da lista do arquivo texto
                break
        if lista == [0, 5]:#repete-se para quebrar o ciclo externo
            break


def gravar(exercicios):
    exercicios = str(exercicios)
    file = open('programacao.txt', 'a')
    file.writelines(exercicios)
    file.close()

def abrir_arq():
    #lista = []
    file = open('programacao.txt', 'r')
    print(file.readlines())
    #lista.append(file.readlines())
    file.close()
    #return lista

def menu():
    opcao = input('1- Definir programação\n'
                  '2- Iniciar programação\n'
                  '3- Cronometro\n')

    if opcao == '1':
        definir_prog()
        print()
        menu()
    if opcao == '2':
        iniciar_prog()
        print()
        menu()
    if opcao == '3':
        cronometro()
        print()
        menu()
    else:
        print('Erro')

#Main program
menu()