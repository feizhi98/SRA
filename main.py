import streamlit as st

# Set page configurations
st.set_page_config(page_title="Student Registration Form", page_icon=":mortar_board:")

# Define the function to display the registration form
def registration_form():
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

# Define the function to display the Assessment page
def assessment():
    st.title("Assessment Page")
    st.write("This is the Assessment page")

# Define the function to display the Vle page
def vle():
    st.title("Vle Page")
    st.write("This is the Vle page")

# Define the function to display the studentInfo page
def student_info():
    st.title("Student Info Page")
    st.write("This is the Student Info page")

# Create the menu items and their respective pages
menu_items = {
    "Home": lambda: st.write("Welcome to the Student Registration Form!"),
    "Registration Form": registration_form,
    "Assessment": assessment,
    "Vle": vle,
    "Student Info": student_info
}

# Create the sidebar menu
menu_choice = st.sidebar.selectbox("Select a page", list(menu_items.keys()))

# Display the selected page
menu_items[menu_choice]()
