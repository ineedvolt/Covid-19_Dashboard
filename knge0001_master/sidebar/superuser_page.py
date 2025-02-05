from user_table import view_all_users
from acc_retriever import get_account
import pandas as pd
import streamlit as st
import sqlite3


# SuperUser page Function
def superuser():
    st.header("User Table")
    df = pd.DataFrame(
        view_all_users()
    )
    df.columns = ["Created date", "Name", "Phone number", "Email", "Login frequency"]
    st.table(df)

