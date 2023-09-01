import os

'''
with open('users.txt', 'w') as archivo:
    archivo.write("1, G, root\n")
    archivo.write("1, U, root, root, 123\n")
'''


def setPath(path):
    nueva_path = path.replace("user", "luis_tavico").replace('"', "")
    if (not os.path.exists(nueva_path)):
        print("¡Error! el disco no existe.")

path = '"/home/user/Escritorio/carpetaB"'
setPath(path)