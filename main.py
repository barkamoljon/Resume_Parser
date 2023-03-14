import nltk
nltk.download('wordnet')
import streamlit as st
import pandas as pd
import base64, random
import time, datetime
from pyresparser import ResumeParser
from pdfminer3.layout import LAParams, LTTextBox
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfinterp import PDFResourceManager
from pdfminer3.pdfinterp import PDFPageInterpreter
from pdfminer3.converter import TextConverter
import io, random
from streamlit_tags import st_tags
from PIL import Image
import pymysql
import pafy
import plotly.express as px

# Download wordnet
nltk.download('wordnet')

# Create connection to database
connection = pymysql.connect(host='localhost', user='root', password='', db='sra')
cursor = connection.cursor()

# Create the DB if it doesn't exist
db_sql = """CREATE DATABASE IF NOT EXISTS SRA;"""
cursor.execute(db_sql)

@st.cache()
def fetch_yt_video(link):
    video = pafy.new(link)
    return video.title

def get_table_download_link(df, filename, text):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">{text}</a>'
    return href

def pdf_reader(file):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle, laparams=LAParams())
    page_interpreter = PDFPageInterpreter(resource_manager, converter)
    with open(file, 'rb') as fh:
        for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
            page_interpreter.process_page(page)
        text = fake_file_handle.getvalue()

    # close open handles
    converter.close()
    fake_file_handle.close()
    return text

def show_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

def course_recommender(course_list):
    st.subheader("Courses & Certificates🎓 Recommendations")
    rec_course = [c_name for c_name, c_link in course_list[:no_of_reco]]
    st.write('\n'.join([f"({i+1}) [{name}]({link})" for i, (name, link) in enumerate(course_list[:no_of_reco])]))
    return rec_course

def insert_data(name, email, res_score, timestamp, no_of_pages, reco_field, cand_level, skills, recommended_skills, courses):
    DB_table_name = 'user_data'
    insert_sql = "insert into " + DB_table_name + """ values (0,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    rec_values = (name, email, str(res_score), timestamp, str(no_of_pages), reco_field, cand_level, skills, recommended_skills, courses)
    cursor.execute(insert_sql, rec_values)
    connection.commit()

def run():
    st.set_page_config(page_title="Smart Resume Parser", page_icon='./Logo/Logo.ico')

    st.title("Smart Resume Parser")

    # Sidebar for user type
    activities = ["Normal User", "Admin"]
    choice = st.sidebar.selectbox("Choose among the given options:", activities)

    img = Image.open('./Logo/Logo.webp')
    img = img.resize((250, 250))
    st.image(img)

    # Parsing user input
    if choice == "Normal User":
      # Code for normal user...
      pass 
    else:
      # Code for admin...
      pass

run()
