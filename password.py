import random
import string

def generar_contrasena(longitud=12, incluir_mayusculas=True, incluir_numeros=True, incluir_simbolos=True):
    caracteres = string.ascii_lowercase  # Caracteres por defecto: minúsculas

    if incluir_mayusculas:
        caracteres += string.ascii_uppercase  # Agregar mayúsculas

    if incluir_numeros:
        caracteres += string.digits  # Agregar números

    if incluir_simbolos:
        caracteres += string.punctuation  # Agregar símbolos

    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def main():
    print("Generador de Contraseñas Seguras")
    longitud = int(input("Longitud de la contraseña: "))

    incluir_mayusculas = input("Incluir mayúsculas (Sí/No): ").lower() == 'si'
    incluir_numeros = input("Incluir números (Sí/No): ").lower() == 'si'
    incluir_simbolos = input("Incluir símbolos (Sí/No): ").lower() == 'si'

    contrasena_generada = generar_contrasena(
        longitud, incluir_mayusculas, incluir_numeros, incluir_simbolos
    )

    print("Contraseña generada:", contrasena_generada)

if __name__ == "__main__":
    main()
