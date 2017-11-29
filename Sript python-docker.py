from os import devnull
from subprocess import call, Popen, PIPE, STDOUT

loop = 1

print('-=-' * 30)
print('Python Script to Management Docker')
print('-=-' * 30, '\n')


while loop != 0:
    comando = input('>>> ').lower().strip().split()
    FNULL = open(devnull, 'w')


#checar como exibir apenas o nome, imagem e status (execução)
    if 'status' in comando:
        call('docker ps -a --filter id={}'.format(comando[1]), shell=True)

#Iniciar a execução de um container
    elif 'start' in comando:
        if '-t' in comando:
            call('docker start {}'.format(comando[3]))
            Popen('ping 127.0.0.1 -n {} > nul && docker stop {}'.format(int(comando[2]) + 1, comando[3]), shell=True, stdout=FNULL, stderr=STDOUT)
        else:
            call('docker start {}'.format(comando[1]))

#Comando que para a execução do container
    elif 'stop' in comando:
        call('docker stop {}'.format(comando[1]))

#comando que abre o cmd dentro de um container para execução de comandos
    elif 'exec' in comando:
        call('docker exec -it {} cmd'.format(comando[1]), shell=True)

#Sair do Script
    elif comando == ['exit']:
        exit()

#comando desconhecido
    else:
        print('favor digite um comando válido\n')
