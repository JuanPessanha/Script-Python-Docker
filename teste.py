import subprocess
loop = 1


while loop != 0:
    comando = input('>>> ').lower().strip().split()

#checar como conseguir todo o container id
    def start():
        if 'start' in comando[0]:
            if '-t' in comando[1]:
                print('tempo')
            else:
                subprocess.call('hostname')

    def stop():
        if 'stop' in comando:
            print('Olha no que deu')

    def status():
        if 'status' in comando:
            print('status')

    def executar():
        if 'exec' in comando:
            print('Digite seu comandinho')
     
    def fechar():
        if comando == 'exit':
            exit()

    if comando is not None:
        start(), status(), stop(), fechar(), executar()
