"""
Trabajo Práctico Integrador (TPI) - Programación 1
Tecnicatura Universitaria en Programación a Distancia - UTN
Tema: Gestión de Datos de Países en Python: filtros, ordenamientos y estadísticas.
"""

import csv
import os
import unicodedata


def normalizar(texto):
    """Pasa a minúsculas y quita tildes y espacios extra, para comparar
    textos sin distinguir 'Perú' de 'peru'."""
    sin_tildes = unicodedata.normalize("NFD", texto)
    sin_tildes = "".join(c for c in sin_tildes if unicodedata.category(c) != "Mn")
    return sin_tildes.strip().lower()


def cargar_datos_csv(nombre_archivo):
    """Lee el archivo CSV y retorna una lista de diccionarios con los países.
    Controla errores de formato y archivo inexistente.
    """
    paises = []
    if not os.path.exists(nombre_archivo):
        print(f"Aviso: No se encontró '{nombre_archivo}'. Se creará un dataset base.")
        crear_csv_ejemplo(nombre_archivo)

    try:
        with open(nombre_archivo, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            columnas_esperadas = {"nombre", "poblacion", "superficie", "continente"}
            if not lector.fieldnames or not columnas_esperadas.issubset(set(lector.fieldnames)):
                print("Error: El archivo CSV no contiene las columnas requeridas.")
                return paises

            for num_linea, fila in enumerate(lector, start=2):
                try:
                    nombre = fila["nombre"].strip()
                    continente = fila["continente"].strip()
                    poblacion = int(fila["poblacion"].strip())
                    superficie = int(fila["superficie"].strip())

                    if not nombre or not continente or poblacion <= 0 or superficie <= 0:
                        print(f"Advertencia: Fila {num_linea} con datos inválidos omitida.")
                        continue

                    paises.append({
                        "nombre": nombre,
                        "poblacion": poblacion,
                        "superficie": superficie,
                        "continente": continente
                    })
                except (ValueError, KeyError, AttributeError):
                    print(f"Advertencia: Error de formato en la fila {num_linea} del CSV. Omitida.")

        print(f"¡Datos cargados exitosamente! Total de países: {len(paises)}")
    except Exception as e:
        print(f"Error crítico al leer el archivo CSV: {e}")

    return paises


def crear_csv_ejemplo(nombre_archivo):
    """Crea un archivo CSV inicial con registros base."""
    datos = [
        ["nombre", "poblacion", "superficie", "continente"],
        ["Argentina", "45376763", "2780400", "América"],
        ["Japón", "125800000", "377975", "Asia"],
        ["Brasil", "213993437", "8515767", "América"],
        ["Alemania", "83149300", "357022", "Europa"]
    ]
    with open(nombre_archivo, mode="w", encoding="utf-8", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(datos)


def guardar_datos_csv(nombre_archivo, paises):
    """Persiste la lista actual de países en el archivo CSV."""
    try:
        with open(nombre_archivo, mode="w", encoding="utf-8", newline="") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["nombre", "poblacion", "superficie", "continente"])
            for p in paises:
                escritor.writerow([p["nombre"], p["poblacion"], p["superficie"], p["continente"]])
        print(f"Datos guardados correctamente en '{nombre_archivo}'.")
    except Exception as e:
        print(f"Error al guardar los datos en el CSV: {e}")


def mostrar_tabla_paises(lista_paises):
    """Imprime en consola una tabla formateada con los países recibidos."""
    if not lista_paises:
        print("No hay países para mostrar.")
        return
    print(f"\n{'Nombre':<20} | {'Población':>15} | {'Superficie (km²)':>18} | {'Continente':<15}")
    print("-" * 77)
    for p in lista_paises:
        print(f"{p['nombre']:<20} | {p['poblacion']:>15,d} | {p['superficie']:>18,d} | {p['continente']:<15}")


def pedir_entero_positivo(mensaje, permitir_cero=False):
    """Solicita y valida un número entero mayor que cero.
    Con permitir_cero=True acepta también el 0 (útil para rangos de filtro)."""
    minimo = 0 if permitir_cero else 1
    while True:
        valor = input(mensaje).strip()
        try:
            numero = int(valor)
            if numero < minimo:
                if permitir_cero:
                    print("Error: El valor no puede ser negativo. Intente nuevamente.")
                else:
                    print("Error: El valor debe ser mayor que cero. Intente nuevamente.")
            else:
                return numero
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")


def agregar_pais(paises):
    """Agrega un nuevo país validando campos no vacíos y evitando duplicados."""
    print("\n--- AGREGAR NUEVO PAÍS ---")
    nombre = input("Nombre del país: ").strip()
    if not nombre:
        print("Error: El nombre del país no puede estar vacío.")
        return

    for p in paises:
        if normalizar(p["nombre"]) == normalizar(nombre):
            print(f"Error: El país '{nombre}' ya se encuentra registrado.")
            return

    poblacion = pedir_entero_positivo("Población: ")
    superficie = pedir_entero_positivo("Superficie en km²: ")

    continente = input("Continente: ").strip()
    if not continente:
        print("Error: El continente no puede estar vacío.")
        return

    paises.append({
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    })
    print(f"¡País '{nombre}' agregado con éxito!")


def actualizar_pais(paises):
    """Actualiza población y superficie de un país existente."""
    print("\n--- ACTUALIZAR DATOS DE UN PAÍS ---")
    if not paises:
        print("No hay países cargados en el sistema.")
        return

    busqueda = normalizar(input("Ingrese el nombre del país a actualizar: "))
    if not busqueda:
        print("Error: Debe ingresar un nombre.")
        return

    coincidencias = [p for p in paises if busqueda in normalizar(p["nombre"])]
    if not coincidencias:
        print("No se encontraron países con ese criterio.")
        return

    print("\nPaíses encontrados:")
    for idx, p in enumerate(coincidencias, start=1):
        print(f"{idx}. {p['nombre']} (Pob: {p['poblacion']:,d} | Sup: {p['superficie']:,d} km²)")

    try:
        seleccion = int(input("Seleccione el número de país a modificar: ").strip())
        if seleccion < 1 or seleccion > len(coincidencias):
            print("Error: Selección fuera de rango.")
            return
    except ValueError:
        print("Error: Debe ingresar un número válido.")
        return

    pais = coincidencias[seleccion - 1]
    print(f"Editando: {pais['nombre']}")
    pais["poblacion"] = pedir_entero_positivo("Nueva población: ")
    pais["superficie"] = pedir_entero_positivo("Nueva superficie en km²: ")
    print(f"¡Datos de '{pais['nombre']}' actualizados correctamente!")


def buscar_pais(paises):
    """Busca países por coincidencia parcial o exacta en el nombre."""
    print("\n--- BUSCAR PAÍS POR NOMBRE ---")
    termino = normalizar(input("Ingrese el nombre o parte del nombre: "))
    if not termino:
        print("Error: El término de búsqueda no puede estar vacío.")
        return

    resultados = [p for p in paises if termino in normalizar(p["nombre"])]
    if resultados:
        print(f"Se encontraron {len(resultados)} resultado(s):")
        mostrar_tabla_paises(resultados)
    else:
        print("No se encontraron países que coincidan con la búsqueda.")


def filtrar_paises(paises):
    """Filtra países por continente, rango de población o rango de superficie."""
    print("\n--- FILTRAR PAÍSES ---")
    print("1. Filtrar por Continente")
    print("2. Filtrar por Rango de Población")
    print("3. Filtrar por Rango de Superficie")
    opcion = input("Seleccione una opción (1-3): ").strip()

    resultados = []
    if opcion == "1":
        continente = normalizar(input("Ingrese el continente: "))
        if not continente:
            print("Error: El continente no puede estar vacío.")
            return
        resultados = [p for p in paises if normalizar(p["continente"]) == continente]

    elif opcion == "2":
        min_pob = pedir_entero_positivo("Población mínima: ", permitir_cero=True)
        max_pob = pedir_entero_positivo("Población máxima: ", permitir_cero=True)
        if min_pob > max_pob:
            print("Error: La población mínima no puede ser mayor a la máxima.")
            return
        resultados = [p for p in paises if min_pob <= p["poblacion"] <= max_pob]

    elif opcion == "3":
        min_sup = pedir_entero_positivo("Superficie mínima (km²): ", permitir_cero=True)
        max_sup = pedir_entero_positivo("Superficie máxima (km²): ", permitir_cero=True)
        if min_sup > max_sup:
            print("Error: La superficie mínima no puede ser mayor a la máxima.")
            return
        resultados = [p for p in paises if min_sup <= p["superficie"] <= max_sup]

    else:
        print("Error: Opción de filtro inválida.")
        return

    if resultados:
        print(f"\nResultados del filtro ({len(resultados)} país/es):")
        mostrar_tabla_paises(resultados)
    else:
        print("No se encontraron países que cumplan con el filtro ingresado.")


def ordenar_paises(paises):
    """Ordena los países por nombre, población o superficie (ascendente/descendente)."""
    print("\n--- ORDENAR PAÍSES ---")
    if not paises:
        print("No hay países para ordenar.")
        return

    print("1. Ordenar por Nombre")
    print("2. Ordenar por Población")
    print("3. Ordenar por Superficie")
    criterio = input("Seleccione criterio (1-3): ").strip()

    if criterio not in {"1", "2", "3"}:
        print("Error: Criterio inválido.")
        return

    print("1. Ascendente (A-Z / Menor a Mayor)")
    print("2. Descendente (Z-A / Mayor a Menor)")
    sentido = input("Seleccione orden (1-2): ").strip()

    if sentido not in {"1", "2"}:
        print("Error: Sentido de ordenamiento inválido.")
        return

    descendente = (sentido == "2")

    if criterio == "1":
        ordenados = sorted(paises, key=lambda x: normalizar(x["nombre"]), reverse=descendente)
    elif criterio == "2":
        ordenados = sorted(paises, key=lambda x: x["poblacion"], reverse=descendente)
    else:
        ordenados = sorted(paises, key=lambda x: x["superficie"], reverse=descendente)

    mostrar_tabla_paises(ordenados)


def mostrar_estadisticas(paises):
    """Calcula y muestra indicadores clave sobre el dataset de países."""
    print("\n--- ESTADÍSTICAS DEL DATASET ---")
    if not paises:
        print("No hay datos cargados para calcular estadísticas.")
        return

    mayor_pob = max(paises, key=lambda x: x["poblacion"])
    menor_pob = min(paises, key=lambda x: x["poblacion"])

    suma_pob = sum(p["poblacion"] for p in paises)
    suma_sup = sum(p["superficie"] for p in paises)
    cantidad = len(paises)

    promedio_pob = suma_pob / cantidad
    promedio_sup = suma_sup / cantidad

    paises_por_continente = {}
    for p in paises:
        cont = p["continente"]
        paises_por_continente[cont] = paises_por_continente.get(cont, 0) + 1

    print(f"• Total de países registrados: {cantidad}")
    print(f"• País con mayor población: {mayor_pob['nombre']} ({mayor_pob['poblacion']:,d} hab.)")
    print(f"• País con menor población: {menor_pob['nombre']} ({menor_pob['poblacion']:,d} hab.)")
    print(f"• Promedio de población: {promedio_pob:,.2f} hab.")
    print(f"• Promedio de superficie: {promedio_sup:,.2f} km²")
    print("\n• Cantidad de países por continente:")
    for cont, total in sorted(paises_por_continente.items()):
        print(f"   - {cont}: {total} país(es)")


def mostrar_menu():
    """Despliega el menú principal de opciones en consola."""
    print("\n" + "=" * 46)
    print("   SISTEMA DE GESTIÓN DE PAÍSES - TPI UTN")
    print("=" * 46)
    print("1. Agregar un país")
    print("2. Actualizar población y superficie de un país")
    print("3. Buscar un país por nombre")
    print("4. Filtrar países")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas")
    print("7. Guardar y Salir")
    print("=" * 46)


def main():
    """Función principal que controla el ciclo de ejecución del programa."""
    ruta_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), "paises.csv")
    paises = cargar_datos_csv(ruta_csv)

    try:
        while True:
            mostrar_menu()
            opcion = input("Ingrese una opción (1-7): ").strip()

            if opcion == "1":
                agregar_pais(paises)
            elif opcion == "2":
                actualizar_pais(paises)
            elif opcion == "3":
                buscar_pais(paises)
            elif opcion == "4":
                filtrar_paises(paises)
            elif opcion == "5":
                ordenar_paises(paises)
            elif opcion == "6":
                mostrar_estadisticas(paises)
            elif opcion == "7":
                guardar_datos_csv(ruta_csv, paises)
                print("Programa finalizado. ¡Hasta luego!")
                break
            else:
                print("Opción inválida. Por favor, seleccione un número del 1 al 7.")
    except (KeyboardInterrupt, EOFError):
        # Si se interrumpe el programa (Ctrl+C), se guardan los cambios para no perderlos.
        print("\nEjecución interrumpida.")
        guardar_datos_csv(ruta_csv, paises)


if __name__ == "__main__":
    main()
