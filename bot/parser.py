#! usr/bin/env python3
# -*- coding:utf-8 -*-
import json
from string import punctuation


class Parser:

    def __init__(self, file):
        self.data_file = open(file)
        self.stop_words = json.load(self.data_file)
        self.word_list = []

    def list_creation(self, request):
        no_caps = request.lower()
        no_apostrophe = no_caps.replace("'", " ")
        no_punctuation = no_apostrophe.translate(str.maketrans({a: " " for a in
                                                 punctuation}))
        clean_string = no_punctuation.strip()
        self.word_list = clean_string.split()
