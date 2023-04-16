import pandas as pd
from fpdf import FPDF

df = pd.read_csv('topics.csv')

pdf = FPDF(orientation='P', unit='mm', format='A4', )
pdf.set_auto_page_break(auto=False, margin=0)
page_number = 0

# first page
for index, row in df.iterrows():
    topics = row['Topic']
    num_of_pages = row['Pages']
    # Header
    pdf.add_page()
    page_number += 1
    pdf.set_font(family='Helvetica', style='B', size=16)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=16, txt=topics, align='L', ln=1)
    pdf.line(x1=10, y1=23, x2=200, y2=23)

    # body
    for y in range(50, 265, 15):
        pdf.line(10, y, 200, y)

    # footer
    pdf.ln(258)
    pdf.line(x1=10, y1=285, x2=200, y2=285)
    pdf.set_font(family='Helvetica', style='I', size=8)
    pdf.set_text_color(254, 0, 0)
    pdf.cell(w=0, h=8, align='R', txt=topics + ' ' + str(page_number))

    # note pages
    for page in range(num_of_pages):
        pdf.add_page()
        page_number += 1
        # header
        pdf.set_font(family='Helvetica', style='B', size=12)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=12, txt=f"Notes for {topics}", align='L', ln=1)
        pdf.line(x1=10, y1=23, x2=200, y2=23)

        # body
        for y in range(50, 265, 15):
            pdf.line(10, y, 200, y)

        # footer
        pdf.ln(262)
        pdf.line(x1=10, y1=285, x2=200, y2=285)
        pdf.set_font(family='Helvetica', style='I', size=8)
        pdf.set_text_color(254, 0, 0)
        pdf.cell(w=0, h=8, align='R', txt=topics + ' ' + str(page_number))

pdf.output("python_notes.pdf")
