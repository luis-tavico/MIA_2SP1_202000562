from analizador.gramatica import analizador

if __name__ == '__main__':
    #mkdisk -size=-2 -unit=K -path=/home/user/Escritorio/Disco1.dsk
    #mkdisk -size=1 -unit=K -path=/home/user/Escritorio/Discos/Disco2.dsk
    #rmdisk -path=/home/user/Escritorio/Disco1.dsk
    #fdisk -path=/home/user/Escritorio/Disco1.dsk -name=Part1 -unit=B -size=200
    #fdisk -path=/home/user/Escritorio/Disco1.dsk -name=Part2 -unit=B -size=300
    #fdisk -path=/home/user/Escritorio/Disco1.dsk -name=Part3 -unit=B -size=125
    #fdisk -path=/home/user/Escritorio/Disco1.dsk -name=Part4 -unit=B -size=250
    #fdisk -delete=full -name=Part1 -path=/home/user/Escritorio/Disco1.dsk
    #fdisk -add=100 -path=/home/user/Escritorio/Disco1.dsk -name=Part1 -unit=B
    #mount -path=/home/user/Escritorio/Disco1.dsk -name=Part2
    #unmount -id=623Disco1
    #AQUI EMPIEZA EL DOC
    #mkfile -size=15 -path=/home/user/Escritorio/a.txt -r
    #mkfile -size=10 -path=/home/user/Escritorio/b.txt -r
    #cat -file1="/home/user/Escritorio/a.txt" -file2="/home/user/Escritorio/b.txt"
    #remove -path=/home/user/Escritorio/a.txt
    #edit -path=/home/user/Escritorio/b.txt -cont=/home/user/Escritorio/c.txt
    #rename -path=/home/user/Escritorio/a.txt -name=fileA.txt
    #mkdir -r -path=/home/user/Escritorio/usac
    #copy -path="/home/user/Escritorio/b.txt" -destino="/home/user/Escritorio/usac"
    #move -path="/home/user/Escritorio/c.txt" -destino=/home/user/Escritorio/usac
    #execute -path=/home/user/Escritorio/prueba.adsj
    #chgrp -user=user1 -grp=invitados
    #rep -id=623Disco1 -path=/home/user/Escritorio/reports/reporte1.jpg -name=mbr
    #rep -id=623Disco1 -path=/home/user/Escritorio/reports/reporte2.png -name=disk
    while True:
        entrada = input("App> ")
        if entrada == 'exit': break
        waiting_scripts = analizador(entrada)
        while (waiting_scripts != None):
            waiting_scripts = analizador(waiting_scripts)