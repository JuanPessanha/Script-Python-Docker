#import docker
from subprocess import call, Popen
loop = 1

print('-=-' * 20)
print('Bem Vindo ao script python do Juan')
print('-=-' * 20, '\n')

while loop != 0:
    comando = input('>>> ').lower().strip().split()

#checar como exibir apenas o nome, imagem e status (execução)
    if 'status' in comando:
        call('docker ps -a --filter id={}'.format(comando[1]), shell=False,)
        print('\n')

#adcionar o tempo
    elif 'start' in comando:
        call('docker start {}'.format(comando[1]))
        print('Container {} iniciado'.format(comando[1]))

#Comando que para a execução do container
    elif 'stop' in comando:
        Popen('docker stop {}'.format(comando[1]), shell=False)
        print('Container {} parado'.format(comando[1]))

#comando que abre o cmd dentro de um container para execução de comandos
    elif 'exec' in comando:
        call('docker exec -it {} cmd'.format(comando[1]), shell=True)

#Sair do Script
    elif comando == ['exit']:
        exit()

#comando desconhecido
    else:
        print('favor digite um comando válido\n')
