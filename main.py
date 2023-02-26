
import streamlit as st
import datetime

st.title("Student Registation Form") 
st.subheader("Enter details below")

#Generate list of year
this_year = datetime.datetime.now().year
year_list = list(range(this_year-10, this_year+1))

with st.form("StudRegAndCourseForm", clear_on_submit=True): 
	studentID = st.text_input("Enter student ID") 
	code_presentation= st.text_input("Enter code_presentation(semester)") 
        selected_year = st.selectbox('Select year', year_list)
        withdrawnstatus = st.radio('Select an withdrawn status', ['0', '1'])
	button= st.form_submit_button("Submit")

