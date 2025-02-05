import requests
import pandas as pd

# Data citation:
# Hannah Ritchie, Edouard Mathieu, Lucas Rodés-Guirao, Cameron Appel, Charlie Giattino, Esteban Ortiz-Ospina, Joe Hasell
# Bobbie Macdonald, Diana Beltekian and Max Roser (2020) - "Coronavirus Pandemic (COVID-19)".
# Published online at OurWorldInData.org. Retrieved from: 'https://ourworldindata.org/coronavirus' [Online Resource]


class DataRetrieval:
    def __init__(self):
        url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
        r = requests.get(url)
        url_content = r.content
        csv_file = open('../covid_data.csv', 'wb')
        csv_file.write(url_content)
        csv_file.close()

        # col_list = ['location', 'date', 'people_fully_vaccinated', 'population', 'new_deaths_smoothed',
        #             'new_cases_smoothed', 'new_vaccinations_smoothed', 'new_tests_smoothed']

        self.df = pd.read_csv('../covid_data.csv')

    def get_df_by_location(self, location: str) -> pd.DataFrame:
        """returns a dataframe that only includes columns included in col_list"""
        return self.df[self.df['location'].str.contains(location)]

    def get_countries(self) -> pd.Series:
        """returns the list of unique country values from the data api"""
        return self.df['location'].unique()

    # 1st Widget
    def people_fully_vaccinated(self, location: str) -> pd.DataFrame:
        col_list = ['location', 'date', 'people_fully_vaccinated']
        df = self.get_df_by_location(location)[col_list]
        return df

    # 1st Widget
    def population(self, location):
        col_list = ['location', 'date', 'population']
        df = self.get_df_by_location(location)[col_list]
        return df

    # 2nd Widget
    def new_deaths(self, location):
        col_list = ['location', 'date', 'new_deaths_smoothed']
        df = self.get_df_by_location(location)[col_list]
        return df

    # 3rd Widget
    def new_cases(self, location):
        col_list = ['location', 'date', 'new_cases_smoothed']
        df = self.get_df_by_location(location)[col_list]
        return df

    # 4th Widget
    def new_vaccinations(self, location):
        col_list = ['location', 'date', 'new_vaccinations_smoothed']
        df = self.get_df_by_location(location)[col_list]
        return df

    # 5th Widget
    def new_tests(self, location):
        col_list = ['location', 'date', 'new_tests_smoothed']
        df = self.get_df_by_location(location)[col_list]
        return df


if __name__ == '__main__':
    data = DataRetrieval()
    # print(data.people_fully_vaccinated('Sri Lanka'))
    print(data.people_fully_vaccinated('Malaysia'))
    print(data.get_df_by_location('Sri Lanka'))
    print(data.population('Ireland'))
