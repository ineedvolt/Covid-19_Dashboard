from api.api_retriever import APIRetriever
import requests

class NewsData:
    def __init__(self):
        self.data = APIRetriever("https://newsapi.org/","v2/top-headlines?country=my&q=covid", "84e3e2af789e4c618f7629f4c9ba9750")
        self.articles = self.data.getDataByKey("articles")

    def getByKey(self, key :str, num :int = None):
        if num is None:
            num = len(self.articles)
        dataList = []
        for i in range (num):
            dataList.append(self.articles[i][key])
        return dataList

