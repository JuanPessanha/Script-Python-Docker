from os import devnull
from subprocess import call, Popen, STDOUT

loop = 1

print('-=-' * 30)
print('Scrip Python para gerenciamento do Docker')
print('-=-' * 30, '\n')

#iniciando estrutura de repetição
while loop != 0:
    comando = input('>>> ').lower().strip().split()
    FNULL = open(devnull, 'w')

#funções de comando
    def start():
        if 'start' in comando:
            if '-t' in comando:
                call('docker start {}'.format(comando[3]))
                Popen('ping 127.0.0.1 -n {} > nul && docker stop {}'.format(int(comando[2]) + 1, comando[3]),
                      shell=True, stdout=FNULL, stderr=STDOUT)
            else:
                call('docker start {}'.format(comando[1]))

    def stop():
        if 'stop' in comando:
            call('docker stop {}'.format(comando[1]))

    def status():
        if 'status' in comando:
            call('docker ps -a --filter id={}'.format(comando[1]), shell=True)

    def executar():
        if 'exec' in comando:
            call('docker exec -it {} cmd'.format(comando[1]), shell=True)

    def fechar():
        if comando == ['exit']:
            exit()

#input de comando
    if comando is not None:
        start(), stop(), status(), executar(), fechar()

