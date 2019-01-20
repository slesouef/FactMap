"""Parser test Module"""
import bot.myparser as script
from constants import DATA


class TestParser:
    """Test the parser behaviour"""

    @classmethod
    def setup_class(cls):
        """Setup test class with test text and load parser"""
        cls.text = "Salut GrandPy! Est-ce que tu connais l'adresse " \
                   "d'OpenClassrooms Paris?"
        cls.parser = script.Parser(DATA)

    def test_list_creation(self):
        """test list creation method

        Return:
            list of words from test text
        """
        self.parser.list_creation(self.text)
        assert self.parser.word_list == ["salut", "grandpy", "est", "ce", "que",
                                         "tu", "connais", "l", "adresse", "d",
                                         "openclassrooms", "paris"]

    def test_parse_list(self):
        """test parse list method

        Return:
            relevant words from test text
        """
        results = self.parser.parse_list()
        assert results == ["openclassrooms", "paris"]
