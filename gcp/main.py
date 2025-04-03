
import base64
import json
import requests
from datetime import datetime
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from email.mime.text import MIMEText
from base64 import urlsafe_b64encode

# Parámetros globales
JIRA_URL = "https://nubemsystems.atlassian.net"
JIRA_EMAIL = "USUARIO_ADMIN"
JIRA_API_TOKEN = "TOKEN_API_JIRA"
GMAIL_SENDER = "noreply@nubemsystems.es"

# Función: calcular porcentaje transcurrido
def porcentaje_transcurrido(start_date, due_date):
    fmt = "%Y-%m-%d"
    hoy = datetime.now()
    start = datetime.strptime(start_date, fmt)
    due = datetime.strptime(due_date, fmt)
    total = (due - start).days
    trans = (hoy - start).days
    return min(100, max(0, int(trans / total * 100))) if total > 0 else 100

# Generar correo MIME codificado
def generar_mensaje(destinatario, asunto, html_body):
    mensaje = MIMEText(html_body, "html")
    mensaje["to"] = destinatario
    mensaje["from"] = GMAIL_SENDER
    mensaje["subject"] = asunto
    return {"raw": urlsafe_b64encode(mensaje.as_bytes()).decode()}

# Autenticación Gmail con token guardado
def enviar_correo_gmail(creds, mensaje):
    url = "https://gmail.googleapis.com/gmail/v1/users/me/messages/send"
    headers = {"Authorization": f"Bearer {creds.token}", "Content-Type": "application/json"}
    response = requests.post(url, headers=headers, json=mensaje)
    print(f"Email enviado: {response.status_code} - {response.text}")
    return response

# Obtener tareas de todos los proyectos en JIRA
def obtener_tareas_jira():
    url = f"{JIRA_URL}/rest/api/3/search"
    query = {
        "jql": 'status != Done AND duedate IS NOT EMPTY AND startDate IS NOT EMPTY',
        "maxResults": 100
    }
    response = requests.get(url, auth=(JIRA_EMAIL, JIRA_API_TOKEN), params=query)
    return response.json().get("issues", [])

# Cargar plantilla HTML
def cargar_plantilla(path, data):
    with open(path, "r") as f:
        html = f.read()
    for k, v in data.items():
        html = html.replace(f"{{{{{k}}}}}", v)
    return html

# MAIN
def main(request):
    creds = Credentials.from_authorized_user_file("token_gmail.json", ["https://www.googleapis.com/auth/gmail.send"])
    tareas = obtener_tareas_jira()

    for tarea in tareas:
        fields = tarea["fields"]
        assignee = fields.get("assignee")
        if not assignee: continue

        datos = {
            "usuario": assignee.get("displayName"),
            "email": assignee.get("emailAddress"),
            "proyecto": fields["project"]["name"],
            "tarea": fields["summary"],
            "fecha_limite": fields["duedate"],
            "url_conversacion": "https://chat.openai.com/gpts/editor/hoteltech"
        }
        porcentaje = porcentaje_transcurrido(fields["startDate"], fields["duedate"])

        if porcentaje >= 75:
            plantilla = cargar_plantilla("recordatorio_75_porcentaje.html", datos)
            asunto = "🚨 Alerta Crítica: 75% del tiempo transcurrido"
        elif porcentaje >= 50:
            plantilla = cargar_plantilla("recordatorio_50_porcentaje.html", datos)
            asunto = "⚠️ Recordatorio: 50% del tiempo alcanzado"
        else:
            continue

        mensaje = generar_mensaje(datos["email"], asunto, plantilla)
        enviar_correo_gmail(creds, mensaje)
    return "Proceso completado", 200
