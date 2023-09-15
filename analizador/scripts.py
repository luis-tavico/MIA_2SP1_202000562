import os
import random
from datetime import datetime
import shutil
import pygraphviz as pgv
#import graphviz
from analizador.comandos.cat import Cat
from analizador.comandos.chgrp import Chgrp
from analizador.comandos.chmod import Chmod
from analizador.comandos.chown import Chown
from analizador.comandos.copy import Copy
from analizador.comandos.edit import Edit
from analizador.comandos.execute import Execute
from analizador.comandos.fdisk import Fdisk
#from analizador.comandos.find import Find
from analizador.comandos.login import Login
from analizador.comandos.mbr import Mbr
from analizador.comandos.mkdir import Mkdir
from analizador.comandos.mkdisk import Mkdisk
from analizador.comandos.mkfile import Mkfile
from analizador.comandos.mkfs import Mkfs
from analizador.comandos.mkgrp import Mkgrp
from analizador.comandos.mkusr import Mkusr
from analizador.comandos.mount import Mount
from analizador.comandos.move import Move
from analizador.comandos.partition import Partition
from analizador.comandos.rename import Rename
from analizador.comandos.remove import Remove
from analizador.comandos.rep import Rep
from analizador.comandos.rmdisk import Rmdisk
from analizador.comandos.rmgrp import Rmgrp
from analizador.comandos.rmusr import Rmusr
from analizador.comandos.unmount import Unmount

global comando, script, usuario_actual, particiones_montadas
usuario_actual = ""
particiones_montadas = {}

def comando_activar(valor):
    global comando, script
    comando = valor

    #comandos de discos
    if (comando.lower() == "mkdisk"):
        script = Mkdisk()
        print("\033[36m<<System>> {}\033[00m" .format("Ejecutando comando mkdisk..."))
    elif (comando.lower() == "rmdisk"):
        script = Rmdisk()
        print("\033[36m<<System>> {}\033[00m" .format("Ejecutando comando rmdisk..."))
    elif (comando.lower() == "fdisk"):
        script = Fdisk()
        print("\033[36m<<System>> {}\033[00m" .format("Ejecutando comando fdisk..."))
    elif (comando.lower() == "mount"):
        script = Mount()
        print("\033[36m<<System>> {}\033[00m" .format("Ejecutando comando mount..."))
    elif (comando.lower() == "unmount"):
        script = Unmount()
        print("\033[36m<<System>> {}\033[00m" .format("Ejecutando comando unmount..."))
    elif (comando.lower() == "mkfs"):
        script = Mkfs()
        print("\033[36m<<System>> {}\033[00m" .format("Ejecutando comando mkfs..."))
    #comandos de usuarios y grupos
    elif (comando.lower() == "login"):
        script = Login()
    elif (comando.lower() == "mkgrp"):
        script = Mkgrp()
    elif (comando.lower() == "rmgrp"):
        script = Rmgrp()
    elif (comando.lower() == "mkusr"):
        script = Mkusr()
    elif (comando.lower() == "rmusr"):
        script = Rmusr()
    #comandos de archivos y permisos
    elif (comando.lower() == "mkfile"):
        script = Mkfile()
    elif (comando.lower() == "cat"):
        script = Cat()
    elif (comando.lower() == "remove"):
        script = Remove()
    elif (comando.lower() == "edit"):
        script = Edit()
    elif (comando.lower() == "rename"):
        script = Rename()
    elif (comando.lower() == "mkdir"):
        script = Mkdir()
    elif (comando.lower() == "copy"):
        script = Copy()
    elif (comando.lower() == "move"):
        script = Move()
    elif (comando.lower() == "find"):
        #script = Find()
        pass
    elif (comando.lower() == "chown"):
        script = Chown()
    elif (comando.lower() == "chgrp"):
        script = Chgrp()
    elif (comando.lower() == "chmod"):
        script = Chmod()
    elif (comando.lower() == "execute"):
        script = Execute()
        print("\033[36m<<System>> {}\033[00m" .format("Ejecutando comando execute..."))
    elif (comando.lower() == "rep"):
        script = Rep()
        print("\033[36m<<System>> {}\033[00m" .format("Ejecutando comando rep..."))

def comando_ejecutar(parametro, valor):
    global comando, script, usuario_actual, particiones_montadas
    #COMANDO MKDISK
    if (comando == "mkdisk"):
        if (parametro == 'size'):
            print("leyendo tamaño del disco...")
            script.setSize(int(valor))
        elif (parametro == 'path'):
            print("leyendo ruta del disco...")
            script.setPath(valor)
        elif (parametro == 'fit'):
            print("leyendo ajuste del disco...")
            script.setFit(valor)
        elif (parametro == 'unit'):
            print("leyendo unidad del disco...")
            script.setUnit(valor)
        elif (parametro == "ejecutar"):
            if (script.errors == 0):
                #crear un arhivo vacio
                tamano_archivo = script.getSize()
                if (script.getUnit() == "M"):
                    tamano_archivo = tamano_archivo * 1024
                with open(script.getPath(), 'wb') as archivo:
                    for i in range(0, tamano_archivo):
                        archivo.write(b'\x00' * 1024)
                #crear mbr
                mbr = Mbr()
                if (script.getUnit() == "M"):
                    mbr.setTamano(script.getSize()*1024*1024)
                else:
                    mbr.setTamano(script.getSize()*1024)
                mbr.setFecha_creacion(datetime.now())
                mbr.setDsk_signature(generarCodigo())
                mbr.setFit(script.getFit()[0])
                #escribir mbr
                with open(script.getPath(), 'rb+') as archivo:
                    archivo.write(mbr.pack_data())
                #escribir particiones
                pos = mbr.getLength()
                for particion in mbr.getPartitions():
                    with open(script.getPath(), 'rb+') as archivo:
                        archivo.seek(pos)
                        archivo.write(particion.pack_data())
                    pos += particion.getLength()
                print("\033[1;32m<<Success>> {}\033[00m" .format("Disco creado exitosamente."))
                print("\033[36m<<System>> {}\033[00m" .format("...Comando mkdisk ejecutado"))
            else: 
                print("\033[91m<<Error>> {}\033[00m" .format("No se pudo crear el disco."))
        else:
            script.errors += 1
            print("\033[91m<<Error>> {}\033[00m" .format("Parametro no valido."))
        return None
    #COMANDO RMDISK
    elif (comando == "rmdisk"):
        if (parametro == 'path'):   
            print("leyendo ruta del disco...")   
            script.setPath(valor)
        elif (parametro == 'ejecutar'):
            if (script.errors == 0):
                script.deleteDisk()
                print("\033[36m<<System>> {}\033[00m" .format("...Comando rmdisk ejecutado"))
            else:
                print("\033[91m<<Error>> {}\033[00m" .format("No se pudo eliminar el disco."))
        else:
            script.errors += 1
            print("\033[91m<<Error>> {}\033[00m" .format("Parametro no valido."))
        return None
    #COMANDO FDISK
    elif (comando == 'fdisk'):
        if (parametro == 'size'):
            print("leyendo tamaño de la particion...")
            script.setSize(int(valor))
        elif (parametro == 'path'):
            print("leyendo ruta del disco...")
            script.setPath(valor)
        elif (parametro == 'name'):
            print("leyendo nombre de la particion...")
            script.setName(valor)
        elif (parametro == 'unit'):
            print("leyendo unidad de la particion...")
            script.setUnit(valor)
        elif(parametro == 'type'):
            print("leyendo tipo de la particion...")
            script.setType(valor)
        elif(parametro == 'fit'):
            print("leyendo ajuste de la particion...")
            script.setFit(valor)
        elif(parametro == 'delete'):
            print("eliminando particion...")
            script.setDelete(valor)
        elif(parametro == 'add'):
            print("agregando/quitando espacio a particion...")
            script.setAdd(valor)
        elif (parametro == 'ejecutar'):
            if (script.errors == 0):
                #obtener mbr
                mbr = Mbr()
                with open(script.getPath(), 'rb+') as archivo:
                    archivo.seek(0)
                    contenido = archivo.read(mbr.getLength())
                mbr = mbr.unpack_data(contenido)
                #obtener particiones
                pos = mbr.getLength()
                for i in range(4):
                    particion = Partition()
                    with open(script.getPath(), 'rb+') as archivo:
                        archivo.seek(pos)
                        contenido = archivo.read(particion.getLength())
                    particion = particion.unpack_data(contenido)
                    mbr.getPartitions()[i] = particion
                    pos += particion.getLength()
                #obtener tamaño del disco
                tamano_disco = mbr.getTamano()
                #eliminar particion
                if (script.getDelete().lower() == "full"):
                    for partition in mbr.getPartitions():
                        if (partition.getPart_name().rstrip("\x00") == script.getName()):
                            content = ""
                            for i in range (partition.getPart_s()):
                                content += '\x00' 
                            print(len(content))
                            #print(content)
                            with open(script.getPath(), 'rb+') as archivo:
                                archivo.seek(partition.getPart_start())
                                archivo.write(b'aqui\x00\x00\x00\x00\x00')
                            print("\033[1;32m<<Success>> {}\033[00m" .format("Particion eliminada exitosamente."))
                            return None
                    print("\033[91m<<Error>> {}\033[00m" .format("La particion no existe."))
                    print("\033[91m<<Error>> {}\033[00m" .format("No se pudo eliminar la particion."))
                    return None
                #agregar/quitar tamaño a particion
                if (int(script.getAdd()) != 0):
                    for partition in mbr.getPartitions():
                        if (partition.getPart_name().rstrip("\x00") == script.getName()):
                            if (int(script.getAdd()) < 0):
                                if (script.getUnit()) == "M":
                                    new_size = int(partition.getPart_s())+int(script.getAdd())*1024*1024
                                elif (script.getUnit()) == "K":
                                    new_size = int(partition.getPart_s())+ int(script.getAdd())*1024
                                elif (script.getUnit()) == "B":
                                    new_size = int(partition.getPart_s())+int(script.getAdd())
                                if new_size >= 0:
                                    partition.setPart_s(int(new_size))
                                    #escribir mbr
                                    with open(script.getPath(), 'rb+') as archivo:
                                        archivo.write(mbr.pack_data())
                                    #escribir particiones
                                    pos = mbr.getLength()
                                    for particion in mbr.getPartitions():
                                        with open(script.getPath(), 'rb+') as archivo:
                                            archivo.seek(pos)
                                            archivo.write(particion.pack_data())
                                        pos += particion.getLength()
                                    print("\033[1;32m<<Success>> {}\033[00m" .format("Particion reducida exitosamente."))
                                    return None
                                else:
                                    print("\033[91m<<Error>> {}\033[00m" .format("La particion es menor al tamaño a reducir."))
                                    print("\033[91m<<Error>> {}\033[00m" .format("No se pudo agregar/quitar tamaño a la particion."))
                    print("\033[91m<<Error>> {}\033[00m" .format("La particion no existe."))
                    print("\033[91m<<Error>> {}\033[00m" .format("No se pudo agregar/quitar tamaño a la particion."))
                    return None
                #verificar si nombre existe
                for partition in mbr.getPartitions():
                    if (partition.getPart_name() == script.getName()):
                        script.errors += 1
                        print("\033[91m<<Error>> {}\033[00m" .format("El valor del parametro 'name' ya existe."))
                        break
                #verificar tipo de particion
                if (script.getType().lower() == "e"):
                    for partition in mbr.getPartitions():
                        if (partition.getPart_type().lower() == "e"):
                            script.errors += 1
                            print("\033[91m<<Error>> {}\033[00m" .format("Ya existe una particion extendida."))
                            break
                elif (script.getType().lower() == "l"):
                    extendida_existe = False
                    for partition in mbr.getPartitions():
                        if (partition.getPart_type().lower() == "e"):
                            extendida_existe = True
                            break
                    if not(extendida_existe):
                        script.errors += 1
                        print("\033[91m<<Error>> {}\033[00m" .format("No existe una particion extendida."))


                if (script.errors == 0):
                #if (script.getType() == "P" or script.getType() == "E"):
                    temp = 0
                    pos_en_disco = 21 + 4 * 28
                    pos_particion = None
                    if (mbr.getFit() == 'BF'):
                        diferencia_minima = float('inf')
                        for i, partition in enumerate(mbr.getPartitions()):
                            if (partition.getPart_status == "0"):
                                diferencia = partition.getPart_s() - script.getSize()
                                if diferencia >= 0 and diferencia < diferencia_minima:
                                    pos_particion = i
                                    diferencia_minima = diferencia
                            else:
                                pos_en_disco += partition.getPart_s()
                    elif (mbr.getFit() == 'FF'):
                        for i, partition in enumerate(mbr.getPartitions()):
                            if (partition.getPart_status() == "0"):
                                if partition.getPart_s() >= script.getSize():
                                    pos_particion = i
                            else:
                                pos_en_disco += partition.getPart_s()
                    elif (mbr.getFit() == 'WF'):
                        for i, partition in enumerate(mbr.getPartitions()):
                            if (partition.getPart_status() == "0"):
                                if (partition.getPart_s() >= script.getSize() and partition.getPart_s() >= temp):
                                    pos_particion = i
                                    temp = partition.getPart_s()
                            else:
                                pos_en_disco += partition.getPart_s()
                    if (pos_particion == None):
                        for i, partition in enumerate(mbr.getPartitions()):
                            if (partition.getPart_status() == "0"):
                                if (partition.getPart_s() == 0):
                                    pos_particion = i
                                    break                           
                            else:
                                pos_en_disco += partition.getPart_s()

                    
                    if (pos_particion != None):
                        mbr.getPartitions()[pos_particion].setPart_status("1")
                        mbr.getPartitions()[pos_particion].setPart_type(script.getType())
                        mbr.getPartitions()[pos_particion].setPart_fit(script.getFit()[0])
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
                        pos = mbr.getLength()
                        for particion in mbr.getPartitions():
                            with open(script.getPath(), 'rb+') as archivo:
                                archivo.seek(pos)
                                archivo.write(particion.pack_data())
                            pos += particion.getLength()
                        print("\033[1;32m<<Success>> {}\033[00m" .format("Particion creada exitosamente."))
                        print("\033[36m<<System>> {}\033[00m" .format("...Comando fdisk ejecutado"))
                    else:
                        script.errors += 1
                        print("\033[91m<<Error>> {}\033[00m" .format("Las 4 particiones permitidas, ya han sido usadas."))
            if (script.errors != 0):
                print("\033[91m<<Error>> {}\033[00m" .format("No se pudo crear la particion."))
        else:
            print("\033[91m<<Error>> {}\033[00m" .format("Parametro no valido."))
        return None
    #cOMANDO MOUNT
    elif (comando == 'mount'):
        if (parametro == 'path'):
            print("leyendo ruta del disco...")
            script.setPath(valor)
        elif (parametro == 'name'):
            print("leyendo nombre de la particion...")
            script.setName(valor)
        elif (parametro == 'ejecutar'):
            if (script.errors == 0):
                #obtener mbr
                mbr = Mbr()
                with open(script.getPath(), 'rb+') as archivo:
                    archivo.seek(0)
                    contenido = archivo.read(mbr.getLength())
                mbr = mbr.unpack_data(contenido)
                #obtener particiones
                pos = mbr.getLength()
                for i in range(4):
                    particion = Partition()
                    with open(script.getPath(), 'rb+') as archivo:
                        archivo.seek(pos)
                        contenido = archivo.read(particion.getLength())
                    particion = particion.unpack_data(contenido)
                    mbr.getPartitions()[i] = particion
                    pos += particion.getLength()
                #buscar particion
                num_particion = -1
                for i, partition in enumerate(mbr.getPartitions()):
                    if (partition.getPart_name().rstrip("\x00") == script.getName()):
                        num_particion = i+1
                        break
                if (num_particion == -1):
                    script.errors += 1
                    print("\033[91m<<Error>> {}\033[00m" .format("La particion no existe."))
                else:
                    id = "62" + str(num_particion) + os.path.splitext(os.path.basename(script.getPath()))[0]
                    if not(id in particiones_montadas):   
                        particiones_montadas[id] = script.getPath()
                        print("Particiones montadas:")
                        for clave, valor in particiones_montadas.items():
                            print(clave)
                        print("\033[1;32m<<Success>> {}\033[00m" .format("Particion montada exitosamente."))
                        print("\033[36m<<System>> {}\033[00m" .format("...Comando mount ejecutado"))
                    else:
                        script.errors += 1
                        print("\033[91m<<Error>> {}\033[00m" .format("La particion ya esta montada."))
            if (script.errors != 0):
                print("\033[91m<<Error>> {}\033[00m" .format("No se pudo montar la particion."))
        else:
            print("\033[91m<<Error>> {}\033[00m" .format("Parametro no valido."))
        return None
    #COMANDO UNMOUNT
    elif (comando == 'unmount'):
        if (parametro == 'id'):
            print("leyendo id de la particion...")
            script.setId(valor)
        elif (parametro == 'ejecutar'):
            if script.getId() in particiones_montadas:   
                particiones_montadas.pop(script.getId())
                print("\033[1;32m<<Success>> {}\033[00m" .format("Particion desmontada exitosamente."))
                print("\033[36m<<System>> {}\033[00m" .format("...Comando unmount ejecutado"))
            else:
                print("\033[91m<<Error>> {}\033[00m" .format("La particion no existe."))
                print("\033[91m<<Error>> {}\033[00m" .format("No se pudo desmontar la particion."))
        else:
            print("\033[91m<<Error>> {}\033[00m" .format("Parametro no valido."))
        return None
    #COMANDO MKFS
    elif (comando == 'mkfs'):
        if (parametro == 'id'):
            print("leyendo id de la particion...")
            script.setId(valor)
        elif (parametro == 'type'):
            print("leyendo tipo de formateo...")
            script.setType(valor)
        elif (parametro == 'fs'):
            print("leyendo sistema de fichero...")
            script.setFs(valor)
        elif (parametro == 'ejecutar'):
            if script.getId() in particiones_montadas:
                pass
            else:
                print("¡Error! la particion no existe.")
        else:
            print("\033[91m<<Error>> {}\033[00m" .format("Parametro no valido."))
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
            with open("users.txt", "r") as archivo:
                lineas = archivo.readlines()
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
        if (parametro == 'ejecutar'):
            if (usuario_actual != ""):
                usuario_actual = ""
            else:
                print("¡Error! no existe una sesion activa.")
        return None
    #COMANDO MKGRP
    elif (comando == 'mkgrp'):
        if (parametro == 'name'):
            script.setName(valor)
        elif (parametro == 'ejecutar'):
            if (usuario_actual == "root"):
                num = 1
                grupo_existe = False
                #leer archivo users.txt
                with open("users.txt", "r") as archivo:
                    lineas = archivo.readlines()
                for linea in lineas:
                    usuario_grupo = linea.strip().split(", ")
                    if (usuario_grupo[1] == "G"):
                        if (script.getName() in usuario_grupo):
                            grupo_existe = True
                            break
                        else:
                            num += 1
                if (not grupo_existe):
                    #editar archivo
                    with open("users.txt", 'a') as archivo:
                        archivo.write(str(num) + ", G, " + script.getName() + "\n")
                    print("¡Grupo creado exitosamente!")
                else:
                    print("¡Error! el grupo a crear ya existe.")
            elif (usuario_actual == ""):
                print("¡Error! ningun usuario ha iniciado sesion.")
            else:
                print("¡Error! solo el usuario 'root' tiene permiso de crear grupos.")
        else:
            print("¡Error! parametro no valido.")
        return None
    #COMANDO RMGRP
    elif (comando == 'rmgrp'):
        if (parametro == 'name'):
            script.setName(valor)
        elif (parametro == 'ejecutar'):
            if (usuario_actual == "root"):
                cont_editado = ""
                grupo_existe = False
                pos = None
                #leer archivo users.txt
                with open("users.txt", "r") as archivo:
                    lineas = archivo.readlines()
                for i, linea in enumerate(lineas):
                    usuario_grupo = linea.strip().split(", ")
                    if (usuario_grupo[1] == "G"):
                        if (script.getName() in usuario_grupo):
                            cont_editado = "0, " + usuario_grupo[1] + ", " + usuario_grupo[2] + "\n"
                            grupo_existe = True
                            pos = i
                            break
                if (grupo_existe):
                    lineas[pos] = cont_editado
                    #escribir las líneas de nuevo en el archivo
                    with open("users.txt", 'w') as archivo:
                        archivo.writelines(lineas)
                    print("¡Grupo eliminado exitosamente!")
                else:
                    print("¡Error! el grupo a eliminar no existe")
            elif (usuario_actual == ""):
                print("¡Error! ningun usuario ha iniciado sesion.")
            else:
                print("¡Error! solo el usuario 'root' tiene permiso de eliminar grupos.")
        else:
            print("¡Error! parametro no valido.")
        return None
    #COMAND MKUSR
    elif (comando == 'mkusr'):
        if (parametro == 'user'):
            script.setUser(valor)
        elif (parametro == 'pass'):
            script.setPassword(valor)
        elif (parametro == 'grp'):
            script.setGrp(valor)
        elif (parametro == 'ejecutar'):
            if (usuario_actual == 'root'):
                if (script.errors == 0):
                    usuario_existe = False
                    grupo_existe = False
                    pos = None
                    #leer archivo users.txt
                    with open("users.txt", "r") as archivo:
                        lineas = archivo.readlines()
                    for i, linea in enumerate(lineas):
                        usuario_grupo = linea.strip().split(", ")
                        if (usuario_grupo[1] == "U"):
                            if (script.getUser() in usuario_grupo):
                                usuario_existe = True
                        elif (usuario_grupo[1] == "G"):
                            if (script.getGrp() == usuario_grupo[2]):
                                grupo_existe = True
                                pos = usuario_grupo[0]
                    if (grupo_existe):
                        if (not usuario_existe):
                            #editar archivo
                            with open("users.txt", 'a') as archivo:
                                archivo.write(pos + ", U, " + script.getGrp() + ", " + script.getUser() + ", " + script.getPassword() + "\n")
                            print("¡Usuario creado exitosamente!")
                        else:
                            print("¡Error! el usuario a crear ya existe.")
                    else:
                        print("¡Error! el grupo no existe.")
                else:
                    print('¡Error! no se pudo crear el usuario.')
            elif (usuario_actual == ""):
                print("¡Error! ningun usuario ha iniciado sesion.")
            else:
                print("¡Error! solo el usuario 'root' tiene permiso de crear usuarios.")
        else:
            print("¡Error! parametro no valido.")
        return None
    #COMANDO RMUSR
    elif (comando == 'rmusr'):
        if (parametro == 'user'):
            script.setUser(valor)
        elif (parametro == 'ejecutar'):
            if (usuario_actual == "root"):
                cont_editado = ""
                usuario_existe = False
                pos = None
                #leer archivo users.txt
                with open("users.txt", "r") as archivo:
                    lineas = archivo.readlines()
                for i, linea in enumerate(lineas):
                    usuario_grupo = linea.strip().split(", ")
                    if (usuario_grupo[1] == "U"):
                        if (script.getUser() in usuario_grupo):
                            cont_editado = "0, " + "U, " + usuario_grupo[2] + ", " + usuario_grupo[3] + ", " + usuario_grupo[4] + "\n"
                            usuario_existe = True
                            pos = i
                            break
                if (usuario_existe):
                    lineas[pos] = cont_editado
                    #escribir las líneas de nuevo en el archivo
                    with open("users.txt", 'w') as archivo:
                        archivo.writelines(lineas)
                    print("¡Usuario eliminado exitosamente!")
                else:
                    print("¡Error! el usuario a eliminar no existe")
            elif (usuario_actual == ""):
                print("¡Error! ningun usuario ha iniciado sesion.")
            else:
                print("¡Error! solo el usuario 'root' tiene permiso de eliminar usuarios.")
        else:
            print("¡Error! parametro no valido.")
        return None
    #COMANDO MKFILE
    elif (comando == 'mkfile'):
        if (parametro == 'path'):
            script.setPath(valor)
        elif (parametro == 'r'):
            script.setR(True)
        elif (parametro == 'size'):
            script.setSize(int(valor))
        elif (parametro == 'cont'):
            script.setCont(valor)
        elif ('ejecutar'):
            if script.errors == 0:
                if (script.getR()):
                    carpetas = os.path.dirname(script.getPath())
                    if (not os.path.exists(script.getPath())):
                        if (not os.path.exists(carpetas)):
                            os.makedirs(carpetas)
                        contenido = ""
                        if (script.getSize() != 0):
                            num = 0
                            for i in range(script.getSize()):
                                if (num == 10): num = 0
                                contenido += str(num)
                                num += 1
                        if (script.getCont() != ""):
                            with open(script.getCont(), "r") as archivo:
                                contenido = archivo.read()
                        with open(script.getPath(), "w") as archivo:
                            archivo.write(contenido)
                    else:
                        respuesta = input("El archivo ya existe, ¿Desea sobreescribirlo? (y/n)")
                        if (respuesta == "s"):
                            #pendiente                       
                            contenido = ""
                            if (script.getSize() != 0):
                                num = 0
                                for i in range(script.getSize()):
                                    if (num == 10): num = 0
                                    contenido += str(num)
                                    num += 1
                            if (script.getCont() != ""):
                                with open(script.getCont(), "r") as archivo:
                                    contenido = archivo.read()
                            with open(script.getPath(), "a") as archivo:
                                archivo.write(contenido)
                else:
                    carpetas = os.path.dirname(script.getPath())
                    if (not os.path.exists(script.getPath())):
                        if (os.path.exists(carpetas)):
                            contenido = ""
                            if (script.getSize() != 0):
                                num = 0
                                for i in range(script.getSize()):
                                    if (num == 10): num = 0
                                    contenido += str(num)
                                    num += 1
                            if (script.getCont() != ""):
                                with open(script.getCont(), "r") as archivo:
                                    contenido = archivo.read()
                            with open(script.getPath(), "w") as archivo:
                                archivo.write(contenido)
                        else:
                            print("¡Error! la ruta de carpetas no existe.")
                    else:
                        respuesta = input("El archivo ya existe, ¿Desea sobreescribirlo? (y/n)")
                        if (respuesta == "s"):
                            #pendiente                       
                            contenido = ""
                            if (script.getSize() != 0):
                                num = 0
                                for i in range(script.getSize()):
                                    if (num == 10): num = 0
                                    contenido += str(num)
                                    num += 1
                            if (script.getCont() != ""):
                                with open(script.getCont(), "r") as archivo:
                                    contenido = archivo.read()
                            with open(script.getPath(), "a") as archivo:
                                archivo.write(contenido)
            else:
                print('¡Error! no se pudo crear el archivo.')
        else:
            print("¡Error! parametro no valido.")
        return None
    #COMANDO CAT
    elif (comando == 'cat'):
        if (parametro[:4] == 'file'):
            script.setPathFile(valor)
        elif (parametro == 'ejecutar'):
            if script.errors == 0:
                for path in script.getPathFiles():
                    with open(path, "r") as archivo:
                        contenido = archivo.read()
                    print(contenido)
            else:
                print('¡Error! no se pudo mostrar el contenido de archivo(s).')
        else:
            print("¡Error! parametro no valido.")
        return None
    #COMANDO REMOVE
    elif (comando == 'remove'):
        if (parametro == 'path'):
            script.setPath(valor)
        elif (parametro == 'ejecutar'):
            if script.errors == 0:
                if (os.path.isfile(script.getPath())):
                    os.remove(script.getPath())
                elif (os.path.isdir(script.getPath())):
                    os.rmdir(script.getPath())
            else:
                print("¡Error! no se pudo eliminar la carpeta o el archivo.")
        else:
            print("¡Error! parametro no valido.")
        return None
    #COMANDO EDIT
    elif (comando == 'edit'):
        if (parametro == 'path'):
            script.setPath(valor)
        elif (parametro == 'cont'):
            script.setCont(valor)
        elif (parametro == 'ejecutar'):
            contenido = ""
            #leer archivo
            try:
                with open(script.getCont(), "r") as archivo:
                    contenido = archivo.read()
            except FileNotFoundError:
                print(f"¡Error! el archivo no existe.")
            #escribir contenido a archivo
            try:
                with open(script.getPath(), "a") as archivo:
                    archivo.write(contenido)
            except FileNotFoundError:
                print(f"¡Error! el archivo no existe.")
            print("¡Archivo editado exitosamente!")
        else:
            print("¡Error! parametro no valido.")
        return None
    #COMANDO RENAME
    elif (comando == 'rename'):
        if (parametro == 'path'):
            script.setPath(valor)
        elif (parametro == 'name'):
            script.setName(valor)
        elif (parametro == 'ejecutar'):
            nueva_ruta = os.path.join(os.path.dirname(script.getPath()), script.getName())
            try:
                os.rename(script.getPath(), nueva_ruta)
                print(f"La carpeta o archivo en '{script.getPath()}' ha sido renombrado a '{script.getName()}'.")
            except FileNotFoundError:
                print(f"La carpeta o archivo en '{script.getPath()}' no existe.")
            except FileExistsError:
                print(f"Ya existe un archivo o carpeta con el nombre '{script.getName()}'.")
            except Exception as e:
                print(f"Ocurrió un error al renombrar: {str(e)}")
        else:
            print("¡Error! parametro no valido.")
        return None
    #COMANDO MKDIR
    elif (comando == 'mkdir'):
        if (parametro == 'path'):
            script.setPath(valor)
        elif (parametro == 'r'):
            script.setR(True)
        elif (parametro == 'ejecutar'):
            if (script.getR()):
                try:
                    os.makedirs(script.getPath())
                except FileNotFoundError as ex:
                    print(ex)
            else:
                try:
                    os.mkdir(script.getPath())
                except FileNotFoundError as ex:
                    print(ex)
        else:
            print("¡Error! parametro no valido.")
        return None
    #COMANDO COPY
    elif (comando == 'copy'):
        if (parametro == 'path'):
            script.setPath(valor)
        elif (parametro == 'destino'):
            script.setDestino(valor)
        elif (parametro == 'ejecutar'):
            if (os.path.isfile(script.getPath())):
                shutil.copy(script.getPath(), script.getDestino())
            elif (os.path.isdir(script.getPath())):
                shutil.copytree(script.getPath(), os.path.join(script.getDestino(), os.path.basename(script.getPath())))
        else:
            print("¡Error! parametro no valido.")
        return None
    #COMANDO MOVE
    elif (comando == 'move'):
        if (parametro == 'path'):
            script.setPath(valor)
        elif (parametro == 'destino'):
            script.setDestino(valor)
        elif (parametro == 'ejecutar'):
            shutil.move(script.getPath(), script.getDestino())
        else:
            print("¡Error! parametro no valido.")
        return None
    #COMANDO FIND
    elif (comando == 'find'):
        if (parametro == 'path'):
            pass
        elif (parametro == 'name'):
            pass
        elif (parametro == 'ejecutar'):
            pass
        else:
            print("¡Error! parametro no valido.")
        return None
    #COMANDO CHOWN
    elif (comando == 'chown'):
        if (parametro == 'path'):
            script.setPath(valor)
        elif (parametro == 'user'):
            script.setName(valor)
        elif (parametro == 'r'):
            script.setR(True)
        elif (parametro == 'ejecutar'):
            pass
        else:
            print("¡Error! parametro no valido.")
        return None
    #COMANDO CHGRP
    elif (comando == 'chgrp'):
        if (parametro == 'user'):
            script.setUser(valor)
        elif (parametro == 'grp'):
            script.setGrp(valor)
        elif (parametro == 'ejecutar'):
            usuario_existe = False
            grupo_existe = False
            cont = ""
            gid = None
            pos = None
            #leer archivo users.txt
            with open("users.txt", "r") as archivo:
                lineas = archivo.readlines()
            for i, linea in enumerate(lineas):
                usuario_grupo = linea.strip().split(", ")
                if (usuario_grupo[1] == "G"):
                    if (script.getGrp() in usuario_grupo):
                        grupo_existe = True
                        gid = usuario_grupo[0]
                if (usuario_grupo[1] == "U"):
                    if (script.getUser() in usuario_grupo):
                        cont = usuario_grupo[3] + ", " + usuario_grupo[4] + "\n"
                        usuario_existe = True
                        pos = i
            if (grupo_existe):
                if (usuario_existe):
                    lineas[pos] = gid + ", U, " + script.getGrp() + " " + cont
                    #escribir las líneas de nuevo en el archivo
                    with open("users.txt", 'w') as archivo:
                        archivo.writelines(lineas)
                    print("¡Usuario cambiado de grupo exitosamente!")
                else:
                    print("¡Error! el usuario a cambiar no existe")
            else:
                print("¡Error! el grupo no existe")
        else:
            print("¡Error! parametro no valido.")
        return None
    #COMANDO CHMOD
    elif (comando == 'chmod'):
        if (parametro == 'path'):
            script.setPath(valor)
        elif (parametro == 'ugo'):
            script.setUgo(valor)
        elif (parametro == 'r'):
            script.setR(True)
        elif (parametro == 'ejecutar'):
            pass
        else:
            print("¡Error! parametro no valido.")
        return None
    #COMANDO PAUSE
    elif (comando == 'pause'):
        while True: 
            tecla = input("\033[1;33m<<Confirm>> {}\033[00m\n" .format("Presione 'ENTER' para continuar "))
            if (tecla == ""):
                break
        return None
    #COMANDO EXECUTE
    elif (comando == 'execute'):
        if (parametro == "path"):
            print("leyendo ruta del archivo...")
            script.setPath(valor)
        elif (parametro == 'ejecutar'):
            if script.errors == 0:
                with open(script.getPath(), 'r') as archivo:
                    contenido = archivo.read()
                print("\033[36m<<System>> {}\033[00m" .format("...Comando execute ejecutado"))
                return contenido
            else:
                print("\033[91m<<Error>> {}\033[00m" .format("No se pudo ejecutar el archivo."))
        else:
            script.errors += 1
            print("\033[91m<<Error>> {}\033[00m" .format("Parametro no valido."))
        return None
    #COMANDO REP
    elif (comando == "rep"):
        if (parametro == "name"):
            print("leyendo nombre del reporte...")
            script.setName(valor)
        elif (parametro == "path"):
            print("leyendo ruta del reporte...")
            script.setPath(valor)
        elif (parametro == "id"):
            print("leyendo id de la particion...")
            script.setId(valor)
        elif (parametro == "ruta"):
            print("leyendo ruta del reporte...")
            script.setRuta(valor)
        elif (parametro == "ejecutar"):
            if (script.errors == 0):
                #buscar particion o disco
                if script.getId() != "":
                    if script.getId() in particiones_montadas:   
                        path = particiones_montadas[script.getId()]
                if not(os.path.exists(path)):
                    return None
                #obtener mbr
                mbr = Mbr()
                with open(path, 'rb+') as archivo:
                    archivo.seek(0)
                    contenido = archivo.read(mbr.getLength())
                mbr = mbr.unpack_data(contenido)
                #obtener particiones
                pos = 21
                for i in range(4):
                    particion = Partition()
                    with open(path, 'rb+') as archivo:
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
                if (script.getName().lower() == "mbr"):
                    generarReporteMBR(path, script.getPath())
                elif (script.getName().lower() == "disk"):
                    generarReporteDisco(path, script.getPath())
                print("\033[1;32m<<Success>> {}\033[00m" .format("Reporte generado exitosamente."))
                print("\033[36m<<System>> {}\033[00m" .format("...Comando rep ejecutado"))
            if (script.errors != 0):
                print("\033[91m<<Error>> {}\033[00m" .format("No se pudo generar el reporte."))
        else:
            script.errors += 1
            print("\033[91m<<Error>> {}\033[00m" .format("Parametro no valido."))
        return None
    elif (comando[0] == "#"):
        print("\033[90m<<Comment>> {}\033[00m".format(comando[1:]))
        return None

#FUNCIONES
def generarCodigo():
    code = list(range(1001, 1030))
    random.shuffle(code)
    return code.pop()

def generarReporteMBR(path, pathReport):
    code = 'digraph G {\n'
    code += '  subgraph cluster { margin="0.0" penwidth="1.0"\n'
    code += '    tbl [shape=none fontname="Arial" label=<\n'
    code += '        <table border="1" cellborder="0" cellspacing="0">\n'
    #obtener mbr
    code += '        <tr>\n'
    code += '            <td bgcolor="springgreen4" align="left"><font color="white"> REPORTE DE MBR </font></td>\n'
    code += '            <td bgcolor="springgreen4" align="left"><font color="white"> </font></td>\n'
    code += '        </tr>\n'
    mbr = Mbr()
    with open(path, 'rb+') as archivo:
        archivo.seek(0)
        contenido = archivo.read(mbr.getLength())
    mbr = mbr.unpack_data(contenido)
    code += '        <tr>\n'
    code += '            <td bgcolor="white" align="center"> mbr_tamño </td>\n'
    code += '            <td bgcolor="white" align="left"> ' + str(mbr.getTamano()) + ' </td>\n'
    code += '        </tr>\n'
    code += '        <tr>\n'
    code += '            <td bgcolor="white" align="center"> mbr_fecha_creacion </td>\n'
    code += '            <td bgcolor="white" align="left"> ' + str(mbr.getFecha_creacion()) + ' </td>\n'
    code += '        </tr>\n'
    code += '        <tr>\n'
    code += '            <td bgcolor="white" align="center"> mbr_disk_signature </td>\n'
    code += '            <td bgcolor="white" align="left"> ' + str(mbr.getDsk_signature()) + ' </td>\n'
    code += '        </tr>\n'
    #obtener particiones
    pos = mbr.getLength()
    for i in range(4):
        particion = Partition()
        with open(path, 'rb+') as archivo:
            archivo.seek(pos)
            contenido = archivo.read(particion.getLength())
        particion = particion.unpack_data(contenido)
        mbr.getPartitions()[i] = particion
        code += '        <tr>\n'
        code += '            <td bgcolor="teal" align="left"><font color="white"> Particion </font></td>\n'
        code += '            <td bgcolor="teal" align="left"><font color="white"> </font></td>\n'
        code += '        </tr>\n'
        code += '        <tr>\n'
        code += '            <td bgcolor="white" align="center"> part_status </td>\n'
        code += '            <td bgcolor="white" align="left"> ' + mbr.getPartitions()[i].getPart_status() + ' </td>\n'
        code += '        </tr>\n'
        code += '        <tr>\n'
        code += '            <td bgcolor="white" align="center"> part_type </td>\n'
        code += '            <td bgcolor="white" align="left"> ' + mbr.getPartitions()[i].getPart_type() + ' </td>\n'
        code += '        </tr>\n'
        code += '        <tr>\n'
        code += '            <td bgcolor="white" align="center"> part_fit </td>\n'
        code += '            <td bgcolor="white" align="left"> ' + mbr.getPartitions()[i].getPart_fit() + ' </td>\n'
        code += '        </tr>\n'
        code += '        <tr>\n'
        code += '            <td bgcolor="white" align="center"> part_start </td>\n'
        code += '            <td bgcolor="white" align="left"> ' + str(mbr.getPartitions()[i].getPart_start()) + ' </td>\n'
        code += '        </tr>\n'
        code += '        <tr>\n'
        code += '            <td bgcolor="white" align="center"> part_size </td>\n'
        code += '            <td bgcolor="white" align="left"> ' + str(mbr.getPartitions()[i].getPart_s()) + ' </td>\n'
        code += '        </tr>\n'
        code += '        <tr>\n'
        code += '            <td bgcolor="white" align="center"> part_name </td>\n'
        code += '            <td bgcolor="white" align="left"> ' + mbr.getPartitions()[i].getPart_name().rstrip("\x00") + ' </td>\n'
        code += '        </tr>\n'
        pos += particion.getLength()
    code += '        </table>\n'
    code += '    >];\n'
    code += '  }\n'
    code += '}'

    with open("reporte_mbr.dot", "w") as archivo:
        archivo.write(code)

    #src = graphviz.Source(code)
    #src.render('graph', format='png')
    G = pgv.AGraph("reporte_mbr.dot")
    G.draw(pathReport, prog="dot", format=os.path.splitext(os.path.basename(pathReport))[1][1:])

def generarReporteEBR(path, pathReport):
    code =  'digraph G {\n'
    code += '  subgraph cluster { margin="0.0" penwidth="1.0"\n'
    code += '    tbl [shape=none fontname="Arial" label=<\n'
    code += '        <table border="1" cellborder="0" cellspacing="0">\n'
    code += '        <tr>\n'
    code += '            <td bgcolor="teal" align="left"><font color="white"> Particion </font></td>\n'
    code += '            <td bgcolor="teal" align="left"><font color="white"> </font></td>\n'
    code += '        </tr>\n'
    code += '        <tr>\n'
    code += '            <td bgcolor="white" align="center"> part_status </td>'
    code += '            <td bgcolor="white" align="left"> 1024 </td>'
    code += '        </tr>\n'
    code += '        </table>\n'
    code += '    >];\n'
    code += '  }\n'
    code += '}'

def generarReporteDisco(path, pathReport):
    code =  'digraph G {\n'
    code += '    subgraph cluster { margin="5.0" penwidth="1.0" bgcolor="#68d9e2"\n'
    code += '        node [style="rounded" style=filled fontname="Arial" fontsize="16" margin=0.3];\n'
    label = ''
    #obtener mbr
    mbr = Mbr()
    with open(path, 'rb+') as archivo:
        archivo.seek(0)
        contenido = archivo.read(mbr.getLength())
    mbr = mbr.unpack_data(contenido)
    label += 'MBR'
    #obtener particiones
    pos = mbr.getLength()
    for i in range(4):
        particion = Partition()
        with open(path, 'rb+') as archivo:
            archivo.seek(pos)
            contenido = archivo.read(particion.getLength())
        particion = particion.unpack_data(contenido)
        mbr.getPartitions()[i] = particion
        if (mbr.getPartitions()[i].getPart_type().lower() == "p"):
            label += '|Primaria'
        elif (mbr.getPartitions()[i].getPart_type().lower() == "e"):
            label += '|{Extendida|{EBR|Logica}}'
        pos += particion.getLength()
    #label += '|Libre\\n25% del disco|{Extendida|{EBR|Logica|EBR|Logica}}'
    code += '        node_disk [shape="record" label="' + label + '"];\n'
    code += '    }\n'
    code += '}'

    with open("reporte_disco.dot", "w") as archivo:
        archivo.write(code)

    G = pgv.AGraph("reporte_disco.dot")
    G.draw(pathReport, prog="dot", format=os.path.splitext(os.path.basename(pathReport))[1][1:])


#convertir a binario
'''
name = struct.pack('16s', script.getName().encode('utf-8'))
name = struct.unpack('16s', name)
name = name[0].decode('utf-8')
'''