import streamlit as st
from PIL import Image

# Set page title and favicon
st.set_page_config(page_title="Student Registration Form", page_icon=":mortar_board:")

# Set page background
page_bg = """
<style>
body {
background-image: url("https://i.imgur.com/7pUWq6Y.jpg");
background-size: cover;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Set page style
page_style = """
<style>
h1, h2, h3 {
    font-weight: bold;
    text-align: center;
    color: #ffffff;
    margin-bottom: 1rem;
}

label {
    color: #ffffff;
    font-weight: bold;
}

select, input[type="text"] {
    width: 100%;
    padding: 0.5rem 1rem;
    border: none;
    border-radius: 5px;
    margin-bottom: 1rem;
    font-size: 1rem;
    font-weight: bold;
}

select:focus, input[type="text"]:focus {
    outline: none;
}

button {
    background-color: #0069D9;
    color: #ffffff;
    font-size: 1rem;
    font-weight: bold;
    border: none;
    border-radius: 5px;
    padding: 0.5rem 1rem;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

button:hover {
    background-color: #0052A3;
}
</style>
"""
st.markdown(page_style, unsafe_allow_html=True)

# Page content
image = Image.open("https://i.imgur.com/EJzU6Of.png")
st.image(image, use_column_width=True)

st.title("Student Registration Form")
st.subheader("Enter details below")

year_list = ['2013', '2014']
semester_list = ['2013B', '2013J', '2014B', '2014J']

with st.form("StudRegAndCourseForm", clear_on_submit=True):
    col1, col2 = st.beta_columns(2)
    with col1:
        studentID = st.text_input("Student ID")
    with col2:
        withdrawnstatus = st.radio('Withdrawn status', ['Enrolled', 'Withdrawn'])

    col3, col4 = st.beta_columns(2)
    with col3:
        code_presentation = st.selectbox('Semester', semester_list)
    with col4:
        year = st.selectbox('Year', year_list)

    submitted = st.form_submit_button("Submit")

    if submitted:
        st.write("Submitted data:")
        st.write(f"Student ID: {studentID}")
        st.write(f"Withdrawn status: {withdrawnstatus}")
        st.write(f"Semester: {code_presentation}")
        st.write(f"Year: {year}")
