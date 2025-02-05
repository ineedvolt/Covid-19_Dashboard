import sqlite3
import streamlit as st
import user_table
import pw_hashing
import re
from datetime import date


# Sign Up functionality
def signup():
    st.subheader("Create New Account")
    sign_up_date = date.today()
    user_name = st.text_input("Name")
    user_number = st.text_input("Phone number")
    user_email = st.text_input("Email")
    new_password = st.text_input("Password", type='password')
    kept_pwd = pw_hashing.make_hashes(new_password)
    if st.button("Sign Up"):
        user_table.create_usertable()
        if not check_email(user_email):
            st.error("Invalid email")
        else:
            try:
                user_table.add_userdata(sign_up_date, user_name, user_number, user_email, kept_pwd, 0)
                st.success("You have successfully created an account")
                st.info("Go to Login Menu to log in")
            except sqlite3.IntegrityError:
                st.error("Your email has been used before for signup. \nPlease signup with other email")


def check_email(email):
    # citation : referenced from https://stackoverflow.com/questions/8022530/how-to-check-for-valid-email-address
    regex = r'\b[A-Za-z0-9.%+-]+@[A-Za-z0-9.-]+.[A-Z|a-z]{2,}\b'
    if re.match(regex, email):
        return True
    return False
