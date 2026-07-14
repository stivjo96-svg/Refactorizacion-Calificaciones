import os

ARCHIVO = "notas.txt"

NOTA_APROBACION = 7

def registrar_estudiante(nombre, nota1, nota2, nota3):
    if nombre != "" and nota1 >= 0 and nota2 >= 0 and nota3 >= 0:
        promedio = (nota1 + nota2 + nota3) / 3

        if promedio >= NOTA_APROBACION:
            estado = "APROBADO"
        else:
            estado = "REPROBADO"

        with open(ARCHIVO, "a") as archivo:
            archivo.write(
                nombre + "," +
                str(nota1) + "," +
                str(nota2) + "," +
                str(nota3) + "," +
                str(promedio) + "," +
                estado + "\n"
            )

        print("Registro guardado")
    else:
        print("Datos incorrectos")


def listar_registros():
    if os.path.exists(ARCHIVO):
        print("-" * 70)

        with open(ARCHIVO, "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")

                print(
                    datos[0],
                    datos[1],
                    datos[2],
                    datos[3],
                    datos[4],
                    datos[5]
                )
    else:
        print("No existen registros")


def mostrar_resumen():
    if os.path.exists(ARCHIVO):
        aprobados = 0
        reprobados = 0

        with open(ARCHIVO, "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")

                if datos[5] == "APROBADO":
                    aprobados += 1
                else:
                    reprobados += 1

        print("Aprobados:", aprobados)
        print("Reprobados:", reprobados)


def main():
    registrar_estudiante("Ana", 8, 9, 10)
    registrar_estudiante("Luis", 5, 6, 4)
    registrar_estudiante("Carlos", 7, 8, 6)

    listar_registros()
    mostrar_resumen()


if __name__ == "__main__":
    main()