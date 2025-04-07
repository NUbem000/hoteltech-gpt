
import datetime
import base64
from fpdf import FPDF
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.header import Header

# Datos del emisor
GMAIL_SENDER = "noreply@nubemsystems.es"
GMAIL_PASSWORD = "qinjvieshbcicjci"

# Simulación de datos
cliente = "Hotel Majestic"
proyecto = "HTX"
periodo = "Marzo 2025"
email_destino = "gestion@hoteltech.com"

kpis = {
    "incidencias_reportadas": 23,
    "sla_cumplidos": 20,
    "sla_fallidos": 3,
    "tareas_completadas": 14,
    "tickets_criticos": 2
}

# Crear PDF
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, f"Informe mensual - {cliente}", ln=True, align="C")
        self.set_font("Arial", "", 10)
        self.cell(0, 10, f"Proyecto: {proyecto} | Periodo: {periodo}", ln=True, align="C")
        self.ln(10)

    def section(self, title, content):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, ln=True)
        self.set_font("Arial", "", 10)
        for line in content:
            self.cell(0, 8, f"- {line}", ln=True)
        self.ln()

pdf = PDF()
pdf.add_page()

pdf.section("📊 KPIs",
    [f"{k}: {v}" for k, v in kpis.items()]
)

pdf.section("🧠 Análisis GPT",
    ["Este mes se ha mantenido un buen ritmo de resolución.",
     "Se recomienda reforzar el soporte técnico en los próximos cierres de fase."])

pdf.section("📆 Próximos pasos",
    ["Entrega Wi-Fi (10/04)", "Inicio CCTV (15/04)", "Retro semanal (12/04)"])

pdf_bytes = pdf.output(dest='S').encode('latin1')

# Preparar y enviar correo
mensaje = MIMEMultipart()
mensaje["From"] = GMAIL_SENDER
mensaje["To"] = email_destino
mensaje["Subject"] = Header(f"📄 Informe NubemFlow – {cliente} – {periodo}", 'utf-8')

cuerpo = MIMEText("Adjunto encontrarás el resumen mensual del proyecto.

Saludos,
Equipo NubemFlow", 'plain', 'utf-8')
mensaje.attach(cuerpo)

adjunto = MIMEApplication(pdf_bytes, _subtype="pdf")
adjunto.add_header("Content-Disposition", "attachment", filename="informe_mensual.pdf")
mensaje.attach(adjunto)

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(GMAIL_SENDER, GMAIL_PASSWORD)
    server.sendmail(GMAIL_SENDER, email_destino, mensaje.as_string())
    server.quit()
    print("✅ Informe enviado con éxito.")
except Exception as e:
    print(f"❌ Error al enviar el informe: {e}")
