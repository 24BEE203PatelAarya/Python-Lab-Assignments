
#6.Convert list of temperatures in Fahrenheit degrees to equivalent Celsius degrees.


fahrenheit_temps = [40, 45, 55, 70, 75, 84, 90, 104, 110]

celsius_temps = []

for temp in fahrenheit_temps:
    celsius = (temp - 32) * 5 / 9
    celsius_temps.append(celsius)

print("Temperatures in Celsius:", celsius_temps)
