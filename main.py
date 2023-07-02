zmienna_1: int = 10
zmienna_2: float = 20
print(zmienna_1, zmienna_2)

def program(a: int, b: int) -> int:
	wynik = a + b
	return wynik
suma: float = program(zmienna_1, zmienna_2)
print(suma)
