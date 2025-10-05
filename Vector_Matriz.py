import numpy as np
import sys

# -------------------------------------------------------------
# --- FUNCIONES DE INGRESO CON VALIDACIÓN DE ESPACIOS VACÍOS Y CERO/NEGATIVO ---
# -------------------------------------------------------------

def ingresar_vectores():
    """Solicita la cantidad y los valores de los vectores."""
    while True:
        try:
            # Validar Cantidad de Vectores
            n_vectores_str = input("Ingrese la cantidad de vectores: ").strip()
            
            
            if not n_vectores_str:
                print("ALERTA: El campo de cantidad de vectores está vacío.")
                continue
            n_vectores = int(n_vectores_str)

           
            if n_vectores <= 0:
                print("ERROR: La cantidad de vectores debe ser un número entero positivo (mayor que 0).")
                continue

            
            longitud_str = input("Ingrese la longitud de los vectores: ").strip()
            
            
            if not longitud_str:
                print("ALERTA: El campo de longitud está vacío.")
                continue
            longitud = int(longitud_str)
            
            
            if longitud <= 0:
                print("ERROR: La longitud del vector debe ser un número entero positivo (mayor que 0).")
                continue
            
            break # Si ambas validaciones pasan
        except ValueError:
            print("Error: Ingrese solo números enteros válidos.")
    
    vectores = []
    for i in range(n_vectores):
        print(f"\n--- Ingrese los valores para el Vector {i + 1} ---")
        valores = []
        for j in range(longitud):
            while True:
                valor = input(f"Valor {j + 1}: ").strip()
                
               
                if not valor:
                    print("ALERTA: El campo está vacío. Ingrese un número entero.")
                    continue
                
                # Note: La validación 'isdigit()' prohíbe negativos, decimales, y cero (porque lo tratamos como positivo en este contexto)
                if not valor.isdigit():
                    print("Error: Ingrese solo números enteros positivos (sin punto ni signo).")
                elif int(valor) < 0: # Check extra para la claridad del error si se hubiera permitido signo
                    print("Error: Ingrese solo números enteros positivos.")
                else:
                    valores.append(int(valor))
                    break
        vectores.append(np.array(valores))
    return vectores


def ingresar_matrices():
    """Solicita dos matrices y valida entradas."""
    while True:
        try:
            
            filas_str = input("Ingrese el número de filas: ").strip()
            
            if not filas_str:
                print("ALERTA: El campo de filas está vacío.")
                continue
            filas = int(filas_str)
            
           
            if filas <= 0:
                print("ERROR: El número de filas debe ser un número entero positivo (mayor que 0).")
                continue

            
            columnas_str = input("Ingrese el número de columnas: ").strip()
            
            if not columnas_str:
                print("ALERTA: El campo de columnas está vacío.")
                continue
            columnas = int(columnas_str)
            
            
            if columnas <= 0:
                print("ERROR: El número de columnas debe ser un número entero positivo (mayor que 0).")
                continue
            
            break # Si ambas validaciones pasan
        except ValueError:
            print("Error: Ingrese solo números enteros válidos.")

    matrices = []
    for i in range(2):
        print(f"\nIngrese los valores de la Matriz {i + 1}:")
        matriz = []
        for f in range(filas):
            fila = []
            for c in range(columnas):
                while True:
                    valor = input(f"Elemento [{f + 1}, {c + 1}]: ").strip()
                    
                    # ALERTA: Campo Vacío
                    if not valor:
                        print("ALERTA: El campo está vacío. Ingrese un número entero.")
                        continue
                        
                    if not valor.isdigit():
                        print("Error: Ingrese solo números enteros positivos (sin punto ni signo).")
                    elif int(valor) < 0:
                        print("Error: Ingrese solo números enteros positivos.")
                    else:
                        fila.append(int(valor))
                        break
            matriz.append(fila)
        matrices.append(np.array(matriz))
    return matrices


# -------------------------------------------------------------
# --- FUNCIONES DE MENÚ Y CÁLCULO (Se renombra la opción 6) ---
# -------------------------------------------------------------

def mostrar_menu_vectores(n_vectores):
    print("\n--- MENÚ DE OPERACIONES (Vectores) ---")
    print("1. Suma de vectores")
    print("2. Resta de vectores (solo si hay 2)")
    print("3. Multiplicación por escalar")
    if n_vectores == 2:
        print("4. Producto punto")
    print("5. Mostrar todos los vectores")
    print("6. Reiniciar vectores") # Opción renombrada
    print("0. Volver al menú principal")
    return input("Seleccione una opción: ").strip()


def mostrar_menu_matrices():
    print("\n--- MENÚ DE OPERACIONES (Matrices) ---")
    print("1. Suma de matrices")
    print("2. Resta de matrices")
    print("3. Multiplicación de matrices")
    print("4. Mostrar matrices")
    print("6. Reiniciar matrices") # Se añade opción de Reiniciar
    print("0. Volver al menú principal")
    return input("Seleccione una opción: ").strip()


def calculadora_vectores():
    print("\n=== CALCULADORA DE VECTORES ===")
    vectores = ingresar_vectores()
    n_vectores = len(vectores)

    while True:
        opcion = mostrar_menu_vectores(n_vectores)
        
        if not opcion:
            print("ALERTA: La selección de opción no puede estar vacía.")
            continue
        
        if opcion == "1":
            resultado = np.sum(vectores, axis=0)
            print(f"\nResultado de la suma: {resultado}")
        elif opcion == "2":
            if n_vectores == 2:
                resultado = vectores[0] - vectores[1]
                print(f"\nResultado de la resta: {resultado}")
            else:
                print("La resta solo se puede ejecutar con 2 vectores.")
        elif opcion == "3":
            while True:
                try:
                    escalar = input("Ingrese el escalar (entero positivo): ").strip()
                    
                    if not escalar:
                        print("ALERTA: El campo está vacío. Ingrese un número entero positivo.")
                        continue
                        
                    if not escalar.isdigit() or int(escalar) <= 0: # Validación de escalar (cero/negativo)
                        print("Error: Ingrese un número entero positivo.")
                        continue
                        
                    escalar = int(escalar)
                    
                    indice_str = input(f"¿Qué vector desea multiplicar? (1-{n_vectores}): ").strip()
                    if not indice_str:
                         print("ALERTA: El campo de índice está vacío.")
                         continue
                    
                    if not indice_str.isdigit() or int(indice_str) <= 0: # Validación de índice (cero/negativo)
                        print("Error: Ingrese un número entero positivo válido.")
                        continue
                         
                    indice = int(indice_str) - 1
                    
                    if 0 <= indice < n_vectores:
                        resultado = escalar * vectores[indice]
                        print(f"\nResultado: {escalar} × Vector{indice + 1} = {resultado}")
                        break
                    else:
                        print("Índice fuera de rango.")
                except ValueError:
                    print("Error: Ingrese un número válido para el escalar y el índice.")
        elif opcion == "4" and n_vectores == 2:
            resultado = np.dot(vectores[0], vectores[1])
            print(f"\nResultado del producto punto: {resultado}")
        elif opcion == "5":
            print("\n--- VECTORES ACTUALES ---")
            for i, v in enumerate(vectores):
                print(f"Vector {i + 1}: {v}")
        elif opcion == "6": # Reiniciar vectores
            print("\n=== REINICIANDO VECTORES ===")
            vectores = ingresar_vectores()
            n_vectores = len(vectores)
        elif opcion == "0":
            break
        else:
            print("Opción no válida.")


def calculadora_matrices():
    print("\n=== CALCULADORA DE MATRICES ===")
    matrices = ingresar_matrices()
    while True:
        opcion = mostrar_menu_matrices()
        
        if not opcion:
            print("ALERTA: La selección de opción no puede estar vacía.")
            continue
            
        if opcion == "1":
            print("\nResultado de la suma:")
            print(matrices[0] + matrices[1])
        elif opcion == "2":
            print("\nResultado de la resta:")
            print(matrices[0] - matrices[1])
        elif opcion == "3":
            try:
                print("\nResultado de la multiplicación:")
                print(np.dot(matrices[0], matrices[1]))
            except ValueError:
                print("Error: No se pueden multiplicar las matrices (dimensiones incompatibles).")
        elif opcion == "4":
            for i, m in enumerate(matrices):
                print(f"\nMatriz {i + 1}:\n{m}")
        elif opcion == "6": # Reiniciar matrices
            print("\n=== REINICIANDO MATRICES ===")
            matrices = ingresar_matrices()
        elif opcion == "0":
            break
        else:
            print("Opción no válida.")


def main():
    while True:
        print("\n========== CALCULADORA GENERAL ==========")
        print("1. Calculadora de Vectores")
        print("2. Calculadora de Matrices")
        print("0. Salir del programa")
        
        opcion = input("Seleccione una opción: ").strip()
        
        if not opcion:
            print("ALERTA: La selección de opción no puede estar vacía.")
            continue

        if opcion == "1":
            calculadora_vectores()
        elif opcion == "2":
            calculadora_matrices()
        elif opcion == "0":
            print("\n¡Hasta luego!")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()