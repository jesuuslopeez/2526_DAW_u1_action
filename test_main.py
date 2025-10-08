from main import saludar, sumar

def test_saludar():
    assert saludar("Jesus") == "Hola, Jesus!"
    assert saludar("Lopez") == "Hola, Lopez!"
    assert saludar("Perez") == "Hola, Perez!"

def test_sumar():
    assert sumar(1, 1) == 2
    assert sumar(2, 2) == 4
    assert sumar(3, 3) == 6
    assert sumar(4, 4) == 8
    assert sumar(5, 5) == 10
