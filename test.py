content = ""
for i in range (100):
    content += "\x00"  # Tu cadena de caracteres
content_binary = content.encode('latin-1')  # Convertir la cadena a bytes

# Imprimir la representación binaria
print(content_binary)