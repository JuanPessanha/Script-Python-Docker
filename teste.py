import docker
client = docker.from_env()
containers1 = str(client.containers.list(all)).split()


print(containers1)
comando = input(':').strip().lower().split()
print(comando)

if 'status' in comando[0]:
    if comando[1] + '>,' in containers1 or comando[1] + '>]' in containers1:
        print(client.containers.get(comando[1]))
    else:
        print('container ID not found\n')
        
        
# usando o cmd para realizar as requisições
import subprocess
loop = 1
proc = subprocess.Popen(['hostname'], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
containers = str(out)
print(containers)

while loop != 0:
    comando = input('>>> ').lower().strip().split()

#checar como conseguir todo o container id
    if 'status' in comando:
        subprocess.call(comando[1])
        print('\n')

    elif comando == ['amoeba']:
        print('Olha no que deu\n')

    elif comando == ['exit']:
        exit()

    else:
        print('por favor digite um comando válido\n')

