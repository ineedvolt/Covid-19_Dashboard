import math

import streamlit as st
import matplotlib.pyplot as plt
from api.data_retrieval import DataRetrieval


# total_vaccination widget
def make_total_vaccinated_chart(location: str, data: DataRetrieval) -> None:
    df = data.people_fully_vaccinated(location)
    index = len(df) - 1

    # retrieving the latest data for number of people vaccinated
    vaccinated = df.iloc[len(df)-1]['people_fully_vaccinated']

    # if latest is NaN, check if there's available data from earlier
    while math.isnan(vaccinated) and index >= 0:
        vaccinated = df.iloc[index]['people_fully_vaccinated']
        index -= 1

    # if all is NaN, then no data
    if math.isnan(vaccinated):
        st.header(f"Total vaccinated in {location}")
        st.subheader("There is no data available for this country")
    else:
        date = df.iloc[index]['date']
        df = data.population(location)
        population = df.iloc[index]['population']  # retrieving the latest data for the population
        not_vaccinated = population - vaccinated

        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = 'Vaccinated', 'Not Vaccinated'
        sizes = [vaccinated, not_vaccinated]
        explode = (0.1, 0)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        stats_container = st.container()
        with stats_container:
            st.header(f"Total vaccinated in {location} by {date}")
            st.write(f"{int(vaccinated):,} people vaccinated out of {int(population):,} total people")
            st.pyplot(fig1)


if __name__ == '__main__':
    data = DataRetrieval()
    make_total_vaccinated_chart("Malaysia", data)
