def saludar(nombre: str) -> str:
    """
    Devuelve un saludo personalizado.

    Args:
        nombre (str): El nombre de la persona a saludar.

    Returns:
        str: Mensaje de saludo.

    Example:
        >>> saludar("Jesus")
        'Hola, Jesus!'
    """
    return f"Hola, {nombre}!"

def sumar(a: int, b: int) -> int:
    """
    Suma dos números enteros.

    Args:
        a (int): Primer número.
        b (int): Segundo número.

    Returns:
        int: La suma de a y b.

    Example:
        >>> sumar(3, 3)
        6
    """
    return a + b

if __name__ == "__main__":
    print(saludar("yiisus"))
    print("2 + 3 =", sumar(2, 3))
