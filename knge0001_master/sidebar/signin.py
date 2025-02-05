import streamlit as st
import user_table
import pw_hashing
from widgets.new_cases import make_cases_per_day_chart
from widgets.new_tests import make_new_tests_per_day_chart
from widgets.news_bulletin import display_news
from sidebar.country_menu import CountryMenu
from api.data_retrieval import DataRetrieval
from widgets.deaths import make_deaths_per_day_chart
from widgets.total_vaccinated import make_total_vaccinated_chart
from widgets.vaccination_rate import make_vaccinated_per_day_chart
from user_check import check_superuser

flag = False
is_superuser = False


# Sign In functionality
def signin():
    st.subheader("Login Section")
    email = st.sidebar.text_input("Email")
    password = st.sidebar.text_input("Password", type='password')
    if st.sidebar.button("Login"):
        user_table.create_usertable()
        hashed_pswd = pw_hashing.make_hashes(password)
        result = user_table.login_user(email, pw_hashing.check_hashes(password, hashed_pswd))
        if result:
            if check_superuser(email):
                global is_superuser
                is_superuser = True
            else:
                is_superuser = False
            st.success("Logged in as {}".format(email))
            user_table.update_login_count(email) #update login count of user
            data = DataRetrieval()
            countries = data.get_countries()  # retrieves pd.Series of countries
            country_choice = CountryMenu(countries)  # country_choice stores user selected country
            make_total_vaccinated_chart(country_choice.get_country_selection(), data)  # number of vaccinated people
            make_deaths_per_day_chart(country_choice.get_country_selection(), data)  # number of death cases chart
            make_cases_per_day_chart(country_choice.get_country_selection(), data)
            make_new_tests_per_day_chart(country_choice.get_country_selection(),data)  # number of new covid tests chart
            make_vaccinated_per_day_chart(country_choice.get_country_selection(), data)
            display_news(4)
            global flag
            flag = True
            return flag
        else:
            st.warning("Incorrect Email/Password")
