
# 📄 NubemFlow – Documentación de Acciones GPT (OpenAPI)

Este archivo describe todas las acciones disponibles e integradas en el asistente GPT personalizado **NubemFlow**, mediante el uso de especificaciones OpenAPI.

---

## 🔗 Dominio base

Todas las funciones están alojadas en:

```
https://europe-west1-hoteltech-gmail-api.cloudfunctions.net
```

---

## ✅ Acciones disponibles

| Acción                    | Método | Ruta                         | Descripción |
|---------------------------|--------|------------------------------|-------------|
| `send_reminder_email`     | POST   | `/gmail/v1/users/me/messages/send` | Enviar correos manuales a responsables |
| `trigger_hoteltech_reminder` | GET | `/`                          | Ejecutar recordatorio diario de tareas |
| `generate_pdf_report`     | POST   | `/generate`                  | Generar informe PDF desde lista de tareas |
| `crearEstructuraEnJIRA`   | POST   | `/crearEstructuraEnJIRA`     | Crear tareas y subtareas en JIRA desde estructura GPT |

---

## 📥 ¿Cómo importar?

1. Entra a [https://chat.openai.com/gpts/editor](https://chat.openai.com/gpts/editor)
2. En la sección **Acciones**, haz clic en **"Importar desde URL"**
3. Usa la siguiente URL:

```
https://raw.githubusercontent.com/NUbem000/hoteltech-gpt/main/openapi/nubemflow_actions_final.json
```

4. Verifica que todas las acciones aparecen listadas
5. Guarda el GPT

---

## 🧩 Archivo relacionado

- `openapi/nubemflow_actions_final.json`: archivo OpenAPI que contiene todas las acciones actuales

---

## 📌 Recomendación

Mantener este README sincronizado con las acciones reales y versiones de funciones desplegadas. Para nuevas acciones, añade la descripción y su endpoint aquí.

