import docker
client = docker.from_env()
containers1 = str(client.containers.list(all)).split()
loop = 1

print('-=-' * 20)
print('Bem Vindo ao script python do Juan')
print('-=-' * 20, '\n')

while loop != 0:
    comando = input('>>> ').lower().strip().split()

#checar como conseguir todo o container id
    if 'status' in comando:
        if comando[1] + '>,' in containers1 or comando[1] + '>]' in containers1:
            print(client.containers.get(comando[1]))
        else:
            print('container ID not found\n')

    elif comando == ['amoeba']:
        print('Olha no que deu\n')

    elif comando == ['exit']:
        exit()

    else:
        print('favor digite um comando válido\n')
