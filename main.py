
from google.protobuf import message
import streamlit as st

st.title("Streamlit Form Demo") 
st.subheader("Enter details below")


with st.form("form1", clear_on_submit=True): 
	name = st.text_input("Enter full name") 
	email = st.text_input("Enter email") 
	message = st.text_area("Message") 
	st.write(age)
	submit = st.form_submit_button("Submit this form")