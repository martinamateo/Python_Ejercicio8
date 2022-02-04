# Para que envie el email a gmail, hay q desactivar el acceso a aplicaciones 
# poco seguras entrando acá: https://myaccount.google.com/lesssecureapps?
# O reconociendo identidad cuando te llegue el mensage de alerta de gmail (si es q lo tenes activado)

import smtplib 
from email.message import EmailMessage 

email_subject = "Asunto x" #Acá se escribe el asunto.
sender_email_address = "pepito@gmail.com" #Acá se escribe la dire de email del remitente
receiver_email_address = "juancito@gmail.com" #En esta direccion cae el email
email_smtp = "smtp.gmail.com" 
email_password = "xxxxxxxx"  #Acá se escribe la contraseña de email del remitente

# Crear un objeto de mensaje de correo electrónico 
message = EmailMessage() 

# Configure email headers 
message['Subject'] = email_subject 
message['From'] = sender_email_address 
message['To'] = receiver_email_address 

# Cuerpo del email 
message.set_content("Este es un mensaje desde Python") #Acá se escribe el mensaje

# Colocar servidor smtp y puerto
server = smtplib.SMTP(email_smtp, '587') 

# Identifique este cliente en el servidor SMTP
server.ehlo() 

# Asegure la conexión SMTP 
server.starttls() 

# Iniciar sesión en la cuenta de correo electrónico 
server.login(sender_email_address, email_password) 

# Envio de email 
server.send_message(message) 

# Cerrar conexión con el servidor 
server.quit()

