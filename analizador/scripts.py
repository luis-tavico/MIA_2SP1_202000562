import os
from comandos.mkdisk import Mkdisk
from comandos.rmdisk import Rmdisk
from comandos.fdisk import Fdisk

global comando, disk

def comando_activar(valor):
    global comando, disk
    comando = valor

    if (comando == "mkdisk"):
        disk = Mkdisk()
    elif (comando == "rmdisk"):
        disk = Rmdisk()
    elif (comando == "fdisk"):
        disk = Fdisk()

def comando_ejecutar(parametro, valor):
    global comando, disk
    #COMANDO MKDISK
    if (comando == "mkdisk"):
        if (parametro == 'size'):
            disk.setSize(int(valor))
        elif (parametro == 'path'):
            disk.setPath(valor)
        elif (parametro == 'fit'):
            disk.setFit(valor)
        elif (parametro == 'unit'):
            disk.setUnit(valor)
        elif (parametro == "ejecutar"):
            if (disk.errors == 0):
                #crear un arhivo vacio
                size_file = int(disk.size)
                if (disk.unit == "M"):
                    size_file = size_file * 1024
                with open(disk.getPath(), 'wb') as archivo:
                    for i in range(0, size_file):
                        archivo.write(b'\x00' * 1024)   
                #escribir en archivo
                with open(disk.getPath(), 'rb+') as archivo:
                    archivo.write(disk.pack_data())
                    archivo.close()
                print('¡Disco creado!')
            else: 
                print('No se pudo crear el disco.')
        else:
            print("¡Error! parametro no valido.")
        return None
    #COMANDO RMDISK
    elif (comando == "rmdisk"):
        if (parametro == 'path'):      
            disk.setPath(valor)
        elif (parametro == 'ejecutar'):
            if (disk.errors == 0):
                disk.deleteDisk()
                '''
                #leer archivo
                disco = Mkdisk()
                with open(disk.getPath(), 'rb+') as archivo:
                    archivo.seek(0)
                    contenido = archivo.read(disco.getLength())
                    archivo.close()
                disco = disco.unpack_data(contenido)
                print("size: ", disco.getSize())
                print("path: ", disco.getPath())
                print("fit: ", disco.getFit())
                print("unit: ", disco.getUnit())
                '''
            else: 
                print('No se pudo eliminar el disco.')
        else:
            print("¡Error! parametro no valido.")
    #COMANDO FDISK
    elif (comando == 'fdisk'):
        ruta_disco = "lo hice solo para arreglar el error"
        if (parametro == 'size'):
            if (int(valor) > 0):
                disk.size = int(valor)
            else:
                print("¡Ocurrio un error al asignar valor al parametro 'size'.\nEl valor debe ser mayor a 0.")
        elif (parametro == 'path'):
            disk.path = valor
        elif (parametro == 'name'):
            disk.name = valor
        elif (parametro == 'unit'):
            disk.unit = valor
        elif (parametro == 'ejecutar'):
            mbr = Mkdisk()
            with open(ruta_disco, 'rb+') as archivo:
                archivo.seek(0)
                contenido = archivo.read(mbr.getLength())
                archivo.close()
            mbr = mbr.unpack_data(contenido)
            partitionFree = mbr.getPartitionFree()
            if partitionFree != None:
                if (disk.getUnit() == 'M'):
                    mbr.setSizePartition(partitionFree+(disk.getSize()*1024*1024))
                elif (disk.getUnit() == 'K'):
                    mbr.setSizePartition(partitionFree+(disk.getSize()*1024))
                else:
                    mbr.setSizePartition(partitionFree+disk.getSize())
                #escribir en archivo mbr
                with open(disk.getPath(), 'rb+') as archivo:
                    archivo.write(mbr.pack_data())
                    archivo.close()
                #escribir en archivo particion
                with open(disk.getPath(), 'rb+') as archivo:
                    archivo.seek(partitionFree)
                    archivo.write(disk.pack_data())
                    archivo.close()
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

    elif (comando == 'unmount'):
        if (parametro == 'id'):
            pass
        else:
            print("¡Error! parametro no valido.")

    elif (comando == 'mkfs'):
        if (parametro == 'id'):
            pass
        elif (parametro == 'type'):
            pass
        elif (parametro == 'fs'):
            pass
        else:
            print("¡Error! parametro no valido.")

    elif (comando == 'login'):
        if (parametro == 'user'):
            pass
        elif (parametro == 'pass'):
            pass
        elif (parametro == 'id'):
            pass
        else:
            print("¡Error! parametro no valido.")

    elif (comando == 'logout'):
        print("Cierra Sesion")

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
