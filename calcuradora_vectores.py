import numpy as np

def main():
    print("=== OPERACIONES CON VECTORES USANDO NUMPY ===\n")
    
    try:
        # Solicitar cantidad de vectores y longitud
        num_vectores = int(input("Ingrese la cantidad de vectores: "))
        longitud = int(input("Ingrese la longitud de los vectores: "))
        
        if num_vectores <= 0 or longitud <= 0:
            print("Error: La cantidad de vectores y la longitud deben ser números positivos.")
            return
        
        vectores = []
        
        # Solicitar valores de cada vector
        for i in range(num_vectores):
            print(f"\n--- Vector {i+1} ---")
            vector = []
            for j in range(longitud):
                valor = float(input(f"Ingrese el valor {j+1} del vector {i+1}: "))
                vector.append(valor)
            vectores.append(np.array(vector))
            print(f"Vector {i+1}: {vectores[i]}")
        
        # Mostrar menú de operaciones
        print("\n--- OPERACIONES DISPONIBLES ---")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación por escalar")
        if num_vectores == 2:
            print("4. Producto punto")
        
        # Solicitar operación
        opcion = input("\nSeleccione la operación (1-4): ")
        
        # Realizar operación seleccionada
        if opcion == "1":
            # Suma de todos los vectores
            resultado = np.zeros(longitud)
            for vector in vectores:
                resultado += vector
            print(f"\nResultado de la suma: {resultado}")
            
        elif opcion == "2":
            # Resta (solo para 2 vectores)
            if num_vectores != 2:
                print("Error: La resta solo está disponible para exactamente 2 vectores.")
                return
            resultado = vectores[0] - vectores[1]
            print(f"\nResultado de la resta (Vector1 - Vector2): {resultado}")
            
        elif opcion == "3":
            # Multiplicación por escalar
            escalar = float(input("Ingrese el valor del escalar: "))
            indice_vector = int(input(f"¿Qué vector desea multiplicar? (1-{num_vectores}): ")) - 1
            
            if indice_vector < 0 or indice_vector >= num_vectores:
                print("Error: Índice de vector inválido.")
                return
                
            resultado = escalar * vectores[indice_vector]
            print(f"\nResultado de multiplicar {escalar} × Vector{indice_vector+1}: {resultado}")
            
        elif opcion == "4" and num_vectores == 2:
            # Producto punto
            resultado = np.dot(vectores[0], vectores[1])
            print(f"\nResultado del producto punto: {resultado}")
            
        else:
            print("Error: Opción no válida.")
            
    except ValueError:
        print("Error: Por favor ingrese valores numéricos válidos.")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()