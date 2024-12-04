import streamlit as st
from pdf2image import convert_from_path
import pytesseract
from PIL import Image
import pandas as pd
import os

# Configuración de los paths de Poppler y Tesseract
poppler_path = r"C:\Program Files (x86)\poppler-24.08.0\Library\bin"
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Función para procesar el PDF y convertirlo a texto con OCR
def process_pdf_with_ocr(pdf_file):
    images = convert_from_path(pdf_file, poppler_path=poppler_path)
    extracted_texts = []
    for img in images:
        text = pytesseract.image_to_string(img, lang="spa")
        extracted_texts.append((text, img))
    return extracted_texts

# Función para extraer datos específicos del texto
def extract_data_from_text(text_list):
    data = []
    for text, img in text_list:
        forma_pago = extract_between(text, "Forma de Pago:", "\n")
        medio_pago = extract_between(text, "Medio de Pago:", "\n")
        fecha_pago = extract_between(text, "Fecha de Pago:", "\n")
        total_pagar = extract_between(text, "Total a Pagar:", "\n")
        factura = extract_between(text, "Factura Electronica de Venta:", "\n")

        # Extraer el "Código Principal" utilizando recorte de imagen
        codigo_principal = extract_code_from_image(img)

        data.append({
            "Forma de Pago": forma_pago,
            "Medio de Pago": medio_pago,
            "Fecha de Pago": fecha_pago,
            "Código Principal": codigo_principal,
            "Total a Pagar": total_pagar,
            "Factura": factura
        })
    return data

# Función para extraer texto entre dos delimitadores
def extract_between(text, start, end):
    try:
        return text.split(start)[1].split(end)[0].strip()
    except IndexError:
        return "No encontrado"

# Función para extraer el código principal de un área específica de la imagen
def extract_code_from_image(image):
    try:
        # Recortar el área específica del "Código Principal"
        cropped_img = image.crop((50, 300, 450, 350))  # Ajusta los valores según sea necesario
        code = pytesseract.image_to_string(cropped_img, lang="spa", config="--psm 6")
        return code.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Interfaz con Streamlit
st.title("Extracción de Facturas PDF con OCR")
uploaded_files = st.file_uploader("Cargue sus archivos PDF", accept_multiple_files=True, type=["pdf"])

if st.button("Procesar Facturas"):
    if uploaded_files:
        all_data = []
        for pdf_file in uploaded_files:
            with open(pdf_file.name, "wb") as f:
                f.write(pdf_file.read())
            text_list = process_pdf_with_ocr(pdf_file.name)
            extracted_data = extract_data_from_text(text_list)
            all_data.extend(extracted_data)
            os.remove(pdf_file.name)  # Elimina el archivo temporal

        # Mostrar los datos extraídos en un DataFrame
        df = pd.DataFrame(all_data)
        st.dataframe(df)
    else:
        st.error("Por favor, cargue al menos un archivo PDF.")
