#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""Parser module

Takes the content of the user entry from the ajax POST and returns a short
list of relevant terms
"""
import json
from string import punctuation
from constants import DATA


class Parser:
    """Extract a list of words and compare it to stop-word file content

    Args:
        file: file containing the list of stop words
    """

    def __init__(self):
        self.data_file = open(DATA)
        self.stop_words = json.load(self.data_file)

    def parse(self, request):
        """call parse methods

        Args:
            request: POST body content
        """
        words = self.list_creation(request)
        results = self.parse_list(words)
        return results

    def list_creation(self, request):
        """create word list from provided string

        Args:
            request: POST body content
        """

        no_caps = request.lower()
        no_numbers = "".join([char for char in no_caps if not char.isdigit()])
        no_apostrophe = no_numbers.replace("'", " ")
        # remove punctuation marks by replacing it with space after comparing
        # each string character to string.punctuation elements
        no_punctuation = no_apostrophe.translate(str.maketrans({a: " " for a in
                                                                punctuation}))
        clean_string = no_punctuation.strip()
        return clean_string.split()

    def parse_list(self, words):
        """Remove elements from word list if found in stop word file

        Args:
            words: list of words to be compared to stop words
        """
        results = [w for w in words if w not in self.stop_words]
        return results
