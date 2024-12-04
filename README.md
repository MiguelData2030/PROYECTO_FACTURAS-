# 📄 PROYECTO_FACTURAS 

Este proyecto permite realizar la extracción automatizada de datos importantes de facturas en formato PDF utilizando OCR (Reconocimiento Óptico de Caracteres). Con este sistema, puedes obtener información estructurada de tus facturas, como total a pagar, fecha de pago, forma de pago, y más.

---

## ✨ Características

- **Extracción automatizada de datos clave desde archivos PDF**.
- **Interfaz web interactiva creada con Streamlit**.
- **Soporte para múltiples archivos PDF**.
- **Utiliza Tesseract OCR para el reconocimiento de texto**.
- **Convierte páginas PDF a imágenes utilizando Poppler**.

---

## 🛠️ Requisitos

### 1. Entorno Local

- **Python**: Versión 3.8 o superior.
- **Pip**: Administrador de paquetes de Python.

### 2. Librerías Python

Asegúrate de instalar las siguientes dependencias:

- `pytesseract`: Para realizar OCR.
- `pdf2image`: Para convertir páginas de PDF a imágenes.
- `pandas`: Para manipular y estructurar datos.
- `streamlit`: Para la interfaz web.

### 3. Software Externo

- **Poppler**: Necesario para manejar conversiones de PDF a imágenes. [Descargar aquí](http://blog.alivate.com.au/poppler-windows/).
- **Tesseract OCR**: Para el reconocimiento óptico de caracteres. [Descargar aquí](https://github.com/tesseract-ocr/tesseract).

---

## 🚀 Guía de Instalación

### 1. Clona el Repositorio

```bash
### git clone https://github.com/MiguelData2030/PROYECTO_FACTURAS-.git
cd PROYECTO_FACTURAS-

2. Configura el Entorno
Instala las dependencias listadas en requirements.txt:

2. Configura el Entorno
Instala las dependencias listadas en requirements.txt:

bash
Copiar código
pip install -r requirements.txt
3. Configura Poppler y Tesseract
Agrega el binario de Poppler y Tesseract OCR a las variables de entorno (PATH) según tu sistema operativo.
4. Ejecuta la Aplicación
Corre el siguiente comando para iniciar la interfaz web:

bash
Copiar código
streamlit run Proyecto_Facturas.py
📂 Estructura del Proyecto
bash
Copiar código
PROYECTO_FACTURAS/
├── Proyecto_Facturas.py   # Código principal del proyecto
├── requirements.txt       # Dependencias del proyecto
├── README.md              # Documentación del proyecto
├── ejemplo.pdf            # Archivo PDF de ejemplo
├── screenshots/           # Imágenes de la interfaz
📸 Capturas de Pantalla
1. Interfaz de Usuario
Haz clic en el botón "Procesar Facturas" para cargar y extraer los datos de los PDF seleccionados.


📜 Licencia
Este proyecto está licenciado bajo la licencia MIT. Consulta el archivo LICENSE para más información.

🤝 Contribuciones
¡Las contribuciones son bienvenidas! Sigue estos pasos para colaborar:

Haz un fork del proyecto.

Crea una nueva rama:

bash
Copiar código
git checkout -b feature/nueva-caracteristica
Realiza tus cambios y confirma:

bash
Copiar código
git commit -m "Añade nueva característica"
Haz un push a la rama:

bash
Copiar código
git push origin feature/nueva-caracteristica
Abre un pull request.

👤 Autor
Miguel Ángel Londoño Díaz
LinkedIn | GitHub

🌟 Instrucciones Adicionales:
Si decides incluir imágenes para los ejemplos o capturas de pantalla, asegúrate de colocarlas en la carpeta screenshots/ dentro del repositorio.
Al realizar un git push final, asegúrate de verificar el archivo para garantizar que todo se ve correctamente en la vista previa de GitHub.
