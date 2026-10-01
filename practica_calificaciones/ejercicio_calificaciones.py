def encabezado():
    print("Reporte de calificaciones")


def nota_minima():
    return 6.0


def rendimiento(nota_final):
    if nota_final < 7.0:
        return "Reprobado"
    elif nota_final <= 9.4:
        return "Aprobado"
    else:
        return "Excelente"


def calcular_promedio(nota_examenes, nota_tareas):
    promedio = (nota_examenes * 0.70) + (nota_tareas * 0.30)
    return round(promedio, 1)


def generar_boleta(nombre_alumno, nota_examenes, nota_tareas):
    encabezado()
    nota_final = calcular_promedio(nota_examenes, nota_tareas)
    o_nota_minima = nota_minima()
    estado = rendimiento(nota_final)
    requiere_extra = "Sí" if nota_final < o_nota_minima else "No"

    print(f"Alumno: {nombre_alumno}")
    print(f"Nota final: {nota_final}")
    print(f"Estado académico: {estado}")
    print(f"Examen extraordinario requerido: {requiere_extra}")



generar_boleta("Juan Pérez", 8.0, 9.0)