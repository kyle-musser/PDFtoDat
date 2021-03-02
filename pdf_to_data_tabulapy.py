import tabula
# Get list of PDF in folder
import os
from os import listdir
from os.path import isfile, join
dir = r"C:\Users\g38f293\Dropbox\RA folder\raw_data\IHS\PDFV2/searchable_pdf_pages"

os.chdir(dir)
#This command will turn all searchable pdfs made in "pdf_to_text.py" into datasets
#NOTE: stream option means no lines are in the tables, guess = false makes stream work, area was found in tabula.io this cuts
#       off the top line that messes up the columns
tabula.convert_into_by_batch(dir, output_format="csv",
                             pages="all",
                             stream=True,
                             guess=False,
                             area=[540.964,7.071,4366.605,5650.069]
                             )

