from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

def generate_timetable_pdf(table_headers, table_data, pdf_filename):
    # Initialize the PDF document
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter)

    # Create the table data
    data = [table_headers] + table_data

    # Define the table style
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])

    # Create the table object
    table = Table(data)
    table.setStyle(table_style)

    # Build the PDF document
    elements = []
    elements.append(table)
    doc.build(elements)

    print("PDF generated successfully: " + pdf_filename)