from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=14)

pdf.cell(200, 10, txt="Hello World en PDF", ln=1, align="C")
pdf.cell(200, 10, txt="PDF generado con python", ln=1, align="C")

pdf.output("archivo_pdf.pdf")