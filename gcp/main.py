import smtplib
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from flask import Flask, request, jsonify
import requests
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# Datos fijos del correo de salida
GMAIL_SENDER = "noreply@nubemsystems.es"  # Correo de salida
GMAIL_PASSWORD = "nyzukergswjmtfrg"  # Contraseña de aplicación para el correo de salida
JIRA_API_URL = "https://tujira.atlassian.net/rest/api/2/search"  # URL de la API de JIRA

app = Flask(__name__)

# Función para obtener tareas de JIRA
def get_jira_tasks():
    jira_query = {
        "jql": "project = 'HotelTech' AND status != 'Done'",  # Personaliza la consulta JQL
        "fields": ["summary", "assignee", "dueDate", "status", "progress"]
    }
    headers = {
        "Authorization": "Basic <tu_token>",  # Reemplaza <tu_token> con el token de autenticación
        "Content-Type": "application/json"
    }
    response = requests.post(JIRA_API_URL, json=jira_query, headers=headers)
    return response.json()

# Función para generar el cuerpo del correo con el progreso
def generate_email_body(tasks):
    body = "Resumen de tareas en progreso:\n\n"
    for task in tasks:
        body += f"Task: {task['summary']}\n"
        body += f"Assigned to: {task['assignee']['displayName']}\n"
        body += f"Due Date: {task['dueDate']}\n"
        body += f"Status: {task['status']['name']}\n"
        body += f"Progress: {task['progress']['progress']}%\n\n"
    return body

@app.route('/send_email', methods=['POST'])
def send_email():
    try:
        # Obtener datos de la solicitud
        data = request.get_json()
        destinatario = data['destinatario']
        
        # Obtener tareas desde JIRA
        tasks = get_jira_tasks()
        
        # Generar cuerpo del correo
        body = generate_email_body(tasks['issues'])
        
        # Datos de autenticación SMTP
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        # Crear el mensaje
        msg = MIMEMultipart()
        msg['From'] = GMAIL_SENDER
        msg['To'] = destinatario  # Usamos el destinatario proporcionado
        msg['Subject'] = Header("Informe de Progreso de Tareas HotelTech", 'utf-8')

        # Cuerpo del mensaje con codificación UTF-8
        msg.attach(MIMEText(body, 'plain', 'utf-8'))  # Especificamos utf-8 para el cuerpo

        # Enviar el correo
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Seguridad de la conexión
        server.login(GMAIL_SENDER, GMAIL_PASSWORD)
        text = msg.as_string()
        server.sendmail(GMAIL_SENDER, destinatario, text)  # Enviar el correo
        server.quit()

        return jsonify({"status": "success", "message": "Correo enviado con éxito!"}), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
