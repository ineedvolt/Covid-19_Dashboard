import streamlit as st
import pandas as pd


class CountryMenu:
    def __init__(self, countries: pd.Series):
        """pass in list of countries as parameter and it will show in the drop down menu"""
        self.choice = st.sidebar.selectbox("Select Country", countries)

    def get_country_selection(self) -> str:
        """returns whatever the user selected in the country drop down menu as str"""
        return self.choice
