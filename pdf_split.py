import os
from PyPDF2 import PdfFileReader, PdfFileWriter


def extract(path, min_page, max_page):
    """
    Extract pdf
    :param path: Path of PDF file
    :param min_page: number of first page
    :param max_page: number of last page
    """
    file_name = os.path.splitext(os.path.basename(path))[0]
    new_name = '{}_new.pdf'.format(file_name)
    pdf = PdfFileReader(path)

    pdf_writer = PdfFileWriter()
    for page in range(min_page-1, max_page):

        pdf_writer.addPage(pdf.getPage(page))

    with open(new_name, 'wb') as out:
        pdf_writer.write(out)

    print('Created: {}'.format(new_name))
