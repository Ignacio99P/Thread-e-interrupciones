#Importo la clase time para la hora y la clase threading
import time
import threading

#Creo una funcion para llamarla
def hora():
    while True:
        hora_actual = time.strftime("%H:%M:%S")
        print("La hora actual es:", hora_actual)
        time.sleep(2)

# Creo y ejecuto el hilo a la funcion
thread = threading.Thread(target=hora)
thread.start()