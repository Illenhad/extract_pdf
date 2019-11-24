import pdf_split


if __name__ == '__main__':
    path = input('Enter pdf path: ')
    min_page = int(input('Enter first page: '))
    max_page = int(input('Enter last page: '))
    pdf_split.split(path, min_page, max_page)
