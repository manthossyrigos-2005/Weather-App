temperature_celsius = float(input("Please enter the temperature celsius:"))
print(f"The temperature in celsius is:{temperature_celsius}")
temperature_fahrenheit = 1.8 * temperature_celsius + 32
print(f"The temperature in fahrenheit is:{temperature_fahrenheit}")
print(round(temperature_fahrenheit, 2))
temperature_kelvin = temperature_celsius + 273.15
print(round(temperature_kelvin, 2))
print(f"The temperature in kelvin is:{temperature_kelvin}")
difference_from_25 = temperature_celsius - 25
print(f"The difference is:{difference_from_25}")

