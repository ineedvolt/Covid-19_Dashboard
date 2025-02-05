import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from api.data_retrieval import DataRetrieval


# display line graph for number of deaths in a chosen country
def make_deaths_per_day_chart(location: str, data: DataRetrieval) -> None:
    df = data.get_df_by_location(location)
    df['date'] = pd.to_datetime(df['date'])  # converting the date column to datetime

    # converting to line chart
    line_chart = plt.figure()
    x = df['date']  # x-axis
    y = df['new_deaths_smoothed']  # y-axis
    plt.plot(x, y)

    stats_container = st.container()

    with stats_container:
        st.header(f"New Death per day in {location}")

        st.plotly_chart(line_chart)
        total_deaths = df.iloc[-1]['total_deaths']
        st.write(f"Total Deaths = {int(total_deaths)}")


if __name__ == "__main__":
    df = DataRetrieval.new_deaths(DataRetrieval(), 'Afghanistan')
    print(df)
    print(df['date'])
    print(type(df['date'][0]))
