#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Implementation of extraction.

    Usage:

    >>> from extract_pdf import extract
    >>> extract('/path/of/pdf', 3, 7)
"""

import os
from PyPDF2 import PdfFileReader, PdfFileWriter

__all__ = ['extract']


def extract(file_path, first_page, last_page):
    """
    Extract pdf
    :param file_path: Path of PDF file
    :param first_page: number of first page
    :param last_page: number of last page
    """
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    new_name = '{}_new.pdf'.format(file_name)
    try:
        pdf = PdfFileReader(file_path)
        pdf_writer = PdfFileWriter()

        for page in range(first_page, last_page+1):
            pdf_writer.addPage(pdf.getPage(page))

        with open(new_name, 'wb') as out:
            pdf_writer.write(out)

        print('Created: {}'.format(new_name))

    except:
        print("file_path: {}".format(file_path))
        print("first_page: {}".format(first_page))
        print("last_page: {}".format(last_page))


if __name__ == '__main__':
    path = input('Enter pdf path: ')
    min_page = int(input('Enter first page: '))
    max_page = int(input('Enter last page: '))
    extract(path, min_page, max_page)
