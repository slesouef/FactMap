#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""Parser module

Takes the content of the user entry from the ajax POST and returns a short
list of relevant terms
"""
import json
from string import punctuation


class Parser:
    """Extract a list of words and compare it to stop-word file content

    Args:
        file: file containing the list of stop words
    """

    def __init__(self, file):
        self.data_file = open(file)
        self.stop_words = json.load(self.data_file)
        self.word_list = []

    def list_creation(self, request):
        """create word list from provided string

        Args:
            request: POST body content
        """
        no_caps = request.lower()
        no_apostrophe = no_caps.replace("'", " ")
        # remove punctuation marks by replacing it with space after comparing
        # each string character to string.punctuation elements
        no_punctuation = no_apostrophe.translate(str.maketrans({a: " " for a in
                                                                punctuation}))
        clean_string = no_punctuation.strip()
        self.word_list = clean_string.split()

    def parse_list(self):
        """Remove elements from word list if found in stop word file"""
        results = [w for w in self.word_list if w not in self.stop_words]
        return results
