import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path
import os

def generate(invoice_path,pdf_path,product_id,product_name,amount_purchased,
             price_per_unit,total_price):
    """
    THIS FUNCTION CONVERTS EXCEL FILES TO PDF INVOICES"""

    filepaths=glob.glob(f"{invoice_path}/*.xlsx")
    for filepath in filepaths:
        
        pdf=FPDF(orientation="P",unit="mm",format="A4")
        filename=Path(filepath).stem
        
        invoice_nr,date=filename.split("-")
        
        pdf.add_page()
        pdf.set_font(family="Times",size=16,style="B")
        pdf.cell(w=50,h=8,txt=f"Invoice number {invoice_nr}",ln=1)
        
        pdf.set_font(family="Times",size=16,style="B")
        pdf.cell(w=50,h=8,txt=f"Date {date}",ln=1)
        
        df=pd.read_excel(filepath)
        columns=(df.columns)
        columns=[item.replace("'"," ").title() for item in columns]
        pdf.set_font(family="Times",size=10, style="B")
        pdf.set_text_color(80,80,80)
        pdf.cell(w=30,h=10,txt=str(columns[1]),border=1)
        pdf.cell(w=50,h=10,txt=str((columns[1])),border=1)
        pdf.cell(w=50,h=10,txt=str(columns[2]),border=1)
        pdf.cell(w=30,h=10,txt=str(columns[3]),border=1)
        pdf.cell(w=30,h=10,txt=str(columns[4]),border=1,ln=1)
        for index,row in df.iterrows():
            pdf.set_font(family="Times",size=10)
            pdf.set_text_color(80,80,80)
            pdf.cell(w=30,h=10,txt=str(row[product_id]),border=1)
            pdf.cell(w=50,h=10,txt=str(row[product_name]),border=1)
            pdf.cell(w=50,h=10,txt=str(row[amount_purchased]),border=1)
            pdf.cell(w=30,h=10,txt=str(row[price_per_unit]),border=1)
            pdf.cell(w=30,h=10,txt=str(row[total_price]),border=1,ln=1)
        total_sum=df["total_price"].sum()
        pdf.set_font(family="Times",size=10)
        pdf.set_text_color(80,80,80)
        pdf.cell(w=30,h=10,txt="",border=1)
        pdf.cell(w=50,h=10,txt="",border=1)
        pdf.cell(w=50,h=10,txt="",border=1)
        pdf.cell(w=30,h=10,txt="",border=1)
        pdf.cell(w=30,h=10,txt=str(total_sum),border=1,ln=1)
        
        pdf.set_font(family="Times",size=20,style="B")
        pdf.cell(w=30,h=10,txt=f"The total price is {total_sum}",ln=1)
        #if not os.path.exists(pdf_path):    
            #os.makedirs(pdf_path)
        pdf.output(f"{pdf_path}/{filename}.pdf")

        