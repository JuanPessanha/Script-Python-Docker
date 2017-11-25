loop = 1

print('-=-' * 20)
print('Bem Vindo ao script python do Juan')
print('-=-' * 20, '\n')

while loop != 0:
    comando = input('>>> ')

    if comando == 'ok':
        print('Rammus\n')

    elif comando == 'amoeba':
        print('Olha no que deu\n')

    elif comando == 'exit':
        exit()

    else:
        print('favor digite um comando válido\n')
