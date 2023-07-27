import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
import json
from datetime import datetime

url = 'http://10.150.4.171:5000/edi'
response = requests.get(url)

lista_edis = []

if response.status_code == 200:
    data = response.json()
    if 'edis' in data:
        lista_edis = data['edis']
    else:
        print("El JSON no contiene la clave 'edis'")
else:
    print(f"Error al realizar la solicitud. Código de estado: {response.status_code}")

smtp_server = 'smtp.gmail.com'
smtp_port = 587

def format_dict_to_string(d):
    return json.dumps(d, indent=4)  # Convierte el diccionario a una cadena JSON con formato

def get_message():
    if not lista_edis:
        return "No hay datos aun."
    else:
        return f'Lista de edis:\n\n{"".join(format_dict_to_string(edi) for edi in lista_edis)}'
    
def get_subject():
    if not lista_edis:
        return "No hay pedidos duplicados 🚛"
    else:
        return 'Edis Raloy 🚛 ({})'.format(len(lista_edis))
    
email_address = 'apps@raloy.com.mx'
email_password = 'Santiago2020'
from_address = 'apps@raloy.com.mx'

to_address = 'alopez@raloy.com.mx'
subject = get_subject()

def enviar_correo():
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject

    message = get_message()
    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(email_address, email_password)
    server.sendmail(from_address, to_address, msg.as_string())
    server.quit()
    print("Log (Output): [{}] | Result: {}".format(datetime.now(), 'Not duplicated' if not len(lista_edis) else len(lista_edis)))

if __name__ == '__main__':
    try:
        while True:
            enviar_correo()
            time.sleep(600)  # Espera 10 minutos (600 segundos) antes de enviar el siguiente correo
    except KeyboardInterrupt:
        print("Ejecución interrumpida por el usuario")
