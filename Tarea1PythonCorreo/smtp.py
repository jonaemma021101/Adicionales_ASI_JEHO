#########Administracion de Servicios de Internet #################
####Alumno: Jonathan Emmnauel Hernandez Ortiz     #Cuenta: 420054834
####Profesor: Angel Brito Segura
####Semestre 2025-2
################3Envio de Correo al Profesor por SMTP##############

import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuración del remitente
EMAIL_ACCOUNT = "ingjonathan.unamfi@gmail.com"  # correo del alumno
EMAIL_PASSWORD = "tfkkqsozqadbbsds"  # contraseña de aplicacion

# Configuración del destinatario
TO_EMAIL = "angel.brito@fi.unam.edu"

# Crear el mensaje
subject = "Correo Python SMTP JEHO" #asunto del correo
#cuerpo del correo
body = "Hola Profesor Ángel, este es un mensaje de prueba enviado desde Python por correo utilizando SMTP.Mi nombre es Jonathan Emmanuel Hernandez O>rtiz"

msg = MIMEMultipart()
msg["From"] = EMAIL_ACCOUNT #emisor
msg["To"] = TO_EMAIL #receptor
msg["Subject"] = subject #asunto
msg.attach(MIMEText(body, "plain")) #contenido

# Configuramos el proveedor de correo y configurarmos el protocolo de comunicación SMTP, junto con puertos de enlace
if "gmail.com" in EMAIL_ACCOUNT:
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
elif "outlook.com" in EMAIL_ACCOUNT or "hotmail.com" in EMAIL_ACCOUNT:
    smtp_server = "smtp.office365.com"
    smtp_port = 587
else:
    raise ValueError("Proveedor de correo no soportado. Usa Gmail o Outlook.")

# Enviar el correo
try:
    context = ssl.create_default_context()
    server = smtplib.SMTP(smtp_server, smtp_port) #puerto de enlace
    server.starttls(context=context)
    server.login(EMAIL_ACCOUNT, EMAIL_PASSWORD) #iniciamos sesion
    server.sendmail(EMAIL_ACCOUNT, TO_EMAIL, msg.as_string()) #enviamos correo
    server.quit() #cerramos el servidor
    print("Correo enviado exitosamente.")
except Exception as e:
    print(f"Error al enviar el correo: {e}")
