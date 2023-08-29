import ply.lex as lex
import ply.yacc as yacc
from scripts import *

errors = []

reserved_words = {
    #Comandos
    'mkdisk': 'MKDISK',
    'rmdisk': 'RMDISK',
    'fdisk' : 'FKDISK',
    'pause' : 'PAUSE',
    'execute' : 'EXECUTE',
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
    'RUTA_ARCHIVO',
    'RUTA_DISCO',
    'AJUSTE',
    'UNIDAD',
    'ENTERO',
    'CADENA'
] + list(reserved_words.values())

t_ignore = ' \t'
t_GUION = r'-'
t_IGUAL = r'='

def t_RUTA_ARCHIVO(t):
    r'(\"(\/(\w|\s)+)+\.eea\")|((\/\w+)+\.eea)'
    return t

def t_RUTA_DISCO(t):
    r'(\"(\/(\w|\s)+)+\.dsk\")|((\/\w+)+\.dsk)'
    return t

def t_AJUSTE(t):
    r'BF|FF|WF'
    return t

def t_UNIDAD(t):
    r'B|K|M'
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

def t_COMENTARIO(t):
    r'\#.*'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print(f"Caracter {t.value[0]} ilegal")
    t.lexer.skip(1)

def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

lexer = lex.lex()

global waiting_scripts
waiting_scripts = ""

precedence = ( )

def p_instrucciones(t):
    '''instrucciones    : instruccion instrucciones
                        | instruccion '''
    global waiting_scripts
    t[0] = waiting_scripts

def p_instruccion(t):
    '''instruccion : comando declaraciones
                   | comando '''
    comando_ejecutar("ejecutar", None)

def p_comando(t):
    '''comando : MKDISK
               | RMDISK
               | FDISK
               | PAUSE'''
    comando_activar(str(t[1]))
    
def p_declaraciones(t):
    '''declaraciones : declaracion declaraciones
                     | declaracion '''

def p_declaracion(t):
    'declaracion : MAYORQUE parametro IGUAL valor'
    global waiting_scripts
    waiting_scripts = comando_ejecutar(str(t[2]), str(t[4]))

def p_parametro(t):
    '''parametro : SIZE
                 | PATH
                 | FIT
                 | UNIT
                 | NAME '''
    t[0] = t[1]

def p_valor(t):
    '''valor : ENTERO
             | RUTA_ARCHIVO
             | RUTA_DISCO
             | AJUSTE
             | UNIDAD
             | CADENA '''
    t[0] = t[1]    

def p_error(t):
    print(f"Error sintáctico en {t}")

def analizador(input):
    global errors
    global parser
    parser = yacc.yacc()
    lexer.lineno = 1
    return parser.parse(input)