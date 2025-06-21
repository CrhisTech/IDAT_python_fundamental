import time
import psutil

#Funcion que devuelve el tiempo en hh:mm:ss
def convertir_tiempo(segundos):
    minutos, segundos = divmod(segundos, 60)
    horas, minutos = divmod(minutos, 60)
    return "%d:%02d:%02d" % (horas, minutos, segundos)

while True:
    #Devuelve una tupla con la info de la bateria
    bateria = psutil.sensors_battery()
    print(psutil.virtual_memory())
    
    uso_cpu = psutil.cpu_percent(interval=1)
    print(f"Uso de CPU: {uso_cpu}%")
    time.sleep(1)
    if bateria is not None:
        print("Porcentaje de bateria: ", bateria.percent)
        print("Conectado a corriente: ", bateria.power_plugged)
        # convertir segundos a hh:mm:ss
        print("Tiempo restante de bateria:", convertir_tiempo(bateria.secsleft))