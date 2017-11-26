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

