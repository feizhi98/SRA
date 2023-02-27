import streamlit as st

# Set page layout and background color
st.set_page_config(page_title="Student Registration Form", page_icon=":pencil2:", layout="wide", initial_sidebar_state="expanded")
page_bg = '''
<style>
body {
background-image: url("https://images.unsplash.com/photo-1519681393784-d120267933ba");
background-size: cover;
}
</style>
'''
st.markdown(page_bg, unsafe_allow_html=True)

# Create form
with st.form("StudRegAndCourseForm", clear_on_submit=True):
    # Set form columns
    col1, col2 = st.beta_columns(2)

    with col1:
        st.subheader("Student Details")
        studentID = st.text_input("Enter student ID")
        withdrawnstatus = st.radio('Select a withdrawn status', ['0', '1'])
        button = st.form_submit_button("Submit")

    with col2:
        st.subheader("Semester Details")
        year_list = ['2013','2014']
        year = st.selectbox('Select year', year_list)
        semester = ['2013B', '2013J', '2014B', '2014J']
        code_presentation = st.selectbox('Select semester', semester)

    if button:
        st.write(f"Student ID: {studentID}")
        st.write(f"Withdrawn Status: {withdrawnstatus}")
        st.write(f"Year: {year}")
        st.write(f"Semester: {code_presentation}")
