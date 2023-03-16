temps = input("temperaturas ")

temps=[float(temp) for temp in temps.split()]
temp_min = temps[0]
temp_max = temps[0]
suma_temps= 0



for temp in temps:
    if temp < temp_min:
        temp_min = temp
    if temp > temp_max:
        temp_max=temp
    if temp <= -40:
        categoria = "demaciado frias"
    elif temp <= 20:
        categoria= "optima"
    else:
        categoria = "alta"
    print(f"la tempertura {temp:.1f}°C esta {categoria}")
    suma_temps += temp

promedio_temps = suma_temps / len(temps)


print(f"la temperatura mas baja es {temp_min:.1f}°C")
print(f"la temperatura mas alta es {temp_max:.1f}°C")
print(f"la suma de las temperaturas es: {suma_temps:.1f} °C")
print(f"el promedio de temperaturas es: {promedio_temps:1f}°C")