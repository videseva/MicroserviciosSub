from anyio import Path
from fastapi import APIRouter, HTTPException, Response, UploadFile
from fastapi.responses import FileResponse
from config.db import conn
from models.notification import notifications
from schemas.notification import Notification
from typing import List
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import func, select
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from datetime import datetime

from cryptography.fernet import Fernet

from schemas.vehiculo import Vehiculo

notification_api = APIRouter()
key = Fernet.generate_key()
f = Fernet(key)

@notification_api.get(
    "/notifications",
    tags=["notifications"],
    response_model=List[Notification],
    description="Listado de notificaciones",
)
def get_notification():   
    return conn.execute(notifications.select()).fetchall()

@notification_api.post("/notifications")
def enviar_mensaje_respuesta(v: Vehiculo):
    print("Correo enviado")
    # Configura el servidor de correo
    smtp_server = "smtp.gmail.com"  # Cambia esto a tu servidor SMTP
    smtp_port = 587  # Cambia esto al puerto SMTP adecuado (por ejemplo, 587 para TLS)
    smtp_username = "theblackarts22@gmail.com"  # Cambia esto a tu dirección de correo electrónico
    smtp_password = "hjya glqg azlx gkzo"  # Cambia esto a tu contraseña de correo electrónico

    # Configura el mensaje de correo electrónico
    msg = MIMEMultipart()
    msg["From"] = "theblackarts22@gmail.com"
    msg["To"] = "eva.z0301@gmail.com"
    msg["Subject"] = f"Registro de vehiculo ({v.matricula})"

    mensaje = f"Bienvenido {v.nombre}, Su vehiculo  ha sido exitoso."
    msg.attach(MIMEText(mensaje, "plain"))

    # Intenta enviar el correo
    try:
        new_notifcation = { "fecha":  datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "asunto": msg["Subject"],  "message": mensaje, "email": v.email}
        conn.execute(notifications.insert().values(new_notifcation))
        conn.commit()
        print(new_notifcation)

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(msg["From"], [msg["To"]], msg.as_string())
        server.quit()
        print("Correo electrónico enviado con éxito")
        return {"message": "Correo electrónico enviado con éxito"}
    except Exception as e:
        print(f"Error al enviar el correo: {str(e)}")
        return {"message": "Error al enviar el correo"}


   