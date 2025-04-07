
# HotelTech GPT – Arquitectura y Herramientas del Proyecto

Este documento resume todas las plataformas, herramientas, APIs y servicios integrados en el ecosistema del proyecto HotelTech GPT.

---

## 🧠 1. ChatGPT (OpenAI)
GPT personalizado con:
- Instrucciones técnicas avanzadas
- Acciones integradas por OpenAPI
- Memoria habilitada (opcional)
- Comportamiento modular (planificación, seguimiento, informes)

### Acciones integradas:
- `send_reminder_email`: Gmail API
- `trigger_hoteltech_reminder`: Cloud Function para recordatorios técnicos
- `generate_pdf_report`: Generación de PDF con opción de envío por correo

---

## ☁️ 2. Google Cloud Platform (GCP)

### Servicios usados:
| Servicio               | Descripción                                  |
|------------------------|----------------------------------------------|
| Cloud Functions        | Lógica backend del GPT (correo, informes)    |
| Cloud Scheduler        | Automatiza recordatorios diarios             |
| Cloud Logging          | Visualiza errores, confirmaciones, ejecuciones |
| IAM & Admin            | Roles de seguridad y acceso                  |
| Gmail SMTP (smtplib)   | Envío de correos desde `noreply@nubemsystems.es` |

---

## 🔧 3. GitHub

Repositorio: `hoteltech-gpt`  
Estructura de carpetas:

- `/gcp/`: funciones para Cloud
- `/deploy-pdf/`, `/deploy-pdf-final/`: versiones de la función PDF
- `/openapi/`: archivos JSON para conectar GPT
- `/docs/`: guías y arquitectura
- `/prompts/`: instrucciones del GPT

---

## 🧪 4. Herramientas de prueba

| Herramienta | Uso |
|-------------|-----|
| Python 3     | Scripts locales (como `test_email.py`) |
| curl         | Llamadas HTTP a funciones desplegadas |
| Postman      | Pruebas visuales de API               |
| VSCode/nano  | Edición y debugging local             |

---

## 📫 5. APIs externas integradas

| API       | Uso |
|-----------|-----|
| Gmail API | Envío de correos (por SMTP, no OAuth en producción) |
| JIRA API  | Consulta de tareas, responsables y progreso         |

---

## 🔐 Seguridad

- Uso de **contraseña de aplicación** (no claves explícitas)
- Fijación del correo emisor (`noreply@nubemsystems.es`)
- Roles de IAM segmentados
- Logs protegidos por permisos de lectura específicos

---

## ✅ Estado Actual

- Función `generatePdfReport`: genera + envía PDF ✔️
- Función `hoteltechReminder`: ejecuta recordatorios ✔️
- GPT configurado con acciones funcionales ✔️
- Cloud Scheduler programado a las 07:00 (hora Madrid) ✔️

---
