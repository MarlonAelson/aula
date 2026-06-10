from fpdf import FPDF, YPos, XPos

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", size=12)
pdf.cell(200, 10, text="Meu primeiro PDF gerado com Python!", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
pdf.output("meu_arquivo.pdf")
