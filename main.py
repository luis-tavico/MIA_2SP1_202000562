from analizador.gramatica import analizador

if __name__ == '__main__':
    while True:
        entrada = input("App> ")
        if entrada == 'exit': break
        waiting_scripts = analizador(entrada)
        while (waiting_scripts != None):
            waiting_scripts = analizador(waiting_scripts)