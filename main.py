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
            if code_presentation:
                st.write(code_presentation)

# Define the function to display the Assessment form
def assessment():
    st.title("Assessment Form")
    st.subheader("Enter details below")

    year_list = ['2013','2014']
    semester = ['2013B', '2013J', '2014B', '2014J']
    code_module = ['AAA','BBB','CCC','DDD','EEE','FFF','GGG']

    with st.form("StudRegAndCourseForm", clear_on_submit=True):
        studentID = st.text_input("Enter student ID")
        code_presentation = st.selectbox('Select semester', semester)
        course = st.selectbox('Select code module', code_module)
        year = st.selectbox('Select year', year_list)
        late_submit = st.radio('Select late submission status', ['0', '1'])
        result = st.radio('Select result', ['Pass', 'Fail'])
        button = st.form_submit_button("Submit")

        if button:
            st.write(studentID)
            if code_presentation:
                st.write(code_presentation)
            if course:
                st.write(course)
            if year:
                st.write(year)
            if late_submit:
                st.write(late_submit)
            if result:
                st.write(result)

# Define the function to display the Vle page
def vle():
    st.title("Virtual Learning Environment(VLE) Form")
    st.subheader("Enter details below")

    activity = ['dataplus', 'forumng', 'homepage', 'oucontent','resource','subpage','url','quiz','glossary','ouelluminate','oucollaborate','sharedsubpage']

    with st.form("StudRegAndCourseForm", clear_on_submit=True):
        activity_type = st.selectbox('Select semester', activity)
        sum_click = st.text_input("Enter sum of clicks")

        if button:
            if activity_type:
                st.write(activity_type)
            st.write(sum_click)

        
# Define the function to display the studentInfo page
def student_info():
    st.title("Student Info Page")
    st.write("This is the Student Info page")

# Create the menu items and their respective pages
menu_items = {
    "Home": lambda: st.write("Welcome to the Student Registration Form!"),
    "Registration Form": registration_form,
    "Assessment Form": assessment,
    "VLE Form": vle,
    "Student Info Form": student_info
}

# Create the sidebar menu
menu_choice = st.sidebar.selectbox("Select a page", list(menu_items.keys()))

# Display the selected page
menu_items[menu_choice]()
