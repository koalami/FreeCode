import time
import threading
from pynput import keyboard
from pynput.mouse import Controller, Button  # Importación corregida
#import pyautogui

# Configuración inicial
clicking = False
interval = 0.05
running = True
mouse = Controller()

def toggle_clicking():
    global clicking
    clicking = not clicking
    status = "ACTIVADO" if clicking else "DESACTIVADO"
    print(f"Auto-clicker {status}")

def change_interval(direction):
    global interval
    if direction == "up":
        interval = max(0.01, interval - 0.01)
    else:
        interval = min(2.0, interval + 0.01)
    print(f"Intervalo actualizado: {interval*1000:.0f} ms")

def on_press(key):
    try:
        if key == keyboard.Key.space:
            toggle_clicking()
        elif key == keyboard.Key.up:
            change_interval("up")
        elif key == keyboard.Key.down:
            change_interval("down")
    except AttributeError:
        pass

def clicker_thread():
    while running:
        if clicking:
            mouse.click(Button.left)  # Referencia corregida
            time.sleep(interval)

# Configurar el listener de teclado
keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()

print("Auto-clicker configurado")
print("[Espacio] - Activar/Desactivar")
print("[Flecha Arriba] - Aumentar velocidad (+10 ms)")
print("[Flecha Abajo] - Disminuir velocidad (-10 ms)")
print("Presiona Esc para salir...")

# Iniciar hilo del clicker
thread = threading.Thread(target=clicker_thread)
thread.start()

# Mantener el programa corriendo
with keyboard.Events() as events:
    for event in events:
        if event.key == keyboard.Key.esc:
            running = False
            keyboard_listener.stop()
            thread.join()
            print("\nAuto-clicker detenido")
            break 