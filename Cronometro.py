import time

def agaixamento():
    time.sleep(15)
    print('AGAIXAMENTO')

def cronometro():
    for h in range(0,24):
        for m in range(0,60):
            for s in range(0,60):
                print('Relógio {}:{}:{}'.format(h, m, s))
                time.sleep(1)

#Main program
print('Iniciando:')
cronometro()