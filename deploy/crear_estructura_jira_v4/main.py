
from flask import request, jsonify, make_response
import requests
import os
import base64

def main(request):
    try:
        data = request.get_json(silent=True)

        project_key = data.get("project_key")
        estructura = data.get("tareas", [])
        email = os.environ.get("JIRA_EMAIL")
        token = os.environ.get("JIRA_API_TOKEN")

        if not email or not token:
            return make_response(jsonify({"status": "error", "message": "Credenciales JIRA no configuradas"}), 400)

        auth = base64.b64encode(f"{email}:{token}".encode()).decode()
        headers = {
            "Authorization": f"Basic {auth}",
            "Content-Type": "application/json"
        }

        created = []
        errores = []

        for tarea in estructura:
            if not tarea.get("titulo") or not tarea.get("asignado_a"):
                errores.append(f"Tarea sin título o asignado: {tarea}")
                continue

            payload = {
                "fields": {
                    "project": {"key": project_key},
                    "summary": tarea["titulo"],
                    "description": tarea.get("descripcion", "Generado por NubemFlow"),
                    "issuetype": {"name": "Task"},
                    "assignee": {"accountId": tarea["asignado_a"]},
                    "duedate": tarea.get("fecha_limite")
                }
            }
            res = requests.post("https://nubemsystems.atlassian.net/rest/api/3/issue", headers=headers, json=payload)
            if res.status_code in (200, 201):
                key = res.json().get("key")
                created.append(key)
                for sub in tarea.get("subtareas", []):
                    if not sub.get("titulo") or not sub.get("asignado_a"):
                        errores.append(f"Sub sin datos: {sub}")
                        continue
                    sub_payload = {
                        "fields": {
                            "project": {"key": project_key},
                            "summary": sub["titulo"],
                            "description": sub.get("descripcion", f"Subtarea de {key}"),
                            "issuetype": {"name": "Sub-task"},
                            "assignee": {"accountId": sub["asignado_a"]},
                            "parent": {"key": key},
                            "duedate": sub.get("fecha_limite")
                        }
                    }
                    sub_res = requests.post("https://nubemsystems.atlassian.net/rest/api/3/issue", headers=headers, json=sub_payload)
                    if sub_res.status_code in (200, 201):
                        created.append(sub_res.json().get("key"))
                    else:
                        errores.append(f"Sub '{sub['titulo']}' → {sub_res.status_code}: {sub_res.text}")
            else:
                errores.append(f"Tarea '{tarea['titulo']}' → {res.status_code}: {res.text}")

        # Guardar resultado en archivo local (opcional)
        with open("/tmp/resultados_creacion.json", "w") as f:
            import json
            json.dump({"created_keys": created, "errores": errores}, f, indent=2)

        return make_response(jsonify({
            "status": "success",
            "created_keys": created,
            "errores": errores
        }), 200)

    except Exception as e:
        return make_response(jsonify({
            "status": "error",
            "message": str(e)
        }), 500)
