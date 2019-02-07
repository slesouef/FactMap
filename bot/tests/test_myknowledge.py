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
    #                 "extract":"La cité Paradis est une voie publique située dans le 10e arrondissement de Paris."
    #             }
    #         }
    #     }
    # }


# test search url construction
    # get search parameters from parser (possible to mutualize with gmaps??)
    # create search url
    # https://fr.wikipedia.org/w/api.php?action=query&format=json&list=search \
    # &utf8=1&srsearch=cit%C3%A9%20paradis%20paris%20france

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
