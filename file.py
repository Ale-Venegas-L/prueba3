import os
from functions import *

while True:
    os.system("cls")
    print("Sistema Gaxplosive")
    print("1. Registrar pedido")
    print("2. Listar pedidos")
    print("3. Buscar pedido por RUT")
    print("4. Imprimir hoja de ruta")
    print("5. Salir")
    opc = opc_Val("opción")
    if opc==1:
        create_Client()
    elif opc==2:
        read()
    elif opc==3:
        rut_Search()
    elif opc==4:
        route()
    elif opc ==5:
        print("Gracias por su confianza! ╰(*°▽°*)╯")
        break
