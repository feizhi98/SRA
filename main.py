import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Setting the page title and favicon
st.set_page_config(page_title='Student Registration Form', page_icon="📚")

# Setting the page background
page_bg = """
<style>
body {
background-image: url("https://cdn.pixabay.com/photo/2016/06/29/08/45/books-1481985_960_720.jpg");
background-size: cover;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)


# Adding a header and subheader
st.write("""
# Student Registration Form
""")
st.write("""
## Enter details below
""")

# Creating form fields
year_list = ['2013','2014']
semester = ['2013B', '2013J', '2014B', '2014J']

with st.form("StudRegAndCourseForm", clear_on_submit=True):
    studentID = st.text_input("Enter student ID")
    code_presentation = st.selectbox('Select semester', semester)
    year = st.selectbox('Select year', year_list)
    withdrawnstatus = st.radio('Select a withdrawn status', ['0', '1'])
    button = st.form_submit_button("Submit")

    # Displaying form submission data
    if button:
        st.write("### Form Submission Data")
        st.write(f"Student ID: {studentID}")
        st.write(f"Withdrawn Status: {withdrawnstatus}")
        st.write(f"Year: {year}")
        st.write(f"Semester: {code_presentation}")
