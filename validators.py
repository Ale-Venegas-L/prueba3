import time, csv
comunas = ("La Granja", 
           "La Pintana",
           "San Ramón")

values = {"5k":12500,
          "15k":25500}

system = [[ "RUT","Nombre", "Dirección", "Comuna", "5kg", "15kg", "Total"]]

def opc_Val(nro):
    while True: 
        try:
            opc = int(input("Ingrese "+ nro+": "))
            return opc
        except:
            print("Debe ingresar un número")
            time.sleep(1)

def search(look):
    try:
        for i in system:
            for n in i:
                n.index(look)
    except:
        print("Parece no existir")

def RUT_val():
    try:
        while True:
            rut = int(input("Ingrese RUT, sin puntos, ni guion (pero sí digito verificador): "))
            if len(str(rut))==9:
                return rut
            else:
                print("Error, debe ingresar un RUT valido")
    except:
        print("Debe ingresar un RUT válido, sin puntos ni guion")

def Name_Val():
    while True:
        name = input("Ingrese nombre: ")
        if len(name)>=2 and name.isalpha():
            return name
        else:
            print("Debe ingresar un nombre váido")

def dir_Val():
    while True:
        print("Deberá ingresar nombre de la calle y número del domicilio por separado")
        dir = input("Ingrese calle: ")
        if len(dir)>=5 and dir.isalpha:
            nro = opc_Val("número de domicilio")
            dir = dir + " " + str(nro)
            return dir
        else:
            print("Debe ser una dirección válida")


def comun_Val():
    while True:
        print("Comunas disponibles: \n La Granja (1) \n La Pintana (2) \n San Ramón (3)")
        opc = opc_Val("opción")
        if opc ==1:
            return comunas[0]
        elif opc ==2:
            return comunas[1]
        elif opc == 3:
            return comunas[2]
        else:
            print("Opción inválida")
