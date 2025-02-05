import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from api.data_retrieval import DataRetrieval


def make_cases_per_day_chart(location: str, data: DataRetrieval) -> None:
    df = data.new_cases(location)
    df['date'] = pd.to_datetime(df['date'])  # converting the date column to datetime

    # converting to line chart
    line_chart = plt.figure()
    x = df['date']  # x-axis
    y = df['new_cases_smoothed']  # y-axis
    plt.plot(x, y)  # plot the graph! the graph is stored in wherever you assigned plt.figure() to

    stats_container = st.container()  # container of this widget

    with stats_container:
        st.header(f"New Cases per day in {location}")

        st.plotly_chart(line_chart)


if __name__ == "__main__":
    df = DataRetrieval.new_cases(DataRetrieval(), 'Afghanistan')
    print(df)
    print(df['date'])
    print(type(df['date'][0]))

