from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

def generate_timetable_pdf(table_headers, table_data, pdf_filename):
    """
    Generates a PDF file containing a timetable table.

    This function creates a PDF document with a formatted table based on the
    provided headers and data. It uses the ReportLab library to construct
    the PDF.

    Args:
        table_headers (list): A list of strings representing the column headers
            of the table.
        table_data (list): A list of lists, where each inner list represents a
            row of data in the table corresponding to the headers.
        pdf_filename (str): The name of the PDF file to be created (including
            the .pdf extension).

    Returns:
        None: This function does not return a value. It prints a success message
        to the console upon completion.
    """
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
    data = [table_headers] + table_data

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

    table = Table(data)
    table.setStyle(table_style)

    elements = []
    elements.append(table)
    doc.build(elements)

    print("PDF generated successfully: " + pdf_filename)
