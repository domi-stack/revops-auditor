from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf(score, insights, filename="report.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 750, "RevOps Audit Report")

    c.setFont("Helvetica", 12)
    c.drawString(50, 720, f"RevOps Score: {score}/100")

    y = 690
    c.drawString(50, y, "Insights:")

    y -= 20

    for i in insights:
        c.drawString(50, y, f"- {i}")
        y -= 20
        if y < 50:
            c.showPage()
            y = 750

    c.save()

    return filename
