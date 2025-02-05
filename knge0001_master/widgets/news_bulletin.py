import streamlit as st
from api.news import NewsData


def display_news(num_of_news :int):
    news = NewsData()
    header_container = st.container()
    images = news.getByKey("urlToImage")
    titles = news.getByKey("title")
    urls = news.getByKey("url")
    with header_container:
        st.header("Latest News")
        # Print all images and titles
        j = 0
        print(images)
        for i in range(len(images)):
            if images[j] is not None and j < num_of_news:
                st.image(images[j], width = 300)
                st.markdown(
                    """<a href=""" + urls[j] + ">"+ titles[j] +"</a>""", unsafe_allow_html=True,
                )
            j += 1