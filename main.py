import streamlit as st
import datetime

st.title("Student Registration Form")
st.subheader("Enter details below")

# Generate list of years
this_year = datetime.datetime.now().year
year_list = list(range(this_year - 10, this_year + 1))

semester = ['2013B', '2013J', '2014B', '2014J']


with st.form("StudRegAndCourseForm", clear_on_submit=True):
    studentID = st.text_input("Enter student ID")
    code_presentation = st.selectbox('Select semester', semester)
    year = st.selectbox('Select year', year_list)
    withdrawnstatus = st.radio('Select a withdrawn status', ['0', '1'])
    button = st.form_submit_button("Submit")
    
st.write(studentID)
st.write(withdrawnstatus)
st.write(year)
st.write(code_presentation)
