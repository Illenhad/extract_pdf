import os
from PyPDF2 import PdfFileReader, PdfFileWriter


def split(path, min_page, max_page):
    file_name = os.path.splitext(os.path.basename(path))[0]

    pdf = PdfFileReader(path)
    for page in range(min_page-1, max_page):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        output_filename = '{}_page_{}.pdf'.format(
            file_name, page + 1
        )

        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)

        print('Created: {}'.format(output_filename))
