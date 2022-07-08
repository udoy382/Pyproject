import PyPDF2

a = PyPDF2.PdfFileReader('automate the boring stuff with python automate the boring stuff with python ( PDFDrive ).pdf')

# print(a.documentInfo)
# print(a.getNumPages())

str = ""
for i in range(1, 30):
    str += a.getPage(i).extractText()

with open("pdftxt.txt", "w", encoding='utf-8') as f:
    f.write(str)

# search on google [ pypdf2 ] as explore and write your own code
# this program use for extract pdf book text on txt file wit using pypdf2 module
