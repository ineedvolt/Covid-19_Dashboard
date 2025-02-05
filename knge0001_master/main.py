# main file to run with streamlit
import streamlit as st
from sidebar import signin, signup, superuser_page
from widgets.widgetmaker import WidgetMaker
from sidebar.country_menu import CountryMenu
from api.data_retrieval import DataRetrieval



def main():
    st.title("Covid-19 Dashboard")

    # menu = ["Home", "Login", "Sign Up"]
    menu = ["Home", "Login", "Sign Up", "Super User", "Logout"]
    choice = st.sidebar.selectbox("Menu", menu)

    # Home menu
    if choice == "Home":
        # st.subheader("Covid-19 Dashboard")
        st.markdown("This dashboard provides Covid-19 data and statistics from around the world")
        st.markdown("Please sign up for an account or log in with an existing account to view the dashboard")
        st.markdown("You can do so with the sidebar menu on the left")

    # Login Menu
    elif choice == "Login":
        if not signin.flag:
            signin.signin()

        elif signin.flag:
            data = DataRetrieval()
            countries = data.get_countries()  # retrieves pd.Series of countries
            country_choice = CountryMenu(countries)  # country_choice stores user selected country
            st.markdown("Data from Our World in Data. https://ourworldindata.org/")
            selected_country = country_choice.get_country_selection()
            widgets = WidgetMaker(selected_country, data)
            widgets.display_charts()

    # Sign up menu
    elif choice == "Sign Up":
        signup.signup()

    # logout will make the signin flag boolean to false , and ask user to signup or login again
    elif choice== "Logout" :
        signin.flag=False
        st.success("You have logged out of the page")
        st.markdown("To access the dashboard again,")
        st.markdown("please sign up for an account or log in with an existing account to view the dashboard")
        st.markdown("You can do so with the sidebar menu on the left")

    # Super user menu
    elif choice == "Super User":
        if signin.is_superuser:
            superuser_page.superuser()
        else:
            st.warning("You are not authorised to access this page since you are not admin")


if __name__ == '__main__':
    main()
