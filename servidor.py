from xmlrpc.server import SimpleXMLRPCServer

def calcular_entrega(distancia,tarifa_por_quilometro):
    return distancia * tarifa_por_quilometro

servidor = SimpleXMLRPCServer(("localhost", 8003))

servidor.register_function(
    calcular_entrega,
    "calcular_entrega"
)

print("Servidor RPC aguardando solicitações...")

servidor.serve_forever()