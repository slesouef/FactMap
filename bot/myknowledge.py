"""Media API call module"""
from constants import SEARCH_URL

class Wiki:
    """Call WikiMedia API and retrieve page extract from response"""

    def __init__(self):
        self.search_url = ""

    def create_search_url(self, parsed_address):
        """Format search URL from parser results

        Args:
            parsed_address: result of parser module on Maps address
        """
        parameters = "%20".join(parsed_address)
        self.search_url = "{}srsearch={}".format(SEARCH_URL, parameters)


# create extract url
# https://fr.wikipedia.org/w/api.php?action=query&format=json&prop=extracts \
# &exintro=&utf8=1&explaintext=1&pageids=5653202
