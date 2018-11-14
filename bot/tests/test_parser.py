from bot.parser import *


class TestParser:

    def setup_method(self):
        self.text = "Salut GrandPy ! Est-ce que tu connais l'adresse " \
                    "d'OpenClassrooms ?"

    def test_string_cleanup(self):
        word_list = string_cleanup(self.text)
        assert word_list == ["Salut", "GrandPy", "connais", "adresse",
                             "OpenClassrooms"]
