📄 PROYECTO_FACTURAS 🖥️
Bienvenido al Proyecto Facturas, una herramienta interactiva y automatizada para la extracción de datos desde facturas en formato PDF utilizando técnicas de OCR (Reconocimiento Óptico de Caracteres). 💡 Este proyecto es ideal para optimizar la gestión y análisis de documentos en empresas y mejorar la eficiencia del manejo de datos.

✨ Características
📝 Extracción precisa de datos: Forma de pago, medio de pago, fecha, código principal, factura y valores monetarios.
🔍 OCR Automático: Convierte texto de PDFs a datos estructurados.
📊 Interfaz amigable: Interactúa con el sistema a través de una interfaz intuitiva hecha en Streamlit.
🚀 Automatización eficiente: Convierte múltiples PDFs a tablas procesables en segundos.
🎯 Objetivo del Proyecto
Facilitar el procesamiento y análisis de facturas en PDF mediante una herramienta interactiva que combina tecnologías como Python, Tesseract OCR, y Streamlit para entregar resultados rápidos y precisos.

🛠️ Requisitos del Sistema
Python (versión 3.8 o superior)
Dependencias Python:
pytesseract
pdf2image
pandas
streamlit
Poppler y Tesseract OCR instalados en el sistema:
Descargar Poppler
Descargar Tesseract OCR
🚀 Instalación y Configuración
1. Clona este repositorio
bash
Copiar código
git clone https://github.com/MiguelData2030/PROYECTO_FACTURAS-.git
cd PROYECTO_FACTURAS-
2. Instala las dependencias
Ejecuta el siguiente comando para instalar las dependencias requeridas:

bash
Copiar código
pip install -r requirements.txt
3. Configura Tesseract y Poppler
Tesseract: Agrega su ruta al archivo .py en pytesseract.pytesseract.tesseract_cmd.
Poppler: Configura la variable poppler_path con la ruta de instalación.
🖥️ Uso de la Aplicación
Ejecuta la aplicación en tu terminal:

bash
Copiar código
streamlit run Proyecto_Facturas.py
Sube tus archivos PDF desde la interfaz:

Haz clic en "Browse files" para seleccionar tus facturas.
Presiona "Procesar Facturas" para extraer los datos.
Visualiza los resultados en una tabla interactiva directamente en la app.

📂 Estructura del Proyecto
graphql
Copiar código
PROYECTO_FACTURAS/
├── Proyecto_Facturas.py     # Código principal del proyecto
├── temp.pdf                 # PDF temporal durante el procesamiento
├── factura-14574.pdf        # Factura de prueba
├── README.md                # Este archivo
└── requirements.txt         # Dependencias necesarias
🌟 Resultados Esperados
Los datos extraídos aparecerán en una tabla con las siguientes columnas:

Forma de Pago
Medio de Pago
Fecha de Pago
Código Principal
Total a Pagar
Factura
🤝 Contribuciones
¡Eres bienvenido a contribuir! Por favor, abre un pull request o genera un issue para reportar cualquier problema o sugerencia.

📧 Contacto
Si tienes alguna duda, puedes contactarme:

Autor: Miguel Ángel Londoño Díaz
GitHub: MiguelData2030
Este archivo README no solo es informativo, sino también visualmente atractivo e interactivo. Si necesitas algo más, ¡dímelo! 🎉






