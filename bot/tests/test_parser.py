import bot.parser as script
from constants import DATA


class TestParser:

    def setup_method(self):
        self.text = "Salut GrandPy! Est-ce que tu connais l'adresse " \
                    "d'OpenClassrooms Paris?"
        self.parser = script.Parser(DATA)

    def test_string_cleanup(self):
        cleaned_string = self.parser.string_cleanup(self.text)
        assert cleaned_string == "salut grandpy  est ce que tu connais l " \
                                 "adresse d openclassrooms paris"
