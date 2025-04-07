
# 📁 Crear Tareas JIRA – NubemFlow

Este módulo contiene herramientas para automatizar la creación de tareas y subtareas técnicas directamente desde una estructura JSON, basada en planificación previa hecha por GPT.

## Archivos incluidos

### ✅ crear_tareas_jira_v3.py
- Ejecuta autenticación persistente (`jira_credentials.json`)
- Lista todos los proyectos del entorno JIRA
- Solicita selección de proyecto
- Carga tareas desde archivo externo
- Crea tareas y subtareas con asignación automática

### 📄 estructura_demo.json
- Archivo de ejemplo con estructura simulada
- Incluye: tareas, subtareas, descripciones, accountId de responsables

## ¿Cómo ejecutar?

1. Guardar credenciales de JIRA al iniciar por primera vez
2. Seleccionar proyecto desde lista mostrada
3. Asegurarse de que `estructura_demo.json` contenga datos válidos
4. Ejecutar con:
```bash
python3 crear_tareas_jira_v3.py
```

## ¿Qué necesitas?

- Cuenta de JIRA Cloud con permisos de creación de issues
- Token de API generado desde: https://id.atlassian.com/manage/api-tokens
- Tener definidos los tipos "Task" y "Sub-task" en el proyecto JIRA seleccionado

## Próximos pasos

- Integrar este módulo como acción GPT: "Crear planificación aprobada en JIRA"
- Permitir validación previa antes de creación en vivo

