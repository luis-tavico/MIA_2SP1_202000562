from analizador.gramatica import analizador

if __name__ == '__main__':
    #execute -path=/home/user/Escritorio/basico.adsj
    #execute -path=/home/user/Escritorio/eliminar.adsj
    #execute -path=/home/user/Escritorio/prueba.adsj
    #remove -path=/home/user/Escritorio/reports
    #sudo rm -r /home/archivos
    #sudo python3.9 main.py
    while True:
        entrada = input("App> ")
        if entrada == 'exit': break
        waiting_scripts = analizador(entrada)
        while (waiting_scripts != None):
            waiting_scripts = analizador(waiting_scripts)