#!/usr/bin/env python

#   
# # IIITM-K Live Presentation Downloader 
# 
# ---

# ### Libraries

# In[1]:


import requests # to get image from the web
import PyPDF2
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
from requests.exceptions import HTTPError


# ### Defaults

#imagePrefix = "https://iiitmk.in/bigbluebutton/presentation/810222974f73722d531d1bb037dc39413af2f7b0-1603768399914/810222974f73722d531d1bb037dc39413af2f7b0-1603768399914/c61c612b4583dcf57f29b6b149cedbd61b3082df-1603771038794/svg/"
#num = 1


# ### Inputs
imagePrefix = str(input("Link to the svg folder:"))
if imagePrefix[-1] != "/":
    imagePrefix += '/'
opName = str(input("Enter the name of PDF i.e. to be saved (without .pdf extention): "))
num = int(input("Enter the initial slide number: "))


# ### Creating New File(s)
pdfWriter = PyPDF2.PdfFileWriter()
pdfOutputFile = open(opName+'.pdf', 'wb') 


# ### Downloading

while True:
    try:
        filename = str(num)
        url = imagePrefix + filename
        r = requests.get(url, stream = True)
        r.raise_for_status()
    except HTTPError:
        pdfOutputFile.close()
        get_ipython().system('rm temp.pdf')
        print('Stopping')
        break
    else:
        r.raw.decode_content = True
        drawing = svg2rlg(r.raw)
        renderPDF.drawToFile(drawing, 'temp.pdf')
        # compressPDF('temp.pdf')
        pdfPage = open('temp.pdf', 'rb') # open in read mode
        pdfReader = PyPDF2.PdfFileReader(pdfPage)
        for pageNum in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
            pdfWriter.write(pdfOutputFile)
            pdfPage.close()
        print('Downloaded slide ',num)
        num += 1

####################################

print("Pdf is up!!")


