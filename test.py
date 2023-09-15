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
            if ("(" in nombre):
                nombre = nombre[:nombre.index("(")+1] + str(n) + nombre[nombre.index(")"):]
            else:
                nombre += "(" + str(n) + ")"
            pathReport = carpetas + "/" + nombre + extension
            n += 1

nuevaRuta("/home/luis_tavico/Escritorio/reports/reporte1.jpg")
nuevaRuta("/home/luis_tavico/Escritorio/reports/reporte1.jpg")
nuevaRuta("/home/luis_tavico/Escritorio/reports/reporte1.jpg")