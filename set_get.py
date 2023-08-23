lista = ['user', 'password', 'id']

print('    #SET')
for palabra in lista:
    print("    def set" + palabra.capitalize() + '(self, '+ palabra +'):\n        self.' + palabra + ' = ' + palabra + '\n')

print('    #GET')
for palabra in lista:
    print("    def get" + palabra.capitalize() + '(self):\n        return self.' + palabra + '\n')