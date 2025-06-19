from configuracion_red import conectar_wifi
from machine import Pin
import time
import urequests
from luces_semaforo import enviar_estado_led


# WiFi
Redes = [
    {'ssid': 'iPhoneH', 'password': 'A$AP__ugly'},
    {'ssid': 'selp', 'password': '12345678jhs'}
]

# Conexión WiFi
if conectar_wifi(Redes):
    print("Conectado a WiFi - Ejecutando")
else:
    print("Modo offline - Funcion limitada")

# Pines
led1 = Pin(13, Pin.OUT)
led2 = Pin(12, Pin.OUT)
led3 = Pin(11, Pin.OUT)

# Firebase URL base
FIREBASE_URL = "https://semafororockemma-default-rtdb.firebaseio.com/"

def enviar_estados():
    try:
        data = {
            "led1": led1.value(),
            "led2": led2.value(),
            "led3": led3.value()
        }
        response = urequests.put(FIREBASE_URL + "semaforo.json", json=data)
        print(f"Datos enviados: {data}")
        response.close()
    except Exception as e:
        print("Error al enviar datos a Firebase:", e)

# Bucle principal
while True:
    for led, nombre in [(led1, "LED1"), (led2, "LED2"), (led3, "LED3")]:
        led.on()
        print(f"{nombre} encendido")
        enviar_estados()
        time.sleep(0.5)

        led.off()
        print(f"{nombre} apagado")
        enviar_estados()
        time.sleep(0.5)