
# 🚀 Despliegue en Google Cloud Functions – HotelTech GPT Notifier

Este módulo automatiza el envío de correos de recordatorio vía Gmail API cuando las tareas en JIRA superan el 50% o 75% de su tiempo asignado.

---

## ✅ Requisitos Previos

1. Cuenta de Google Cloud
2. Proyecto habilitado en [Google Cloud Console](https://console.cloud.google.com/)
3. API de Gmail habilitada
4. Archivo `token_gmail.json` con credenciales OAuth generadas

---

## 🧰 Archivos incluidos

- `main.py`: Función principal con integración JIRA + Gmail
- `requirements.txt`: Librerías requeridas
- `recordatorio_50_porcentaje.html` y `recordatorio_75_porcentaje.html`: Plantillas HTML para emails

---

## 🛠️ Paso a Paso

### 1. Crear credenciales OAuth Gmail

- Ve a Google Cloud Console → API & Services → Credentials
- Crea un OAuth Client ID (tipo: Desktop App)
- Descarga el archivo `credentials.json`
- Usa el siguiente script para generar `token_gmail.json`:
  ```bash
  pip install --upgrade google-auth google-auth-oauthlib
  python -m google.auth.transport.requests
  ```

### 2. Subir a Cloud Functions

```bash
gcloud functions deploy hoteltechReminder   --runtime python310   --trigger-http   --allow-unauthenticated   --entry-point main   --region europe-west1
```

### 3. Configurar Cloud Scheduler

```bash
gcloud scheduler jobs create http daily-gpt-notifier   --schedule="0 7 * * *"   --time-zone="Europe/Madrid"   --http-method=GET   --uri="https://REGION-PROJECT.cloudfunctions.net/hoteltechReminder"
```

---

## 🧪 Prueba Local (opcional)

```bash
python main.py
```

Asegúrate de tener un archivo `token_gmail.json` en el mismo directorio.

---

## 📫 Contacto técnico

Configura `JIRA_EMAIL`, `JIRA_API_TOKEN` y `GMAIL_SENDER` dentro de `main.py` antes del despliegue.
