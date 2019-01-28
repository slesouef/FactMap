"""Parser test Module"""
import bot.myparser as script


class TestParser:
    """Test the parser behaviour"""

    @classmethod
    def setup_class(cls):
        """Setup test class with test text and load parser"""
        cls.text = "Salut GrandPy! Est-ce que tu connais l'adresse " \
                   "d'OpenClassrooms Paris?"
        cls.words = ["salut", "grandpy", "est", "ce", "que",
                     "tu", "connais", "l", "adresse", "d",
                     "openclassrooms", "paris"]
        cls.parser = script.Parser()

    def test_list_creation(self):
        """test list creation method

        Return:
            list of words from text
        """
        word_list = self.parser.list_creation(self.text)
        assert word_list == self.words

    def test_parse_list(self):
        """test parse list method

        Return:
            relevant words from word list
        """
        results = self.parser.parse_list(self.words)
        assert results == ["openclassrooms", "paris"]

    def test_parse(self):
        """test parse method

        Return:
            relevant words from text
        """
        results = self.parser.parse(self.text)
        assert results == ["openclassrooms", "paris"]
