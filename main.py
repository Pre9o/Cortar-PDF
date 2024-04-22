import fitz
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

pdf_name = input('Enter the name of the PDF file: ')
pdf_name = pdf_name if pdf_name.endswith('.pdf') else f'{pdf_name}.pdf'

pdf_path = os.path.join(current_dir, pdf_name)

def main():
    pdf_document = fitz.open(pdf_path)
    print(f'Number of pages in the PDF: {pdf_document.page_count}')

    new_pdf = fitz.open()

    initial_page = int(input('Enter the initial page: '))
    final_page = int(input('Enter the final page: '))

    for page_number in range(initial_page, final_page):
        page = pdf_document.load_page(page_number - 1)
        new_pdf.insert_pdf(pdf_document, from_page=page_number - 1, to_page=page_number)

    new_pdf_path = os.path.join(current_dir, f'{pdf_name.split(".")[0]}_{initial_page}_{final_page}.pdf')
    new_pdf.save(new_pdf_path)

    print(f'New PDF file created: {new_pdf_path}')


if __name__ == '__main__':
    main()