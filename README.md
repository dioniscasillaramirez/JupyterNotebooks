# Plataforma de análisis de figuras públicas

Este repositorio contiene un ejemplo básico de cómo estructurar una 
plataforma para analizar y comparar métricas de figuras públicas a 
partir de las APIs de redes sociales. 

El archivo `public_figures_platform.py` incluye conectores simples para
Twitter, Facebook e Instagram. Los tokens de acceso deben proporcionarse
mediante variables de entorno o directamente en el código de ejemplo.

## Requisitos
- Python 3.11 o superior
- Librería `requests`

Se recomienda crear un entorno virtual e instalar las dependencias:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install requests
```

## Uso

1. Obtén los tokens de acceso para cada API de red social.
2. Edita `public_figures_platform.py` y reemplaza `TU_TOKEN_AQUI` con tus
   credenciales.
3. Ejecuta el script:

```bash
python public_figures_platform.py
```

El ejemplo compara el total de seguidores de dos figuras ficticias.

## Nota
Este código es únicamente un prototipo de referencia. Las APIs reales 
pueden requerir autenticación adicional y manejo de permisos.

## Demostraci\u00f3n sin credenciales

Si no cuentas con tokens de API, puedes ejecutar una demostraci\u00f3n que utiliza
conectores simulados y datos ficticios:

```bash
python demo.py
```

Esto muestra la comparaci\u00f3n de seguidores entre dos figuras utilizando los
datos definidos en `mock_connectors.py`.
