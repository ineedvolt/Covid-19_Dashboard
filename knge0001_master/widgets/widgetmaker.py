"""This module contains the WidgetMaker class that handles calling all the chart drawing methods"""

from api.data_retrieval import DataRetrieval
from widgets.deaths import make_deaths_per_day_chart
from widgets.new_cases import make_cases_per_day_chart
from widgets.new_tests import make_new_tests_per_day_chart
from widgets.news_bulletin import display_news
from widgets.total_vaccinated import make_total_vaccinated_chart
from widgets.vaccination_rate import make_vaccinated_per_day_chart


class WidgetMaker:
    def __init__(self, location: str, data: DataRetrieval) -> None:
        """instantiates WidgetMaker instance with location as an instance variable"""
        if len(location) <= 0:
            raise ValueError("Error in reading country selection")

        self.location = location
        self.df = data

    def display_charts(self) -> None:
        """displays all widgets in the widget package to the dashboard"""
        make_total_vaccinated_chart(self.location, self.df)
        make_cases_per_day_chart(self.location, self.df)
        make_vaccinated_per_day_chart(self.location, self.df)
        make_new_tests_per_day_chart(self.location, self.df)
        make_deaths_per_day_chart(self.location, self.df)
        display_news(4)
