# SISTEMA EXPERTO: DIAGNOSTICO DE FALLAS
# Metodo: Encadenamiento hacia adelante

# 1. Base de conocimientos: hechos y descripciones
descripciones = {
    "no_enciende": "El computador no enciende",
    "sin_luces": "No se encienden las luces del equipo",
    "enciende": "El computador enciende",
    "sin_imagen": "El monitor no muestra imagen",
    "reinicios_frecuentes": "El computador se reinicia frecuentemente",
    "mucho_calor": "El computador presenta mucho calor",
    "lento": "El computador funciona lentamente",
    "disco_al_100": "El disco presenta un uso cercano al 100%",

    "posible_falla_alimentacion":
        "Posible falla de alimentacion electrica",
    "revisar_cable_y_fuente":
        "Revisar el cable de corriente y la fuente de poder",

    "posible_falla_video":
        "Posible falla de pantalla o video",
    "revisar_monitor_y_video":
        "Revisar monitor, cable de video y graficos",

    "posible_sobrecalentamiento":
        "Posible sobrecalentamiento",
    "revisar_ventilacion":
        "Revisar ventiladores y sistema de ventilacion",

    "posible_saturacion_disco":
        "Posible saturacion del disco",
    "revisar_uso_disco":
        "Revisar el uso del disco y los programas de inicio"
}

# 2. Reglas de produccion
reglas = [
    {
        "nombre": "R1",
        "condiciones": ["no_enciende", "sin_luces"],
        "conclusion": "posible_falla_alimentacion"
    },
    {
        "nombre": "R2",
        "condiciones": ["posible_falla_alimentacion"],
        "conclusion": "revisar_cable_y_fuente"
    },
    {
        "nombre": "R3",
        "condiciones": ["enciende", "sin_imagen"],
        "conclusion": "posible_falla_video"
    },
    {
        "nombre": "R4",
        "condiciones": ["posible_falla_video"],
        "conclusion": "revisar_monitor_y_video"
    },
    {
        "nombre": "R5",
        "condiciones": ["reinicios_frecuentes", "mucho_calor"],
        "conclusion": "posible_sobrecalentamiento"
    },
    {
        "nombre": "R6",
        "condiciones": ["posible_sobrecalentamiento"],
        "conclusion": "revisar_ventilacion"
    },
    {
        "nombre": "R7",
        "condiciones": ["lento", "disco_al_100"],
        "conclusion": "posible_saturacion_disco"
    },
    {
        "nombre": "R8",
        "condiciones": ["posible_saturacion_disco"],
        "conclusion": "revisar_uso_disco"
    }
]

# 3. Motor de inferencia: encadenamiento hacia adelante
def encadenamiento_hacia_adelante(hechos_iniciales):
    hechos = set(hechos_iniciales)
    nuevas_conclusiones = []
    cambio = True

    print("\n--- INICIANDO MOTOR DE INFERENCIA ---")

    while cambio:
        cambio = False

        for regla in reglas:
            condiciones = regla["condiciones"]
            conclusion = regla["conclusion"]

            # Verificar si se cumplen todas las condiciones
            if all(c in hechos for c in condiciones):
                # Evitar agregar hechos repetidos
                if conclusion not in hechos:
                    hechos.add(conclusion)
                    nuevas_conclusiones.append(conclusion)
                    cambio = True

                    print(f"\n{regla['nombre']} se activa.")
                    print("  SI:", " Y ".join(condiciones))
                    print("  ENTONCES:",
                          descripciones[conclusion])

    print("\n--- FIN DEL RAZONAMIENTO ---")

    return hechos, nuevas_conclusiones

# 4. Interfaz por consola
def main():
    print("======================================")
    print(" SISTEMA EXPERTO DE SOPORTE TECNICO")
    print("======================================")

    print("\nIngrese los sintomas que presenta el equipo.")
    print("Escriba los codigos separados por comas.\n")

    sintomas = [
        "no_enciende",
        "sin_luces",
        "enciende",
        "sin_imagen",
        "reinicios_frecuentes",
        "mucho_calor",
        "lento",
        "disco_al_100"
    ]

    for i, sintoma in enumerate(sintomas, start=1):
        print(f"{i}. {descripciones[sintoma]} ({sintoma})")

    entrada = input("\nSintomas: ").lower()
    hechos_iniciales = {
        x.strip() for x in entrada.split(",") if x.strip()
    }

    # Validar los hechos ingresados
    invalidos = hechos_iniciales - set(sintomas)

    if invalidos:
        print("\nCodigos no validos:", ", ".join(invalidos))
        print("Ejecute nuevamente e ingrese los codigos indicados.")
        return

    if not hechos_iniciales:
        print("Debe ingresar al menos un sintoma.")
        return

    print("\n--- HECHOS INICIALES ---")
    for hecho in sorted(hechos_iniciales):
        print("-", descripciones[hecho])

    hechos_finales, conclusiones = (
        encadenamiento_hacia_adelante(hechos_iniciales)
    )

    print("\n--- RESULTADO DEL DIAGNOSTICO ---")

    if conclusiones:
        for conclusion in conclusiones:
            print("-", descripciones[conclusion])
    else:
        print("No se encontraron reglas aplicables.")
        print("Se requieren mas sintomas o reglas.")

    print("\nEl diagnostico es orientativo, no definitivo.")


if __name__ == "__main__":
    main()