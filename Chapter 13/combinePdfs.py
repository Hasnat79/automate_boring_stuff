#!/usr/bin/env python3
#combinePdfs.py - Combines all the PDFs in the current working directory into 
# a single PDF.

import PyPDF2,os

# get all the pdf filenames
pdfFiles=[]
os.chdir("/home/hasnat/Desktop/automate_boring_stuff/Chapter 13")
for filename in os.listdir("."):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)
pdfWriter=PyPDF2.PdfFileWriter()

# loop through all the pdf files 0
for filename in pdfFiles:
    pdfFileObj = open(filename,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # Loop through all the pages (except the first) and add them.
    for pageNum in range(1,pdfReader.numPages):
        pageObj=pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
# save the resulting PDF to a file
pdfOutput=open('allminutes.pdf','wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
