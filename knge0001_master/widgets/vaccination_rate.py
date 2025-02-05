import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from api.data_retrieval import DataRetrieval


# number of people vaccinated per day in certain country widget
def make_vaccinated_per_day_chart(location: str, data: DataRetrieval) -> None:

    df = data.new_vaccinations(location)
    df['date'] = pd.to_datetime(df['date'])  # converting the date column to datetime

    # converting to line graph
    line_chart = plt.figure()
    x = df['date']  # the x-axis
    y = df['new_vaccinations_smoothed']  # the y-axis
    plt.plot(x, y)

    stats_container = st.container()

    with stats_container:
        st.header(f"Vaccinated per day in {location}")

        st.plotly_chart(line_chart)


if __name__ == "__main__":
    df = DataRetrieval.new_vaccinations(DataRetrieval(), 'Afghanistan')
    print(df)
    print(df['date'])
    print(type(df['date'][0]))