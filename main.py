from analizador.gramatica import analizador

if __name__ == '__main__':
    #mkdisk >size=1 >unit=K >path=/home/luis_tavico/Escritorio/Disco1.dsk
    #fdisk >path=/home/luis_tavico/Escritorio/Disco1.dsk >unit=B >name=Particion4 >size=150
    #fdisk >path=/home/luis_tavico/Escritorio/Disco1.dsk >unit=B >name=Particion5 >size=200
    #execute >path=/home/luis_tavico/Escritorio/prueba.eea
    while True:
        entrada = input("App> ")
        waiting_scripts = analizador(entrada)
        while (waiting_scripts != None):
            waiting_scripts = analizador(waiting_scripts)
        r = input("continuar(s/n): ")
        if (r == "n") : break