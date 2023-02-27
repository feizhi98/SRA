import streamlit as st
import datetime

st.set_page_config(page_title="Student Registration Form", page_icon=":mortar_board:")

st.title("Student Registration Form")
st.subheader("Enter details below")

year_list = ['2013', '2014']
semester_list = ['2013B', '2013J', '2014B', '2014J']

with st.form("StudRegAndCourseForm", clear_on_submit=True):
    # Input fields for student details
    col1, col2 = st.beta_columns(2)
    with col1:
        studentID = st.text_input("Student ID")
    with col2:
        withdrawnstatus = st.radio('Withdrawn status', ['Enrolled', 'Withdrawn'])

    # Select boxes for semester and year
    col3, col4 = st.beta_columns(2)
    with col3:
        code_presentation = st.selectbox('Semester', semester_list)
    with col4:
        year = st.selectbox('Year', year_list)

    # Submit button
    submitted = st.form_submit_button("Submit")

    # Show submitted data
    if submitted:
        st.write("Submitted data:")
        st.write(f"Student ID: {studentID}")
        st.write(f"Withdrawn status: {withdrawnstatus}")
        st.write(f"Semester: {code_presentation}")
        st.write(f"Year: {year}")
