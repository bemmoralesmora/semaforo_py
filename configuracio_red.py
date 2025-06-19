import network
import time
from machine import Pin

def conectar_wifi(lista_redes):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if wlan.isconnected():
        wlan.disconnect()

    for red in lista_redes:
        print(f"\nConectando a {red['ssid']}...")
        wlan.connect(red['ssid'], red['password'])

        timeout = 0
        while not wlan.isconnected() and timeout < 10:
            print(".", end="")
            time.sleep(1)
            timeout += 1

        if wlan.isconnected():
            print(f"\nConectado a {red['ssid']}")
            return True

    print("No se pudo conectar a ninguna red.")
    return False