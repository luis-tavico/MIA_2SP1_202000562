import ply.lex as lex
import ply.yacc as yacc
from scripts import *

errors = []

reserved_words = {
    #Comandos
    'mkdisk': 'MKDISK',
    'rmdisk': 'RMDISK',
    'pause' : 'PAUSE',
    #Parametros
    'size': 'SIZE',
    'path': 'PATH',
    'fit': 'FIT',
    'unit': 'UNIT',
    #Valores
}

tokens = [
    'GUION',
    'IGUAL',
    'RUTA',
    'AJUSTE',
    'UNIDAD',
    'ENTERO',
    'CADENA'
] + list(reserved_words.values())

t_ignore = ' \t'
t_GUION = r'-'
t_IGUAL = r'='

def t_RUTA(t):
    r'(\"(\/(\w|\s)+)+\.dsk\")|((\/\w+)+\.dsk)'
    return t

def t_AJUSTE(t):
    r'BF|FF|WF'
    return t

def t_UNIDAD(t):
    r'K|M'
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print(f"Error al convertir {t.value} a entero")
        t.value = 0
    return t

def t_CADENA(t):
    r'[a-zA-z_][a-zA-z_0-9]*'
    t.type = reserved_words.get(t.value, 'CADENA')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print(f"Caracter {t.value[0]} ilegal")
    t.lexer.skip(1)

lexer = lex.lex()

precedence = ( )

def p_instrucciones_lista(t):
    '''instrucciones    : instruccion instrucciones
                        | instruccion '''

def p_instrucciones_evaluar(t):
    '''instruccion : comando declaraciones
                   | comando  '''
    comando_ejecutar("ejecutar", None)
    
def p_comando(t):
    '''comando : MKDISK
               | RMDISK
               | PAUSE '''
    comando_activar(str(t[1]))

def p_declaraciones(t):
    '''declaraciones : declaracion declaraciones
                     | declaracion '''

def p_declaracion(t):
    'declaracion : GUION parametro IGUAL valor'
    comando_ejecutar(str(t[2]), str(t[4]))

def p_parametro(t):
    '''parametro : SIZE
                 | PATH
                 | FIT
                 | UNIT '''
    t[0] = t[1]

def p_valor(t):
    '''valor : ENTERO
             | RUTA
             | AJUSTE
             | UNIDAD '''
    t[0] = t[1]    

def p_error(t):
    print(f"Error sintáctico en {t}")

parser = yacc.yacc()
    
f = open("./entrada.txt", "r")
input = f.read()
parser.parse(input)
