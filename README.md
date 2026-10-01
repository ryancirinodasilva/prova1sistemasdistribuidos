# Prova 1 de Sistemas Distribuídos

Nome: Ryan Cirino Da Silva

RA: c6f7900d066d066b12e0e

## Problema da empresa

[Descreva, com suas palavras, o calculo solicitado no enunciado.]
Situação-problema: Uma transportadora cobra uma tarifa por quilômetro. O cliente deve solicitar ao servidor o valor de uma entrega de 8 quilômetros, á tarifa de R$ 3 por quilômetro.

Basicamente o cliente passa ao servidor quanto é os quilômetros sendo 8 e quanto é a tarafa 3.
O servidor Recebe esses dados e processa fazendo 8 X 3, após processar isso ele retorna ao cliente o processamento e o cliente mostra isso ao usuário.

## Arquivos


- servidor.py: recebe a chamada RPC e executa o cálculo.

- -cliente.py: solicita o cálculo ao servidor e mostra a resposta.


## Resultado do teste


[Cole aqui a saída apresentada ao executar o cliente.]

C:\Users\ryanc>
python "C:\Users\ryanc\Downloads\Prova Sis.Dis\cliente.py"
Valor da entrega: 24

## Explicação

1. Em qual programa o cálculo foi executado?
O Cálculo foi executado no servidor.py

2. Qual programa iniciou a solicitação?
O cliente.py inicia a solicitação ao servidor
3. O que aconteceria com o cliente se o servidor estivesse desligado?
O cliente não consegue se conectar apresentando uma mensagem de erro.
Existe um arquivo no repositório que mostra o log de erro, o nome do arquivo é Erro python.

