import os
import random
from datetime import datetime
from analizador.comandos.login import Login
from analizador.comandos.mkdisk import Mkdisk
from analizador.comandos.mbr import Mbr
from analizador.comandos.partition import Partition
from analizador.comandos.rmdisk import Rmdisk
from analizador.comandos.fdisk import Fdisk

global comando, script, usuario_actual
usuario_actual = ""

def comando_activar(valor):
    global comando, script
    comando = valor

    if (comando == "mkdisk"):
        script = Mkdisk()
    elif (comando == "rmdisk"):
        script = Rmdisk()
    elif (comando == "fdisk"):
        script = Fdisk()
    elif (comando == "login"):
        script = Login()
    elif (comando == "logout"):
        pass

def comando_ejecutar(parametro, valor):
    global comando, script, usuario_actual
    #COMANDO MKDISK
    if (comando == "mkdisk"):
        if (parametro == 'size'):
            script.setSize(int(valor))
        elif (parametro == 'path'):
            script.setPath(valor)
        elif (parametro == 'fit'):
            script.setFit(valor)
        elif (parametro == 'unit'):
            script.setUnit(valor)
        elif (parametro == "ejecutar"):
            if (script.errors == 0):
                #crear un arhivo vacio
                size_file = script.getSize()
                if (script.getUnit() == "M"):
                    size_file = size_file * 1024
                with open(script.getPath(), 'wb') as archivo:
                    for i in range(0, size_file):
                        archivo.write(b'\x00' * 1024)
                #crear mbr
                mbr = Mbr()
                mbr.setTamano(script.getSize())
                mbr.setFecha_creacion(datetime.now())
                mbr.setDsk_signature(generarCodigo())
                mbr.setFit('F')
                #escribir mbr
                with open(script.getPath(), 'rb+') as archivo:
                    archivo.write(mbr.pack_data())
                #escribir particiones
                pos = 21
                for particion in mbr.getPartitions():
                    with open(script.getPath(), 'rb+') as archivo:
                        archivo.seek(pos)
                        archivo.write(particion.pack_data())
                    pos += 28
                print('¡Disco creado exitosamente!')
            else: 
                print('¡Error! no se pudo crear el disco.')
        else:
            print("¡Error! parametro no valido.")
        return None
    #COMANDO RMDISK
    elif (comando == "rmdisk"):
        if (parametro == 'path'):      
            script.setPath(valor)
        elif (parametro == 'ejecutar'):
            if (script.errors == 0):
                script.deleteDisk()
            else: 
                print('¡Error! no se pudo eliminar el disco.')
        else:
            print("¡Error! parametro no valido.")
        return None
    #COMANDO FDISK
    elif (comando == 'fdisk'):
        if (parametro == 'size'):
            script.setSize(int(valor))
        elif (parametro == 'path'):
            script.setPath(valor)
        elif (parametro == 'name'):
            script.setName(valor)
        elif (parametro == 'unit'):
            script.setUnit(valor)
        elif(parametro == 'type'):
            script.setType(valor)
        elif(parametro == 'fit'):
            script.setFit(valor)
        elif (parametro == 'ejecutar'):
            #obtener mbr
            mbr = Mbr()
            with open(script.getPath(), 'rb+') as archivo:
                archivo.seek(0)
                contenido = archivo.read(mbr.getLength())
            mbr = mbr.unpack_data(contenido)
            #obtener particiones
            pos = 21
            for i in range(4):
                particion = Partition()
                with open(script.getPath(), 'rb+') as archivo:
                    archivo.seek(pos)
                    contenido = archivo.read(28)
                particion = particion.unpack_data(contenido)
                mbr.getPartitions()[i] = particion
                pos += 28
            #crear particion
            nombre_existe = False
            temp = 0
            for partition in mbr.getPartitions():
                if (partition.getPart_name() == script.getName()):
                    nombre_existe = True
                    break
            if (nombre_existe) :
                print("¡Error! el valor del parametro 'name' ya existe.")
            else:
                pos_en_disco = 21
                pos_particion = None
                if (mbr.getFit() == 'BF'):
                    diferencia_minima = float('inf')
                    for i, partition in enumerate(mbr.getPartitions()):
                        if (partition.getPart_status == "I"):
                            diferencia = partition.getPart_s() - script.getSize()
                            if diferencia >= 0 and diferencia < diferencia_minima:
                                pos_particion = i
                                diferencia_minima = diferencia
                        else:
                            pos_en_disco += partition.getPart_s()
                elif (mbr.getFit() == 'FF'):
                    for i, partition in enumerate(mbr.getPartitions()):
                        if (partition.getPart_status() == "I"):
                            if partition.getPart_s() >= script.getSize():
                                pos_particion = i
                        else:
                            pos_en_disco += partition.getPart_s()
                elif (mbr.getFit() == 'WF'):
                    for i, partition in enumerate(mbr.getPartitions()):
                        if (partition.getPart_status() == "I"):
                            if (partition.getPart_s() >= script.getSize() and partition.getPart_s() >= temp):
                                pos_particion = i
                                temp = partition.getPart_s()
                        else:
                            pos_en_disco += partition.getPart_s()
                if (pos_particion == None):
                    for i, partition in enumerate(mbr.getPartitions()):
                        if (partition.getPart_status() == "I"):
                            if (partition.getPart_s() == 0):
                                pos_particion = i
                                break                           
                        else:
                            pos_en_disco += partition.getPart_s()

                
                if (pos_particion != None):
                    mbr.getPartitions()[pos_particion].setPart_status("A")
                    #mbr.getPartitions()[pos_particion].setPart_type(disk.getType())
                    mbr.getPartitions()[pos_particion].setPart_type('P')
                    #mbr.getPartitions()[pos_particion].setPart_fit(disk.getFit())
                    mbr.getPartitions()[pos_particion].setPart_fit("B")
                    #print(mbr.getPartitions()[pos_particion].getPart_fit())
                    mbr.getPartitions()[pos_particion].setPart_start(pos_en_disco)
                    if (script.unit == "M"):
                        mbr.getPartitions()[pos_particion].setPart_s(script.getSize()*1024*1024)
                    elif (script.unit == "K"):
                        mbr.getPartitions()[pos_particion].setPart_s(script.getSize()*1024)
                    else:
                        mbr.getPartitions()[pos_particion].setPart_s(script.getSize())
                    mbr.getPartitions()[pos_particion].setPart_name(script.getName())
                    #escribir mbr
                    with open(script.getPath(), 'rb+') as archivo:
                        archivo.write(mbr.pack_data())
                    #escribir particiones
                    pos = 21
                    for particion in mbr.getPartitions():
                        with open(script.getPath(), 'rb+') as archivo:
                            archivo.seek(pos)
                            archivo.write(particion.pack_data())
                            pos += 28
                    print('¡Particion creada exitosamente!')
                else: 
                    print('Las 4 particiones permitidas, ya han sido usadas.')
        else:
            print("¡Error! parametro no valido.")
        return None
    #cOMANDO MOUNT
    elif (comando == 'mount'):
        if (parametro == 'path'):
            pass
        elif (parametro == 'name'):
            pass
        else:
            print("¡Error! parametro no valido.")
        return None
    #COMANDO UNMOUNT
    elif (comando == 'unmount'):
        if (parametro == 'id'):
            pass
        else:
            print("¡Error! parametro no valido.")
        return None
    #COMANDO MKFS
    elif (comando == 'mkfs'):
        if (parametro == 'id'):
            pass
        elif (parametro == 'type'):
            pass
        elif (parametro == 'fs'):
            pass
        else:
            print("¡Error! parametro no valido.")
        return None
    #COMANDO LOGIN
    elif (comando == 'login'):
        if (parametro == 'user'):
            script.setUser(valor)
        elif (parametro == 'pass'):
            script.setPassword(valor)
        elif (parametro == 'id'):
            script.setId(valor)
        elif(parametro == 'ejecutar'):
            usuario_existe = False
            contraseña_correcta = False
            #leer archivo users.txt
            with open("users.txt", "r") as f:
                lineas = f.readlines()
            for linea in lineas:
                usuario_grupo = linea.strip().split(", ")
                if (usuario_grupo[1] == "U"):
                    if (script.getUser() in usuario_grupo):
                        usuario_existe = True
                        if (script.getPassword() in usuario_grupo):
                            contraseña_correcta = True
                        break
            if (usuario_existe):
                if (contraseña_correcta):
                    print(f"¡Bienvenido {script.getUser()}!")
                    usuario_actual = script.getUser()
                else:
                    print("¡Contraseña incorrecta!")
            else:
                print("¡Usuario no existe!")          
        else:
            print("¡Error! parametro no valido.")
        return None
    #COMANDO LOGOUT
    elif (comando == 'logout'):
        if (parametro == "ejecutar"):
            if (usuario_actual != ""):
                usuario_actual = ""
            else:
                print("¡Error! No existe una sesion activa.")
        return None
    #COMANDO MKGRP
    elif (comando == 'mkgrp'):
        if (parametro == 'name'):
            pass
        else:
            print("¡Error! parametro no valido.")

    elif (comando == 'rmgrp'):
        if (parametro == 'name'):
            pass
        else:
            print("¡Error! parametro no valido.")

    elif (comando == 'mkusr'):
        if (parametro == 'user'):
            pass
        elif (parametro == 'pass'):
            pass
        elif (parametro == 'grp'):
            pass
        else:
            print("¡Error! parametro no valido.")

    elif (comando == 'rmusr'):
        if (parametro == 'user'):
            pass
        else:
            print("¡Error! parametro no valido.")

    elif (comando == 'mkfile'):
        if (parametro == 'path'):
            pass
        elif (parametro == 'r'):
            pass
        elif (parametro == 'size'):
            pass
        elif (parametro == 'cont'):
            pass
        else:
            print("¡Error! parametro no valido.")

    elif (comando == 'cat'):
        if (parametro == 'filen'):
            pass
        else:
            print("¡Error! parametro no valido.")

    elif (comando == 'remove'):
        if (parametro == 'path'):
            pass
        else:
            print("¡Error! parametro no valido.")

    elif (comando == 'edit'):
        if (parametro == 'path'):
            pass
        elif (parametro == 'cont'):
            pass
        else:
            print("¡Error! parametro no valido.")
    
    elif (comando == 'rename'):
        if (parametro == 'path'):
            pass
        elif (parametro == 'name'):
            pass
        else:
            print("¡Error! parametro no valido.")

    elif (comando == 'mkdir'):
        if (parametro == 'path'):
            pass
        elif (parametro == 'r'):
            pass
        else:
            print("¡Error! parametro no valido.")

    elif (comando == 'copy'):
        if (parametro == 'path'):
            pass
        elif (parametro == 'destino'):
            pass
        else:
            print("¡Error! parametro no valido.")

    elif (comando == 'move'):
        if (parametro == 'path'):
            pass
        elif (parametro == 'destino'):
            pass
        else:
            print("¡Error! parametro no valido.")

    elif (comando == 'find'):
        if (parametro == 'path'):
            pass
        elif (parametro == 'name'):
            pass
        else:
            print("¡Error! parametro no valido.")

    elif (comando == 'chown'):
        if (parametro == 'path'):
            pass
        elif (parametro == 'user'):
            pass
        elif (parametro == 'r'):
            pass
        else:
            print("¡Error! parametro no valido.")

    elif (comando == 'chgrp'):
        if (parametro == 'user'):
            pass
        elif (parametro == 'grp'):
            pass
        else:
            print("¡Error! parametro no valido.")

    elif (comando == 'chmod'):
        if (parametro == 'path'):
            pass
        elif (parametro == 'ugo'):
            pass
        elif (parametro == 'r'):
            pass
        else:
            print("¡Error! parametro no valido.")

    elif (comando == 'pause'):
        while True: 
            tecla = input("Presione 'ENTER' para continuar ")
            if (tecla == ""):
                break
    #COMANDO EXECUTE
    elif (comando == 'execute'):
        if (parametro == "path"):
            if os.path.exists(valor):
                archivo = open(valor, "r")
                contenido = archivo.read()
                return contenido
            else:
                print("¡Error! archivo no encontrado.")
        return None
    #COMANDO REP
    elif (comando == "rep"):
        if (parametro == "path"):
            #obtener mbr
            mbr = Mbr()
            with open(valor, 'rb+') as archivo:
                archivo.seek(0)
                contenido = archivo.read(mbr.getLength())
            mbr = mbr.unpack_data(contenido)
            #obtener particiones
            pos = 21
            for i in range(4):
                particion = Partition()
                with open(valor, 'rb+') as archivo:
                    archivo.seek(pos)
                    contenido = archivo.read(28)
                particion = particion.unpack_data(contenido)
                mbr.getPartitions()[i] = particion
                pos += 28
            #imprimir particiones
            print("mbr_tamaño: ", mbr.getTamano())
            print("mbr_fecha_creacion: ", mbr.getFecha_creacion())
            print("mbr_dsk_signature: ", mbr.getDsk_signature())
            print("mbr_ajuste: ", mbr.getFit())
            for partition in mbr.getPartitions():
                print(partition.getPart_status())
                print(partition.getPart_type())
                print(partition.getPart_fit())
                print(partition.getPart_start())
                print(partition.getPart_s())
                print(partition.getPart_name())

        return None

        
'''
def comando_ejecutar(parametro, valor):
    global comando
    global nombre_archivo
    global numero
    if (comando == "execute"):
        if (parametro == "path"):
            archivo = open(valor, "r")
            contenido = archivo.read()
            return contenido
    elif (comando == "mkdisk"):
        #crear un arhivo vacio
        kilobytes = 5120 # 5MB = 5120KB
        size_kilobyte = 1024
        if (os.path.exists('disk'+str(numero)+'.dsk')):
            numero += 1
        nombre_archivo = 'disk' + str(numero) + '.dsk'
        with open(nombre_archivo, 'wb') as archivo:
            for i in range(0, kilobytes):
                archivo.write(b'\x00' * size_kilobyte)
        size_bytes = 1000000 * (kilobytes/size_kilobyte)
        #crear propiedades
        propiedades = Propiedades()
        propiedades.setAsignature()
        propiedades.setTamano(size_bytes)
        propiedades.setFecha()
        #escribir en archivo
        with open(nombre_archivo, 'rb+') as archivo:
            archivo.write(propiedades.pack_data())
            archivo.close() 
        return ""
    elif (comando == "rep"):
        posicion = 0
        while True:
            #leer archivo
            with open(nombre_archivo, 'rb+') as archivo:
                archivo.seek(posicion)
                contenido = archivo.read(1)
                archivo.close()
            if (contenido == b'\x00') : break
            propiedades = Propiedades()
            #leer archivo
            with open(nombre_archivo, 'rb+') as archivo:
                archivo.seek(posicion)
                contenido = archivo.read(propiedades.getSize())
                archivo.close()
            propiedades = propiedades.unpack_data(contenido)
            print("mbr_dsk_signature: ", propiedades.mbr_dsk_signature)
            print("mbr_tamaño: ", propiedades.mbr_tamano)
            print("mbr_fecha_creacion: ", propiedades.mbr_fecha_creacion)
            posicion += propiedades.getSize()
        return ""
'''

def generarCodigo():
    code = list(range(1001, 1030))
    random.shuffle(code)
    return code.pop()
