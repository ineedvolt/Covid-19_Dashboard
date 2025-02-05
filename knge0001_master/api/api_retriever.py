import requests 


class APIRetriever:
    def __init__(self, base, endpoint, APIKey):
        """
        initialize your API using this constructor.
        base: the base website example: "https://newsapi.org/"
        endpoint: the data's endpoint example: "v2/top-headlines?q=covid"
        APIKey: The key that the API provided to you
        """
        self.base = base
        self.endpoint = endpoint
        self.key = APIKey
        self.url = base + endpoint + "&apiKey=" + APIKey
        self.request = requests.get(self.url).json()
    
    def showKeys(self):
        """
        Displays all the keys of the retrieved data
        """
        return self.request.keys()

    def getDataByKey(self, key):
        """
        Get data by certain key
        """
        return self.request[key]