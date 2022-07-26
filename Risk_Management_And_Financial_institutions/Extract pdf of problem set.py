from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_file_path = '/Users/martinlukeedwards/Library/Mobile Documents/com~apple~CloudDocs/Finance Job Search/risk_management_and_financial_institutions.pdf'
file_base_name = pdf_file_path.replace('.pdf', '')

pdf = PdfFileReader(pdf_file_path)
pages = [int(i) for i in input('Please provide page numbers: ').split(',')]
#pages = [50, 51] # page 1, 3, 5
pdfWriter = PdfFileWriter()

for page_num in pages:
    pdfWriter.addPage(pdf.getPage(page_num))

chapternumber=input("which chapter?")

with open(f"/Users/martinlukeedwards/Library/Mobile Documents/com~apple~CloudDocs/Finance Job Search/Python/Finance-Project/Risk_Management_And_Financial_institutions/Chapter {chapternumber}/chapter_{chapternumber}_questions.pdf".format(file_base_name), 'wb') as f:
    pdfWriter.write(f)
    f.close()