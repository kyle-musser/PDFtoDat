# PDFtoDat
Project to convert scanned pdfs obtained from the Indian Health Service into a usable panel of health locations, year-over-year. 

"pdf_to_text.py" : takes an input folder of scanned pdf's (non-searchable) and coverts each pdf the the folder into a searchable pdf using tesseract_ocr (). 

"pdf_to_data_tabula.py" : uses tabula to convert searchable pdf's created in (pdf_to_text) into usable csv datasets.

