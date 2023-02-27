import streamlit as st
import datetime

# Set page layout
st.set_page_config(
    page_title="Student Registration Form",
    page_icon=":mortar_board:",
    layout="wide"
)

# Define page header
st.title("Student Registration Form")
st.subheader("Enter details below")

# Define form layout
row1_spacer1, row1_col1, row1_spacer2 = st.beta_columns((.1, 1, .1))
with row1_col1:
    with st.form("StudRegAndCourseForm", clear_on_submit=True):
        # Define form inputs
        studentID = st.text_input("Enter student ID")
        code_presentation = st.selectbox('Select semester', semester)
        year = st.selectbox('Select year', year_list)
        withdrawnstatus = st.radio('Select a withdrawn status', ['0', '1'])
        button = st.form_submit_button("Submit")
        
# Define form output
if button:
    row2_spacer1, row2_col1, row2_spacer2 = st.beta_columns((.1, 1, .1))
    with row2_col1:
        st.write("**Student Registration Form Output:**")
        st.write("- Student ID: ", studentID)
        st.write("- Withdrawn Status: ", withdrawnstatus)
        st.write("- Year: ", year)
        st.write("- Semester: ", code_presentation)
