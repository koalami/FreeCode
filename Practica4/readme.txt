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