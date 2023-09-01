import os
import random
from datetime import datetime
import shutil
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
from analizador.comandos.mkgrp import Mkgrp
from analizador.comandos.mkusr import Mkusr
from analizador.comandos.move import Move
from analizador.comandos.partition import Partition
from analizador.comandos.rename import Rename
from analizador.comandos.remove import Remove
from analizador.comandos.rmdisk import Rmdisk
from analizador.comandos.rmgrp import Rmgrp
from analizador.comandos.rmusr import Rmusr

global comando, script, usuario_actual
usuario_actual = ""

def comando_activar(valor):
    global comando, script
    comando = valor

    #comandos de discos
    if (comando.lower() == "mkdisk"):
        script = Mkdisk()
    elif (comando.lower() == "rmdisk"):
        script = Rmdisk()
    elif (comando.lower() == "fdisk"):
        script = Fdisk()
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
                print("¡Error! No existe una sesion activa.")
        return None
    #COMANDO MKGRP
    elif (comando == 'mkgrp'):
        if (parametro == 'name'):
            script.setName(valor)
        elif (parametro == 'ejecutar'):
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
        else:
            print("¡Error! parametro no valido.")
        return None
    #COMANDO RMGRP
    elif (comando == 'rmgrp'):
        if (parametro == 'name'):
            script.setName(valor)
        elif (parametro == 'ejecutar'):
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
        else:
            print("¡Error! parametro no valido.")
        return None
    #COMANDO RMUSR
    elif (comando == 'rmusr'):
        if (parametro == 'user'):
            script.setUser(valor)
        elif (parametro == 'ejecutar'):
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
            if (script.getR()):
                pass
            else:
               print(script.getPath()) 
        else:
            print("¡Error! parametro no valido.")
        return None
    #COMANDO CAT
    elif (comando == 'cat'):
        if (parametro[:4] == 'file'):
            script.setFileN(valor)
        elif (parametro == 'ejecutar'):
            for fileN in script.getFileN():
                print(fileN)
        else:
            print("¡Error! parametro no valido.")
        return None
    #COMANDO REMOVE
    elif (comando == 'remove'):
        if (parametro == 'path'):
            pass
        elif (parametro == 'ejecutar'):
            pass
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
            pass
        elif (parametro == 'name'):
            pass
        elif (parametro == 'ejecutar'):
            pass
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
            pass
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
            tecla = input("Presione 'ENTER' para continuar ")
            if (tecla == ""):
                break
        return None
    #COMANDO EXECUTE
    elif (comando == 'execute'):
        if (parametro == "path"):
            script.setPath(valor)
        elif (parametro == 'ejecutar'):
            if os.path.exists(script.getPath()):
                with open(script.getPath(), 'r') as archivo:
                    contenido = archivo.read()
                return contenido
            else:
                print("¡Error! archivo no encontrado.")
        else:
            print("¡Error! parametro no valido.")
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

#FUNCIONES
def generarCodigo():
    code = list(range(1001, 1030))
    random.shuffle(code)
    return code.pop()