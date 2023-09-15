import os


def nuevaRuta (pathReport):
    n = 1
    while True:
        if not(os.path.exists(pathReport)):
            print(pathReport)
            break
        else:
            carpetas = os.path.dirname(pathReport)
            nombre, extension = os.path.splitext(os.path.basename(pathReport))
            nombre += "(" + str(n) + ")"
            pathReport = carpetas + nombre + extension
            n += 1

nuevaRuta("/home/user/Escritorio/reports/reporte1.jpg")