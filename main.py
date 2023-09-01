from analizador.gramatica import analizador

if __name__ == '__main__':
    #execute -path=/home/luis_tavico/Escritorio/prueba.eea
    #rep -path=/home/luis_tavico/Escritorio/Disco1.dsk
    #fdisk -path=/home/luis_tavico/Escritorio/Disco1.dsk -name=Part1 -unit=B -size=200
    #fdisk -path=/home/luis_tavico/Escritorio/Disco1.dsk -name=Part2 -unit=B -size=150
    #edit -path=/home/user/Escritorio/a.txt -cont=/home/user/Escritorio/b.txt
    while True:
        entrada = input("App> ")
        waiting_scripts = analizador(entrada)
        while (waiting_scripts != None):
            waiting_scripts = analizador(waiting_scripts)
        r = input("continuar(s/n): ")
        if (r == "n") : break