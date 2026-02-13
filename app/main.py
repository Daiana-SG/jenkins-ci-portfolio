# app/main.py

def validar_usuario(nombre: str, edad: int) -> str:
    if not nombre or not nombre.strip():
        raise ValueError("El nombre no puede estar vacío")

    if edad < 0:
        raise ValueError("La edad no puede ser negativa")

    if edad < 18:
        return f"{nombre} es menor de edad"

    return f"{nombre} es mayor de edad"


if __name__ == "__main__":
    # Pequeña prueba manual cuando corrés: python3 app/main.py
    print(validar_usuario("Ana", 25))
