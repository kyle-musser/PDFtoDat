from PIL import Image
import pytesseract
import sys
from pdf2image import convert_from_path
import os
import PyPDF2

# Get list of PDF in folder
from os import listdir
from os.path import isfile, join
dir = r"C:/Users/g38f293/Dropbox/RA folder/raw_data/IHS/PDFV2/rotate_all_files"
pdfs = [f for f in listdir(dir) if isfile(join(dir, f))]
outdir = r"C:/Users/g38f293/Dropbox/RA folder/raw_data/IHS/PDFV2/searchable_pdf_pages"
os.chdir(dir)




for pdf in pdfs:
    print(pdf)
    # 1 : Converting each PDF page to images
    # Store all the pages of the PDF in a variable
    os.chdir(dir)
    pages = convert_from_path(pdf, 500)

    # Counter to store images of each page of PDF to image
    image_counter = 1

    # Iterate through all the pages stored above
    for page in pages:
        os.chdir(outdir)
        # remove .pdf extension from filename
        pdfname = pdf.replace(".pdf", "")

        # Declaring filename for each page of PDF as JPG
        filename = str(pdfname)+str(image_counter)+".jpg"

        # Save the image of the page in system
        page.save(filename, 'JPEG')

        # Increment the counter to update filename
        image_counter = image_counter + 1

    # 2 - Recognizing text from the images using OCR
    # Variable to get count of total number of pages
    filelimit = image_counter-1

    # Iterate from 1 to total number of pages
    for i in range(1, filelimit + 1):
        print(i)

        pdfname = pdf.replace(".pdf", "")
        outdir = outdir

        #make file names
        filename_jpg = str(pdfname)+str(i)+".jpg"
        filename_pdf = str(pdfname) + "_" + "pg" + str(i) + ".pdf"
        print(filename_pdf)

        # Convert PDF to searchable PDF to use with Tabula
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        pdf_wSText = pytesseract.image_to_pdf_or_hocr(Image.open(filename_jpg), extension='pdf')
        f = open(filename_pdf, 'w+b')
        f.write(bytearray(pdf_wSText))
        f.close()


    #Make one PDF to combine all pages,
    mergedpdf = PyPDF2.PdfFileMerger()
    for i in range(1, filelimit + 1):
        filename_pdf = str(pdfname) + "_" + "pg" + str(i) + ".pdf"
        mergedpdf.append(PyPDF2.PdfFileReader(filename_pdf, 'rb'))

    mergedpdf.write(pdf)




