"""
rplace.live Bot - Automatización Multi-Navegador
Autor: Tu nombre
Versión: 1.0.0
"""

import time
import subprocess
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading

class RPlaceBot:
    def __init__(self, start_x=0, start_y=0, delay=5):
        self.start_x = start_x
        self.start_y = start_y
        self.current_x = start_x
        self.current_y = start_y
        self.delay = delay
        self.driver = None
        self.running = True
        
    def setup_driver(self):
        """Configura el navegador Chrome"""
        chrome_options = Options()
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        
        try:
            self.driver = webdriver.Chrome(options=chrome_options)
            return True
        except Exception as e:
            print(f"Error al iniciar Chrome: {e}")
            print("Asegúrate de tener ChromeDriver instalado")
            return False
    
    def navigate_to_coordinate(self):
        """Navega a una coordenada específica"""
        try:
            # Intentar encontrar el input de coordenadas y navegar
            # Esto depende de la estructura de rplace.live
            # Simulamos presionar teclas para la demostración
            pyautogui.press('1')
            time.sleep(0.3)
            pyautogui.press('enter')
            return True
        except Exception as e:
            print(f"Error navegando a ({self.current_x}, {self.current_y}): {e}")
            return False
    
    def run(self):
        """Ejecuta el bot"""
        if not self.setup_driver():
            return
        
        try:
            # Cargar la página
            self.driver.get("https://rplace.live")
            print(f"Bot iniciado en Y={self.start_y}")
            time.sleep(5)  # Esperar carga inicial
            
            while self.running:
                print(f"Posición: ({self.current_x}, {self.current_y})")
                
                # Realizar acción
                self.navigate_to_coordinate()
                
                # Avanzar en X
                self.current_x += 1
                
                # Esperar antes de la siguiente acción
                time.sleep(self.delay)
                
        except KeyboardInterrupt:
            print(f"\nBot Y={self.start_y} detenido por el usuario")
        except Exception as e:
            print(f"Error en bot Y={self.start_y}: {e}")
        finally:
            if self.driver:
                self.driver.quit()
    
    def stop(self):
        """Detiene el bot"""
        self.running = False
        if self.driver:
            self.driver.quit()


def run_bot(y_position):
    """Función para ejecutar un bot en un hilo separado"""
    bot = RPlaceBot(start_x=0, start_y=y_position, delay=5)
    bot.run()


def main():
    print("=" * 50)
    print("rplace.live Multi-Bot")
    print("=" * 50)
    print("\nConfiguración:")
    print("- 4 navegadores simultáneos")
    print("- Cada uno en una fila diferente (Y=0,1,2,3)")
    print("- Avance automático en eje X")
    print("\nPresiona Ctrl+C para detener todos los bots\n")
    
    # Crear hilos para cada bot
    threads = []
    for y in range(4):
        thread = threading.Thread(target=run_bot, args=(y,))
        thread.daemon = True
        threads.append(thread)
        thread.start()
        time.sleep(2)  # Esperar entre cada inicio
    
    try:
        # Mantener el programa corriendo
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\nDeteniendo todos los bots...")
        print("Programa finalizado")


if __name__ == "__main__":
    main()
```

---

## 📄 2. requirements.txt
```
selenium==4.16.0
pyautogui==0.9.54
webdriver-manager==4.0.1
pillow==10.1.0
