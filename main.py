import pandas as pd
from fpdf import FPDF
import glob
from pathlib import Path

df = pd.read_csv('topics.csv')
animal_files = glob.glob('animals/*.txt')

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf2 = FPDF(orientation='L', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)
pdf2.set_auto_page_break(auto=False, margin=0)
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


# iterate over animal files
for animal_file in animal_files:
    # read animal files
    with open(animal_file, 'r') as af:
        # set animal file variables
        animal_content = af.read()
        animal = Path(animal_file).stem
        sentences = animal_content.split('.')
        formatted_content = '\n'.join([s.strip() + '.' for s in sentences if s])

        animal = animal.capitalize()
        # add and set up the pdfs
        pdf2.add_page()
        pdf2.set_font(family='Helvetica', style='B', size=16)
        pdf2.set_text_color(100, 100, 100)
        pdf2.cell(w=0, h=16, txt=animal, align='L', ln=1)
        pdf2.multi_cell(w=0, h=10, txt=formatted_content, align='L')
        # print(animal)
        # print(animal_content)

pdf.output("python_notes.pdf")
pdf2.output("animals/animals.pdf")
