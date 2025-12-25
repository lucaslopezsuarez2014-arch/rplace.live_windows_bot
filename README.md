# 🎨 rplace.live Bot para Windows

Bot automatizado multi-navegador para [rplace.live](https://rplace.live) que permite controlar múltiples instancias simultáneamente.

## 🚀 Características

- ✅ Control de 4 navegadores simultáneos
- ✅ Cada navegador opera en una fila diferente (Y=0,1,2,3)
- ✅ Avance automático en el eje X
- ✅ Configurable y fácil de usar
- ✅ Compatible con Windows 10/11

## 📋 Requisitos

- Windows 10 o superior
- Python 3.8 o superior
- Google Chrome instalado
- Conexión a Internet

## 🔧 Instalación

### 1. Instalar Python

Si no tienes Python instalado:
1. Descarga Python desde [python.org](https://www.python.org/downloads/)
2. Durante la instalación, marca **"Add Python to PATH"**
3. Completa la instalación

### 2. Descargar el Bot
```bash
git clone https://github.com/tu-usuario/rplace-bot.git
cd rplace-bot
```

O descarga el ZIP desde GitHub y extráelo.

### 3. Instalar Dependencias

Abre CMD o PowerShell en la carpeta del proyecto y ejecuta:
```bash
pip install -r requirements.txt
```

### 4. Instalar ChromeDriver

El bot necesita ChromeDriver para controlar Chrome:

**Opción A (Automática):**
```bash
pip install webdriver-manager
```

**Opción B (Manual):**
1. Ve a [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads)
2. Descarga la versión que coincida con tu Chrome
3. Extrae `chromedriver.exe` en la carpeta del proyecto

## 🎮 Uso

### Inicio Rápido

Ejecuta el bot con doble clic en:
```
start_bot.bat
```

O desde CMD/PowerShell:
```bash
python rplace_bot.py
```

### Configuración

Edita `config.json` para personalizar:
```json
{
  "num_bots": 4,
  "start_x": 0,
  "start_y_positions": [0, 1, 2, 3],
  "delay_between_actions": 5,
  "color_to_place": 1
}
```

**Parámetros:**
- `num_bots`: Número de navegadores (1-8)
- `start_x`: Coordenada X inicial
- `start_y_positions`: Coordenadas Y para cada bot
- `delay_between_actions`: Segundos entre acciones
- `color_to_place`: Número del color a colocar (1-32)

### Detener el Bot

Presiona `Ctrl + C` en la ventana de CMD para detener todos los bots.

## 📁 Estructura del Proyecto
```
rplace-bot/
│
├── rplace_bot.py          # Script principal
├── requirements.txt       # Dependencias Python
├── config.json           # Archivo de configuración
├── start_bot.bat         # Iniciador para Windows
├── README.md             # Este archivo
└── LICENSE               # Licencia del proyecto
```

## ⚙️ Configuración Avanzada

### Cambiar el Color

El bot presiona el número del color. Para cambiar:
- Edita `color_to_place` en `config.json`
- O modifica directamente en `rplace_bot.py` línea 46

### Ajustar Velocidad

Modifica `delay_between_actions` en `config.json`:
- Menor valor = más rápido (mínimo recomendado: 3 segundos)
- Mayor valor = más lento pero más seguro

### Múltiples Filas

Para cubrir más área, edita `start_y_positions`:
```json
"start_y_positions": [0, 1, 2, 3, 4, 5, 6, 7]
```

## 🐛 Solución de Problemas

### Error: "chromedriver not found"
- Instala ChromeDriver siguiendo el paso 4 de instalación
- Asegúrate de que `chromedriver.exe` está en la carpeta del proyecto o en PATH

### Error: "Chrome binary not found"
- Asegúrate de tener Google Chrome instalado
- Si usas Chrome en una ubicación no estándar, edita la ruta en el código

### El bot no hace clic correctamente
- Ajusta el tiempo de espera en `config.json`
- Verifica que rplace.live esté cargado completamente

### Los navegadores no se abren
- Verifica que tienes suficiente RAM (mínimo 4GB recomendado)
- Reduce el número de bots en `config.json`

## ⚠️ Advertencias

- Usa este bot responsablemente
- Respeta las reglas de rplace.live
- El uso excesivo puede resultar en bloqueo temporal
- Este proyecto es solo educativo

## 🤝 Contribuir

Las contribuciones son bienvenidas:

1. Fork el proyecto
2. Crea una rama (`git checkout -b feature/mejora`)
3. Commit tus cambios (`git commit -m 'Añadir mejora'`)
4. Push a la rama (`git push origin feature/mejora`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 👤 Autor

**Tu Nombre**
- GitHub: [@L14dev](https://github.com/lucaslopezsuarez2014-arch)

## 🌟 Agradecimientos

- Comunidad de rplace.live
- Selenium WebDriver
- Python Community

---

⭐ Si este proyecto te fue útil, considera darle una estrella en GitHub!
