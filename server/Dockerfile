# Usa una versión específica de la imagen base de Python.
FROM python:3.9

# Copia el script de Python y el archivo requirements.txt al contenedor en la carpeta /app.
COPY email_edi.py /app/email_edi.py
COPY requirements.txt /app/requirements.txt

# Establece el directorio de trabajo en /app.
WORKDIR /app

# Instala las dependencias desde el archivo requirements.txt.
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Instala vim en el contenedor (opcional).
RUN apt-get update && apt-get install -y vim

EXPOSE 5000

# Ejecuta el script de Python cuando el contenedor se inicie.
CMD ["python3", "email_edi.py"]