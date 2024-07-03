import time, csv
comunas = ("La Granja", 
           "La Pintana",
           "San Ramón")

values = {"5k":12500,
          "15k":25500}

system = [[ "RUT","Nombre", "Dirección", "Comuna", "5kg", "15kg", "Total"]]
from validators import *

def create_Client():
    client = []
    rut = RUT_val()
    client.append(rut)
    name = Name_Val()
    client.append(name)
    dirc = dir_Val()
    client.append(dirc)
    comun = comun_Val()
    client.append(comun)
    print("Si no desea ninguna, deberá ingresar 0")
    val1 = opc_Val("cantidad (5k)")
    val2 = opc_Val("cantidad(15k)")
    client.append(val1)
    client.append(val2)
    total = val1*values["5k"]+val2*values["15k"]
    client.append(total)
    system.append(client)

def read():
    if len(system)==1:
        print("No existen pedidos! Registre y vuelva")
        time.sleep(1)
    else:
        for i in system:
            print(i)
            time.sleep(1)

def rut_Search():
    if len(system)==1:
        print("No existen pedidos! Registre y vuelva")
        time.sleep(1)
    else:
        rut = RUT_val()
        s = search(rut)
        print(system[s])

def route():
    commn = comun_Val()
    i = search(commn)
    with open("ruta.csv", "x") as file:
        file.writable(i)
