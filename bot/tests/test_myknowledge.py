"""Media API call testing"""
import bot.myknowledge as script


# create stub
    # search api stub
    # {
    #     "query": {
    #         "search": [
    #             {
    #                 "pageid": 5653202,
    #             }
    #         ]
    #     }
    # }

    # extract api stub
    # {
    #     "query":{
    #         "pages":{
    #             "5653202":{
    #                 "extract":"La cité Paradis est une voie publique située
#                              \ dans le 10e arrondissement de Paris."
    #             }
    #         }
    #     }
    # }


class TestWiki:
    """Test API call behaviour"""

    @classmethod
    def setup_class(cls):
        """Setup test class with test paser results and load API caller"""
        cls.wiki = script.Wiki()
        cls.parameter = ["cité", "paradis", "paris", "france"]

    def test_create_search_url(self):
        """Test search url construction"""
        self.wiki.create_search_url(self.parameter)
        for item in self.parameter:
            assert item in self.wiki.search_url


# test call against media wiki search API

# test extract url construction
    # get pageid from search call repsonse
    # create extract url
    # https://fr.wikipedia.org/w/api.php?action=query&format=json&prop=extracts \
    #                                    &exintro=&utf8=1&explaintext=1 \
    #                                    &pageids=5653202

# test response to client
    # test extract response from API
    # test reponse sent to client
