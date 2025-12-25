@echo off
title rplace.live Bot
color 0A

echo ========================================
echo   rplace.live Multi-Bot
echo ========================================
echo.
echo Iniciando bot...
echo.

python rplace_bot.py

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Error al ejecutar el bot.
    echo Verifica que Python este instalado correctamente.
    echo.
    pause
)

exit
```

---
