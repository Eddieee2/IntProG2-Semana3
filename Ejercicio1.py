temp_fah = float(input("Ingresa la temperatura en F: "))
temp_cel = temp_fah - 32
temp_cel = temp_cel * 5
temp_cel = temp_cel / 9

print("La temperatura en Celsius es: ", temp_cel)

temp_kel = temp_cel + 273.15

print(f"Grados Celcius {temp_cel:.2f}")
print(f"Grados Kelvin {temp_kel:.2f}")