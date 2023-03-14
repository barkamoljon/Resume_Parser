import base64
import datetime
import io
import random

import nltk
import pandas as pd
import pymysql
import pafy
import plotly.express as px
import streamlit as st
from nltk.tokenize import word_tokenize
from pdfminer3.converter import TextConverter
from pdfminer3.layout import LAParams, LTTextBox
from pdfminer3.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer3.pdfpage import PDFPage
from PIL import Image
from pyresparser import ResumeParser
from streamlit_tags import st_tags


nltk.download("punkt")
nltk.download("wordnet")

# Establish database connection
connection = pymysql.connect(host="localhost", user="root", password="", db="sra")
cursor = connection.cursor()


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
    with open(file, "rb") as fh:
        for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
            page_interpreter.process_page(page)
            print(page)
        text = fake_file_handle.getvalue()

    # close open handles
    converter.close()
    fake_file_handle.close()
    return text


def show_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)


def course_recommender(course_list):
    st.subheader("Courses & Certificates🎓 Recommendations")
    c = 0
    rec_course = []
    no_of_reco = st.slider("Choose Number of Course Recommendations:", 1, 10, 4)
    random.shuffle(course_list)
    for c_name, c_link in course_list:
        c += 1
        st.markdown(f"({c}) [{c_name}]({c_link})")
        rec_course.append(c_name)
        if c == no_of_reco:
            break
    return rec_course


def insert_data(
    name, email, res_score, timestamp, no_of_pages, reco_field, cand_level, skills, recommended_skills, courses
):
    DB_table_name = "user_data"
    insert_sql = f"insert into {DB_table_name} values (0,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    rec_values = (
        name,
        email,
        str(res_score),
        timestamp,
        str(no_of_pages),
        reco_field,
        cand_level,
        skills,
        recommended_skills,
        courses,
    )
    cursor.execute(insert_sql, rec_values)
    connection.commit()


st.set_page_config

