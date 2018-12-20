import bot.myparser as script
from constants import DATA


class TestParser:

    def setup_class(cls):
        cls.text = "Salut GrandPy! Est-ce que tu connais l'adresse " \
                   "d'OpenClassrooms Paris?"
        cls.parser = script.Parser(DATA)

    def test_list_creation(self):
        self.parser.list_creation(self.text)
        assert self.parser.word_list == ["salut", "grandpy", "est", "ce", "que",
                                         "tu", "connais", "l", "adresse", "d",
                                         "openclassrooms", "paris"]

    def test_parse_list(self):
        results = self.parser.parse_list()
        assert results == ["openclassrooms", "paris"]
