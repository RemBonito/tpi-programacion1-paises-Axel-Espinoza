# Gestión de Datos de Países en Python - TPI Programación 1

**Universidad Tecnológica Nacional (UTN)**  
**Carrera:** Tecnicatura Universitaria en Programación a Distancia  
**Materia:** Programación 1  

---

## Descripción del Programa

Aplicación de consola desarrollada en **Python 3.x** para gestionar un conjunto de datos de países almacenado en formato CSV (`paises.csv`). El sistema carga los registros en memoria utilizando una lista de diccionarios y permite realizar altas, modificaciones, búsquedas por coincidencia parcial o exacta, filtros combinados/específicos, ordenamientos ascendentes o descendentes y cálculo de indicadores estadísticos.

---

## Estructura del Proyecto

* `main.py`: Código fuente principal modularizado en funciones con responsabilidad única y validaciones de entrada.
* `paises.csv`: Dataset base con columnas `nombre,poblacion,superficie,continente`.
* `Informe_Tecnico_TPI.pdf`: Documentación académica y técnica con marco teórico, diagrama de flujo, capturas de ejecución y conclusiones.
* `README.md`: Guía de uso, ejemplos y enlaces del proyecto.

---

## Instrucciones de Uso

1. Asegurate de tener instalado **Python 3.8 o superior**.
2. Cloná o descargá este repositorio en tu equipo local.
3. Abrí una terminal en la carpeta raíz del proyecto y ejecutá:
   ```bash
   python main.py
   ```
4. Seleccioná las opciones del menú numérico (`1` a `7`) para interactuar con el sistema. Los cambios (altas y actualizaciones) se guardan en `paises.csv` al elegir la opción `7` (Guardar y Salir). Si el programa se interrumpe con `Ctrl+C`, también se guardan antes de cerrar.

---

## Ejemplos de Entradas y Salidas

### Ejemplo 1: Búsqueda por coincidencia parcial (Opción 3)
**Entrada:**
```text
Ingrese una opción (1-7): 3
Ingrese el nombre o parte del nombre: arg
```
**Salida:**
```text
Se encontraron 1 resultado(s):

Nombre               |       Población |   Superficie (km²) | Continente     
-----------------------------------------------------------------------------
Argentina            |      45,376,763 |          2,780,400 | América        
```

### Ejemplo 2: Estadísticas del dataset (Opción 6)
**Entrada:**
```text
Ingrese una opción (1-7): 6
```
**Salida:**
```text
--- ESTADÍSTICAS DEL DATASET ---
• Total de países registrados: 10
• País con mayor población: India (1,393,409,038 hab.)
• País con menor población: Australia (25,687,041 hab.)
• Promedio de población: 213,731,357.70 hab.
• Promedio de superficie: 3,572,459.80 km²

• Cantidad de países por continente:
   - África: 2 país(es)
   - América: 3 país(es)
   - Asia: 2 país(es)
   - Europa: 2 país(es)
   - Oceanía: 1 país(es)
```

### Ejemplo 3: Filtro por continente (Opción 4 → 1)
**Entrada:**
```text
Ingrese una opción (1-7): 4
Seleccione una opción (1-3): 1
Ingrese el continente: asia
```
**Salida:**
```text
Resultados del filtro (2 país/es):

Nombre               |       Población |   Superficie (km²) | Continente     
-----------------------------------------------------------------------------
Japón                |     125,800,000 |            377,975 | Asia           
India                |   1,393,409,038 |          3,287,263 | Asia           
```

### Ejemplo 4: Validación de entradas (Opción 1)
**Entrada:**
```text
Nombre del país: Chile
Población: abc
Población: -5
Población: 19493184
```
**Salida:**
```text
Error: Debe ingresar un número entero válido.
Error: El valor debe ser mayor que cero. Intente nuevamente.
```

---

## Participación de los Integrantes

Axel Espinoza: Desarrollo integral del proyecto, código, documentación y video. *(Entrega individual).*

---

## Enlaces Obligatorios

* **Repositorio en GitHub:** `https://github.com/RemBonito/tpi-programacion1-paises-Axel-Espinoza`
* **Video Demostrativo (10 a 15 minutos - Acceso Público):** `https://drive.google.com/file/d/1XGdFd1jeneqjcDjgt4BEX-_Sek3jLO9a/view?usp=sharing`
* **Documentación Técnica en PDF:** Incluida en la raíz del repositorio (`Informe_Tecnico_TPI.pdf`) / `https://drive.google.com/file/d/1LtIx-P8XacRu-5Lw9h8XXBUkwbx6Na80/view?usp=drive_link`
