
from flask import jsonify, make_response, request
from fpdf import FPDF
from io import BytesIO
import base64
import datetime

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Informe de Tareas Pendientes - HotelTech GPT", ln=True, align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Página {self.page_no()}", 0, 0, "C")

    def add_task_table(self, tareas):
        self.set_font("Arial", "B", 10)
        headers = ["Tarea", "Proyecto", "Responsable", "% Tiempo", "Fecha Límite"]
        for header in headers:
            self.cell(38, 10, header, border=1)
        self.ln()
        self.set_font("Arial", "", 10)
        for t in tareas:
            self.cell(38, 10, str(t.get("tarea", ""))[:20], border=1)
            self.cell(38, 10, str(t.get("proyecto", ""))[:20], border=1)
            self.cell(38, 10, str(t.get("usuario", ""))[:15], border=1)
            self.cell(38, 10, f'{t.get("porcentaje_tiempo", 0)}%', border=1)
            self.cell(38, 10, t.get("fecha_limite", ""), border=1)
            self.ln()

def main(request):
    try:
        data = request.get_json(silent=True)
        tareas = data.get("tareas", [])

        pdf = PDF()
        pdf.add_page()
        pdf.add_task_table(tareas)

        pdf_output = BytesIO()
        pdf.output(pdf_output)
        pdf_output.seek(0)

        encoded_pdf = base64.b64encode(pdf_output.read()).decode("utf-8")

        response = {
            "status": "success",
            "message": f"Informe generado con {len(tareas)} tareas.",
            "pdf_base64": encoded_pdf,
            "filename": f"reporte_tareas_{datetime.datetime.now().strftime('%Y%m%d')}.pdf"
        }

        return make_response(jsonify(response), 200)

    except Exception as e:
        return make_response(jsonify({
            "status": "error",
            "message": str(e)
        }), 500)
