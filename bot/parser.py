#! usr/bin/env python3
# -*- coding:utf-8 -*-
import json
from string import punctuation


class Parser:

    def __init__(self, file):
        self.data_file = open(file)
        self.stop_words = json.load(self.data_file)

    def string_cleanup(self, request):
        no_caps = request.lower()
        no_apostrophe = no_caps.replace("'", " ")
        no_punctuation = no_apostrophe.translate(str.maketrans({a: " " for a in
                                                 punctuation}))
        clean_string = no_punctuation.strip()
        return clean_string
