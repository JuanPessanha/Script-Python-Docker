# Script-Python-Docker

Trata-se de um script escrito em python 3 com funções previamente definidas para executar comandos, com o objetivo de gerenciamento de containers no Docker.

## Introdução

O código foi desenvolvido e testado em um ambiente local utilizando o Windows 10. Portanto, estas instruções tornarão possível a utilização deste script em sua máquina local.

### Pré-requisitos

Para que o script possa ser utilizado é necessário que sua máquina possua:

```
Python 3 (último release)
```
```
Docker Comunity Edition
```
```
Hyper-v
```

### Instalação

Passos para a instalação dos pré-requisitos:

Python 3:

```
Baixar o último release:

https://www.python.org/downloads/
```

Hyper-V
```
Manual para habilitar a função de virtualização no windows 10 (port):

https://docs.microsoft.com/pt-br/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v
```

Docker

```
Download (eng):

https://store.docker.com/editions/community/docker-ce-desktop-windows
```
```
Criação de imagem e container (eng):

https://docs.microsoft.com/en-us/virtualization/windowscontainers/quick-start/quick-start-windows-10
```
## Executando os comandos

Atualmente o script conta com os seguintes comandos: 
* start
* stop
* status
* exec
* exit

Futuramente novos comandos podem ser adicionados.

### Comando Start

O comando start inicia a execução de um container.

```
start <container_ID>
```
A adição do parâmetro -t no comando indica que o container sera iniciado e depois será automaticamente parado após os segundos informados pelo usuário no comando:

```
start -t <tempo_segundos> <container_ID>
```

Os comandos acima são declarados na função start()
```
def start():
        if 'start' in comando:
            if '-t' in comando:
                call('docker start {}'.format(comando[3]))
                Popen('ping 127.0.0.1 -n {} > nul && docker stop {}'.format(int(comando[2]) + 1, comando[3]),
                      shell=True, stdout=FNULL, stderr=STDOUT)
            else:
                call('docker start {}'.format(comando[1]))
```
Obs.: os tempos de resposta dos pings de loopback levam 1 segundo para retornarem, por isso o comando ping 127.0.0.1 foi usado como um contador de segundos.

### Comando stop

O comando stop para a execução de um container.

```
stop <container_ID>
```

O comando stop é declarado na função stop()
```
def stop():
        if 'stop' in comando:
            call('docker stop {}'.format(comando[1]))
```
### Comando status

O comando status mostra os detalhes de um container, como nome da imagem, se está em execução e seu nome.

```
status <container_ID>
```

O comando status é declarado na função status()
```
def status():
        if 'status' in comando:
            call('docker ps -a --filter id={}'.format(comando[1]), shell=True)
```
 
 ### Comando exec

O comando exec abre o cmd dentro de um container para que possam ser executados comandos dentro deste container.

```
exec <container_ID>
```

O comando exec é declarado na função executar()
```
def executar():
        if 'exec' in comando:
            call('docker exec -it {} cmd'.format(comando[1]), shell=True)
```            
 ### Comando exit

O comando exit interrompe a execução do script.

```
exit <container_ID>
```

O comando exit é declarado na função fechar()
```
def fechar():
        if comando == ['exit']:
            exit()
```

## Adicionar novos comandos no script

O script foi escrito com uma quantidade limitada de comandos, porém novos comandos podem ser posteriormente adicionados. Para que novos comandos possam ser inseridos no script é necessário verificar a documentação CLI do docker e usar os métodos presentes no módulo SUBPROCESS para que o python execute comandos do CMD.

### Criando função

É necessário que se crie uma função para este comando, e nos parâmetros desta função será definida a sua instrução.
```
def novo():
        if 'novo' in comando:
            call('<docker_CLI_comando>', shell=True)
```
### Declarando a função

Após a criação da função novo() é necessário que a mesma seja chamada posteriormente. Para isso vamos acrescentá-la no 'if' que checa o input de comando:

```
#input de comando
    if comando is not None:
        start(), stop(), status(), executar(), fechar(), novo()
```
