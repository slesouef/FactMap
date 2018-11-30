import bot.parser as script
from constants import DATA


class TestParser:

    def setup_method(self):
        self.text = "Salut GrandPy! Est-ce que tu connais l'adresse " \
                    "d'OpenClassrooms Paris?"
        self.parser = script.Parser(DATA)

    def test_list_creation(self):
        self.parser.list_creation(self.text)
        assert self.parser.word_list == ["salut", "grandpy", "est", "ce", "que",
                                  "tu", "connais", "l", "adresse", "d",
                                  "openclassrooms", "paris"]
