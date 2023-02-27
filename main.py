import streamlit as st

st.set_page_config(page_title="Student Registration Form", page_icon=":pencil:", layout="wide")

year_list = ['2013','2014']
semester = ['2013B', '2013J', '2014B', '2014J']

# Add some custom CSS
st.markdown("""
        <style>
            .stApp {
                background-color: #F4F4F4;
            }
            .stForm {
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0px 2px 20px rgba(0, 0, 0, 0.1);
                background-color: #FFFFFF;
            }
            .stTextInput {
                border-radius: 5px;
                border: 2px solid #E5E5E5;
                padding: 8px;
                margin-bottom: 10px;
                font-size: 16px;
            }
            .stSelectbox {
                border-radius: 5px;
                border: 2px solid #E5E5E5;
                padding: 8px;
                margin-bottom: 10px;
                font-size: 16px;
            }
            .stRadio {
                margin-bottom: 10px;
            }
            .stButton {
                border-radius: 5px;
                padding: 10px 20px;
                margin-top: 20px;
                background-color: #0078FF;
                color: #FFFFFF;
                font-size: 16px;
            }
            .stButton:hover {
                background-color: #005BE3;
            }
        </style>
    """, unsafe_allow_html=True)

with st.form("StudRegAndCourseForm", clear_on_submit=True):
    st.title("Student Registration Form")
    st.subheader("Enter details below")

    studentID = st.text_input("Enter student ID", key="studentID", value="")
    code_presentation = st.selectbox('Select semester', semester, key="code_presentation")
    year = st.selectbox('Select year', year_list, key="year")
    withdrawnstatus = st.radio('Select a withdrawn status', ['0', '1'], key="withdrawnstatus")
    button = st.form_submit_button("Submit")

    if button:
        st.write(studentID)
        st.write(withdrawnstatus)
        st.write(year)
        st.write(code_presentation)
