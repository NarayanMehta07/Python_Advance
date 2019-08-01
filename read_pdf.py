import PyPDF2
pdfFileObj = open('C:/Users/narayanmehta/Desktop/Migration_for_Reciepts/12122016/000065927E_RNWL_HO01H_2017-12-19_00916866.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
pageObj = pdfReader.getPage(0)
print(pageObj.extractText())
