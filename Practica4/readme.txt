Autoclicker v0
Para usar este código necesitarás instalar las siguientes dependencias:

bash
Copy
pip install keyboard pyautogui
Características principales:

Activa/desactiva con la barra espaciadora

Controla la velocidad con las flechas arriba/abajo

Click izquierdo automático

Intervalo ajustable desde 10ms hasta 2000ms

Feedback visual en la consola

Notas importantes:

El programa necesita permisos de administrador para controlar el teclado y mouse

Para detenerlo completamente usa Ctrl+C en la consola

El intervalo mínimo está establecido en 10ms (100 clicks/segundo)

PyAutoGUI usa las coordenadas actuales del mouse para hacer los clicks

Algunos sistemas pueden requerir ajustes adicionales para permitir el control del mouse

El código funciona creando un hilo secundario que maneja los clicks mientras el hilo principal gestiona los eventos del teclado y la interfaz de usuario.