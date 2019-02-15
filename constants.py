#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""contains all application parameters"""

# Stop word file
DATA = "bot/data/stop-fr.json"

# 404 error url
URL_404 = "https://google.com/404"

# google maps geocoding parameters
URL = "https://maps.googleapis.com/maps/api/geocode/json?language=fr&"

# WikiMedia search API url
SEARCH_URL = "https://fr.wikipedia.org/w/api.php?action=query&format=json&" \
             "list=search&utf8=1"

# WikiMedia extract API url
EXTRACT_URL = "https://fr.wikipedia.org/w/api.php?action=query&format=json" \
              "&prop=extracts&exintro=&utf8=1&explaintext=1"

# Wikipedia base url
WIKI_URL = "https://fr.wikipedia.org/wiki/"
