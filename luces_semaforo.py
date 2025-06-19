import urequests
import time
from machine import Pin

# Pin LED
led = Pin(2, Pin.OUT)

# URL base Firebase
FIREBASE_URL = "https://semafororockemma-default-rtdb.firebaseio.com/"

def enviar_estado_led(estado):
    """Envía el estado del LED a Firebase"""
    data = {"estado_led": estado}
    try:
        response = urequests.put(FIREBASE_URL + "estado_led.json", json=data)
        print(f"Estado LED ({estado}) enviado. Respuesta: {response.text}")
        response.close()
    except Exception as e:
        print("Error al enviar estado a Firebase:", e)

if _name_ == "_main_":
    while True:
        led.on()
        enviar_estado_led(1)
        time.sleep(5)

        led.off()
        enviar_estado_led(0)
        time.sleep(5)