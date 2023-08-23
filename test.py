txt = '"/home/user/Disco1.dsk"'
x = txt.split("/")[-1].replace('"', '')
print(x)