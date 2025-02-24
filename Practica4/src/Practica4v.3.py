"""
=== AUTO-CLICKER PYNPUT EDICIÓN FINAL ===
Requisitos instalación:
1. Bibliotecas Python:
   pip install pynput pyautogui

2. Dependencias del sistema (Linux):
   sudo apt-get install xauth libxext-dev libxtst-dev python3-xlib

3. Permisos X Server (ejecutar antes de iniciar):
   xhost +local:
   export DISPLAY=:0

Explicación técnica:
- PyAutoGUI: Simula clicks del mouse (aunque aquí usamos pynput para mejor integración)
- pynput: Biblioteca de bajo nivel para controlar/monitorear dispositivos de entrada
   * Keyboard.Listener: Captura eventos globales de teclado sin root
   * Mouse.Controller: Controla el mouse y sus eventos
   * Button: Enumeración de botones del mouse

Configuración clave:
- Sistema de hilos separados para no bloquear eventos
- Intervalo dinámico con límites de 10ms a 2000ms
- Mecanismo de seguridad con tecla ESC para salida controlada
- Global flags para sincronización entre hilos

Funcionamiento general:
1. Listener de teclado corre en segundo plano
2. Hilo de clicks opera cuando el flag está activo
3. Bucle principal solo espera la tecla de salida
4. Todos los componentes se detienen limpiamente al salir
"""

import time
import threading
from pynput import keyboard
from pynput.mouse import Controller, Button  # Importación corregida
#import pyautogui

# =============================================
# CONFIGURACIÓN PRINCIPAL
# =============================================
clicking = False    # Estado de activación
interval = 0.05     # Intervalo base (50ms)
running = True      # Flag de control general
mouse = Controller()# Controlador del mouse

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