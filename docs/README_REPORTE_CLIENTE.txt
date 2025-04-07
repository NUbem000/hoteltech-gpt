
────────────────────────────────────────────
📤 INFORME MENSUAL AL CLIENTE – NUBEMFLOW
────────────────────────────────────────────

Al seleccionar esta opción, GPT ejecutará un flujo guiado para generar y enviar un resumen mensual de actividad técnica a un cliente.

────────────────────────────────────────────
🧭 FLUJO GPT
────────────────────────────────────────────

GPT debe preguntar:

1. ¿A qué cliente/proyecto deseas enviar el informe?
2. ¿Qué periodo deseas analizar? (Por defecto: último mes)
3. ¿Deseas incluir:
   - KPIs operativos (SLA, tareas, incidencias)
   - Comentarios personalizados
   - Documentación técnica vinculada?
4. ¿Enviar como PDF adjunto o en cuerpo del correo?
5. ¿Correo electrónico del cliente?

────────────────────────────────────────────
📊 ESTRUCTURA DEL INFORME
────────────────────────────────────────────

1. 📄 Portada:
   - Cliente
   - Periodo
   - Contacto técnico

2. 📊 KPIs:
   - Nº incidencias reportadas
   - SLA cumplidos / vencidos
   - Tareas completadas
   - Tickets críticos gestionados

3. 📂 Actividad destacada:
   - Incidencias más relevantes
   - Fases o entregables completados

4. 🧠 Análisis automatizado:
   - GPT explica los datos
   - Resalta logros y posibles riesgos

5. 📆 Próximas acciones:
   - Hitos próximos
   - Recursos asignados

6. 📎 Adjuntos:
   - PDF del informe
   - Enlaces a Confluence o JIRA

────────────────────────────────────────────
📬 ENVÍO AUTOMÁTICO

- El informe se envía automáticamente por Gmail (desde noreply@nubemsystems.es)
- Puede ser generado por GPT o programado (último día del mes)
- El correo incluirá asunto, cuerpo resumen y el archivo adjunto

────────────────────────────────────────────
🔧 AUTOMATIZACIÓN OPCIONAL

GPT puede generar este informe:

- Cada mes (último día)
- Bajo demanda del usuario
- Por evento específico (fin de sprint, cierre de ticket crítico)

────────────────────────────────────────────
🧠 NOTA

Esta función requiere conexión con:
- JIRA (datos operativos)
- Gmail API (envío)
- Confluence (opcional: documentación técnica)

────────────────────────────────────────────
¿Deseas comenzar ahora? GPT te guiará para seleccionar cliente y periodo.
