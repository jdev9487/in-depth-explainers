from pypdf import PdfReader, PdfWriter
import sys
import re
import os

latexFile = sys.argv[1]
author = list(filter(lambda x: len(x) > 0,[re.findall(r"\\author{.*}", line) for line in open(latexFile)]))[0][0][8:-1]
title = list(filter(lambda x: len(x) > 0,[re.findall(r"\\title{.*}", line) for line in open(latexFile)]))[0][0][7:-1]
subject = list(filter(lambda x: len(x) > 0,[re.findall(r"\\subtitle{.*}", line) for line in open(latexFile)]))[0][0][10:-1]

pdfFile = sys.argv[2]
reader = PdfReader(os.path.join("output", pdfFile))
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

writer.add_metadata(
    {
        "/Author": author,
        "/Title": title,
        "/Subject": subject
    }
)

with open(os.path.join("output", pdfFile), "wb") as f:
    writer.write(f)