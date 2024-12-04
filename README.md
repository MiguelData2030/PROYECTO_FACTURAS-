# 📄 **PROYECTO_FACTURAS** 🖥️

Bienvenido al **Proyecto Facturas**, una herramienta diseñada para la extracción automatizada de datos de facturas en formato PDF mediante tecnologías de OCR (Reconocimiento Óptico de Caracteres). 💡 Este proyecto está orientado a la automatización de procesos y optimización del análisis de documentos, ideal para empresas o individuos que buscan gestionar información de manera eficiente.

---

## ✨ **Características Principales**

- **🚀 Procesamiento Automático**: Extrae datos clave como Forma de Pago, Medio de Pago, Fecha de Pago, Código Principal, Total a Pagar y Número de Factura.
- **🖼️ Conversión de PDF a Texto**: Utiliza **Poppler** y **Tesseract OCR** para convertir PDFs en texto analizable.
- **📊 Visualización Intuitiva**: Presenta los resultados en una tabla interactiva en la aplicación web construida con **Streamlit**.
- **📂 Multiherramientas**: Compatible con múltiples facturas cargadas de forma simultánea.

---

## 🎯 **Objetivo del Proyecto**

El objetivo de este proyecto es proporcionar una solución eficiente y precisa para extraer datos estructurados desde facturas en PDF, reduciendo el tiempo invertido en tareas manuales y mejorando la confiabilidad en el procesamiento de documentos.

---

## 🛠️ **Requisitos del Sistema**

### **1. Herramientas Básicas**
- **Python**: Versión 3.8 o superior.
- **Pip**: Administrador de paquetes de Python.

### **2. Librerías Python**
Asegúrate de instalar las siguientes dependencias:
- **pytesseract**: Para realizar OCR.
- **pdf2image**: Para convertir páginas de PDF a imágenes.
- **pandas**: Para manipular y estructurar datos.
- **streamlit**: Para la interfaz web.

### **3. Software Externo**
- **Poppler**: Necesario para manejar conversiones de PDF a imágenes. [Descargar aquí](https://github.com/oschwartz10612/poppler-windows/releases/).
- **Tesseract OCR**: Para el reconocimiento óptico de caracteres. [Descargar aquí](https://github.com/tesseract-ocr/tesseract).

---

## 🚀 **Guía de Instalación**

### **1. Clona el Repositorio**
```bash
git clone https://github.com/MiguelData2030/PROYECTO_FACTURAS-.git
cd PROYECTO_FACTURAS-
