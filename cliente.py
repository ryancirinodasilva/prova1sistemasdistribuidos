from xmlrpc.client import ServerProxy

servidor = ServerProxy("http://localhost:8003/")

resultado = servidor.calcular_entrega(8,3)

print("Valor da entrega:", resultado)