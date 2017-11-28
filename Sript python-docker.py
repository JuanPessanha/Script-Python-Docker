#import docker
from subprocess import call, Popen, PIPE
loop = 1

proc = Popen('docker ps -a', stdout=PIPE, shell=True)
(out, err) = proc.communicate()
containers = str(out)
#print(containers)

print('-=-' * 20)
print('Bem Vindo ao script python do Juan')
print('-=-' * 20, '\n')



while loop != 0:
    comando = input('>>> ').lower().strip().split()

#checar como exibir apenas o nome, imagem e status (execução)
    if 'status' in comando:
        if comando[1] in containers:
            call('docker ps -a --filter id={}'.format(comando[1]), shell=False,)
        else:
            print('O container {} não existe'.format(comando[1]))

#adcionar o tempo
    elif 'start' in comando:
        call('docker start {}'.format(comando[1]))
        if comando[1] in containers:
            print('Container {} iniciado'.format(comando[1]))

#Comando que para a execução do container
    elif 'stop' in comando:
        Popen('docker stop {}'.format(comando[1]), shell=False)
        if comando[1] in containers:
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
