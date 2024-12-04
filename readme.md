{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# PROYECTO_FACTURAS 🧾\n",
    "\n",
    "Este proyecto permite realizar la extracción automatizada de datos importantes de facturas en formato PDF utilizando OCR (Reconocimiento Óptico de Caracteres). Con este sistema, puedes obtener información estructurada de tus facturas, como total a pagar, fecha de pago, forma de pago, y más.\n",
    "\n",
    "## 🚀 Características\n",
    "\n",
    "- Extracción automatizada de datos clave desde archivos PDF.\n",
    "- Interfaz web interactiva creada con **Streamlit**.\n",
    "- Soporte para múltiples archivos PDF.\n",
    "- Utiliza **Tesseract OCR** para el reconocimiento de texto.\n",
    "- Convierte páginas PDF a imágenes utilizando **Poppler**.\n",
    "\n",
    "## 📋 Requisitos\n",
    "\n",
    "### 1. Entorno Local\n",
    "\n",
    "- **Python**: Versión 3.8 o superior.\n",
    "- **Pip**: Administrador de paquetes de Python.\n",
    "\n",
    "### 2. Librerías Python\n",
    "\n",
    "Asegúrate de instalar las siguientes dependencias:\n",
    "\n",
    "- **pytesseract**: Para realizar OCR.\n",
    "- **pdf2image**: Para convertir páginas de PDF a imágenes.\n",
    "- **pandas**: Para manipular y estructurar datos.\n",
    "- **streamlit**: Para la interfaz web.\n",
    "\n",
    "### 3. Software Externo\n",
    "\n",
    "- **Poppler**: Necesario para manejar conversiones de PDF a imágenes. [Descargar aquí](https://github.com/oschwartz10612/poppler-windows/releases).\n",
    "- **Tesseract OCR**: Para el reconocimiento óptico de caracteres. [Descargar aquí](https://github.com/tesseract-ocr/tesseract).\n",
    "\n",
    "## 🛠️ Guía de Instalación\n",
    "\n",
    "### 1. Clona el Repositorio\n",
    "\n",
    "```bash\n",
    "git clone https://github.com/MiguelData2030/PROYECTO_FACTURAS-.git\n",
    "cd PROYECTO_FACTURAS-\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2. Configura el Entorno\n",
    "Instala las dependencias listadas en requirements.txt:\n",
    "\n",
    "pip install -r requirements.txt"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "3. Configura Poppler y Tesseract\n",
    "Agrega el binario de Poppler y Tesseract OCR a las variables de entorno (PATH).\n",
    "4. Ejecuta la Aplicación\n",
    "Corre el siguiente comando para iniciar la interfaz web:\n",
    "\n",
    "streamlit run Proyecto_Facturas.py\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "📂 Estructura del Proyecto\n",
    "\n",
    "PROYECTO_FACTURAS/\n",
    "│\n",
    "├── Proyecto_Facturas.py    # Código principal del proyecto\n",
    "├── requirements.txt        # Dependencias del proyecto\n",
    "├── README.md               # Documentación del proyecto\n",
    "└── ejemplo.pdf             # Archivo PDF de ejemplo\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "✨ Ejemplo de Uso\n",
    "Sube uno o más archivos PDF con facturas en la interfaz.\n",
    "Haz clic en el botón \"Procesar Facturas\".\n",
    "Visualiza los datos extraídos en una tabla interactiva.\n",
    "🖼️ Capturas de Pantalla\n",
    "Interfaz de Usuario\n",
    "\n",
    "Resultado de Extracción\n",
    "\n",
    "🤝 Contribuciones\n",
    "¡Las contribuciones son bienvenidas! Siéntete libre de crear un pull request o abrir un issue.\n",
    "\n",
    "📜 Licencia\n",
    "Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más información.\n",
    "\n",
    "📧 Contacto\n",
    "Miguel Ángel Londoño Díaz\n",
    "Correo: miguelalejandro21777@hotmail.com\n",
    "GitHub: MiguelData2030\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
