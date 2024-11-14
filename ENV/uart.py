import serial

# Configura el puerto y la velocidad en baudios
puerto = 'COM3'  # Cambia esto al puerto correcto de tu Bluetooth
baudrate = 9600  # Ajusta el baudrate si es necesario

# Abre la conexión serie
ser = serial.Serial(puerto, baudrate, timeout=1)

try:
    while True:
        if ser.in_waiting > 0:  # Verifica si hay datos en el buffer
            datos = ser.readline().decode('utf-8').strip()
            # Procesa los datos recibidos, separando PRESION y DISTANCIA
            if datos.startswith(";PRESION"):
                partes = datos.split()
                presion = partes[2]
                distancia = partes[5]
                print(f"PRESIÓN = {presion}, DISTANCIA = {distancia}")
except KeyboardInterrupt:
    print("Terminando la lectura.")
finally:
    ser.close()
