import os

ARCHIVO = "notas.txt"

def registrar_estudiante(nombre, nota1, nota2, nota3):
    if nombre != "" and nota1 >= 0 and nota2 >= 0 and nota3 >= 0:
        promedio = (nota1 + nota2 + nota3) / 3
        if promedio >= 7:
            estado = "APROBADO"
        else:
            estado = "REPROBADO"

        archivo = open(ARCHIVO, "a")
        archivo.write(
            nombre + "," +
            str(nota1) + "," +
            str(nota2) + "," +
            str(nota3) + "," +
            str(promedio) + "," +
            estado + "\n"
        )
        archivo.close()
        print("Registro guardado")
    else:
        print("Datos incorrectos")


def listar_registros():
    if os.path.exists(ARCHIVO):
        f = open(ARCHIVO)
        print("-" * 70)
        for linea in f:
            datos = linea.strip().split(",")
            print(
                datos[0],
                datos[1],
                datos[2],
                datos[3],
                datos[4],
                datos[5]
            )
        f.close()
    else:
        print("No existen registros")


def mostrar_resumen():
    if os.path.exists(ARCHIVO):
        f = open(ARCHIVO)
        aprobados = 0
        reprobados = 0

        for x in f:
            d = x.strip().split(",")

            if d[5] == "APROBADO":
                aprobados += 1
            else:
                reprobados += 1

        f.close()

        print("Aprobados:", aprobados)
        print("Reprobados:", reprobados)


registrar_estudiante("Ana", 8, 9, 10)
registrar_estudiante("Luis", 5, 6, 4)
registrar_estudiante("Carlos", 7, 8, 6)

listar_registros()
mostrar_resumen()