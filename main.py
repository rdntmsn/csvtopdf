import pandas as pd
from fpdf import FPDF

df = pd.read_csv('topics.csv')

pdf = FPDF(orientation='P', unit='mm', format='A4', )

for index, row in df.iterrows():
    topics = row['Topic']
    num_of_pages = row['Pages']

    pdf.add_page()
    pdf.set_font(family='Helvetica', style='B', size=16)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=16, txt=topics, align='L', ln=1)
    pdf.line(x1=10, y1=23, x2=200, y2=23)
    for page in range(num_of_pages):
        pdf.add_page()
        pdf.set_font(family='Helvetica', style='B', size=12)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=12, txt=f"Notes for {topics}", align='L', ln=1)
        pdf.line(x1=10, y1=23, x2=200, y2=23)

pdf.output("python_notes.pdf")
