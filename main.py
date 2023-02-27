import streamlit as st
import datetime

st.set_page_config(page_title="Student Registration Form", page_icon=":mortar_board:")

st.title("Student Registration Form")
st.subheader("Enter details below")

year_list = ['2013','2014']
semester = ['2013B', '2013J', '2014B', '2014J']

with st.form("StudRegAndCourseForm", clear_on_submit=True):
    studentID = st.text_input("Enter student ID")
    code_presentation = st.selectbox('Select semester', semester)
    year = st.selectbox('Select year', year_list)
    withdrawnstatus = st.radio('Select a withdrawn status', ['0', '1'])
    button = st.form_submit_button("Submit")

    if button:
        st.write(studentID)
        if withdrawnstatus:
            st.write(withdrawnstatus)
        if year:
            st.write(year)
        st.write(code_presentation)
