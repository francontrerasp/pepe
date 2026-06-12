""" El complejo educacional “Chile 2030”, desea realizar una
aplicación computacional que le permita registrar en sus
establecimientos los alumnos a sus cursos.
2
Por tal razón le ha solicitado que cree un programa que le permita
a coordinación estudiantil registrar los alumnos que pertenezcan a
un curso en particular.
Como prototipo, usted desarrolla un algoritmo que permite
almacenar un número variable de alumnos a un curso, pero con
un máximo de 30 por curso """

while True:
    try:
        cant_alumnos = int(input("Ingrese la cantidad de alumnos a registrar: "))
        if cant_alumnos > 0 and cant_alumnos <= 30:
            break
        raise ValueError
    except:
        print("La cantidada no puede ser superior a 30 y debe ser un numero entero positivo")

lista_alumnos = []

for i in range(cant_alumnos):
    print("------Datos del alumno nro------ ", i+1)
    alumno = {}
    alumno["nombre"] = input("ingrese nombre del alumno: ")
    alumno["direccion"] = input("ingrese direccion de alumno: ")
    alumno["telefono"] = input("ingrese telefono de alumno: ")
    lista_alumnos.append(alumno)

print(lista_alumnos)