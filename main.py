from analizador.gramatica import analizador

if __name__ == '__main__':
    #execute -path=/home/luis_tavico/Escritorio/prueba.adsj
    #execute -path="/home/luis_tavico/Escritorio/prueba2.adsj"
    #rep -path=/home/luis_tavico/Escritorio/Disco1.dsk
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
    while True:
        entrada = input("App> ")
        if entrada == 'exit': break
        waiting_scripts = analizador(entrada)
        while (waiting_scripts != None):
            waiting_scripts = analizador(waiting_scripts)