import os

'''
with open('users.txt', 'w') as archivo:
    archivo.write("1, G, root\n")
    archivo.write("1, U, root, root, 123\n")
'''

num = 0
contenido = ""
for i in range(30):
    if (num == 10): num = 0
    contenido += str(num)
    num += 1

print(contenido)