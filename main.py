import PyPDF2
import re
import requests

file = st.file_uploader('Upload Your Resume', type=(['pdf']))
pdfFileObj = open(file, 'rb')
pdfReader = PyPDF2.PdfReader(pdfFileObj)

text = ""
for page in range(len(pdfReader.pages)):
    pageObj = pdfReader.pages[0]
    text += pageObj.extract_text()

text = re.sub('\s@','@',text)
text = re.sub('\s.com','.com',text)
text = re.sub('\s.ru','.ru',text)
text = re.sub('@\s','@',text)

# Extract email
#email = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
email = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
print(email)
# Extract phone number
phone = re.findall(r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{6}", text)

# Extract skills
skills = re.findall(r'\b(?:C\+\+|Java|Python|SQL|Machine Learning|Data Analysis|Power BI|Tableau|R|SAS)\b', text)
skills = list(set(skills))

# Extract education
education = re.findall(r'Education\n([\s\S]+?)\nLanguages', text)
