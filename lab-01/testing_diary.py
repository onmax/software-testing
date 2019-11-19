
import bibtex
import unittest


class TestAuthorExtract(unittest.TestCase):
    """Functions for testing the extraction of author names.
    Note that the rules for extracting bibtex author names is actually
    quite complicated. As these test cases illustrate. I haven't
    implemented all the cases."""

    def setUp(self):

        self.simpleauthor1 = "Smith"
        self.simpleauthor2 = "Jones"
        self.author1 = "John Smith"
        self.author2 = "Bob Jones"
        self.author3 = "Justin Kenneth Pearson"
        self.surnamefirst1 = "Pearson, Justin Kenneth"
        self.surnamefirst2 = "Van Hentenryck, Pascal"
        self.multipleauthors1 = "Pearson, Justin and Jones, Bob"

    def testauthor1(self):
        # Test only surnames.
        (Surname, FirstNames) = bibtex.extractauthor(self.simpleauthor1)
        self.assertEqual((Surname, FirstNames), ('Smith', ''))
        (Surname, FirstNames) = bibtex.extractauthor(self.simpleauthor2)
        self.assertEqual((Surname, FirstNames), ('Jones', ''))

    def testauthor2(self):
        # Test simple first name author.
        (Surname, First) = bibtex.extractauthor(self.author1)
        self.assertEqual((Surname, First), ("Smith", "John"))
        (Surname, First) = bibtex.extractauthor(self.author2)
        self.assertEqual((Surname, First), ("Jones", "Bob"))

    def testauthor3(self):
        (Surname, First) = bibtex.extractauthor(self.author3)
        self.assertEqual((Surname, First), ("Pearson", "JustinKenneth"))

    def testsurnamefirst(self):
        (Surname, First) = bibtex.extractauthor(self.surnamefirst1)
        self.assertEqual((Surname, First), ("Pearson", "Justin Kenneth"))
        (Surname, First) = bibtex.extractauthor(self.surnamefirst2)
        self.assertEqual((Surname, First), ("Van Hentenryck", "Pascal"))

    def testmultipleauthors(self):
        Authors = bibtex.extractauthors(self.multipleauthors1)
        self.assertEqual(Authors[0], ('Pearson', 'Justin'))
        self.assertEqual(Authors[1], ('Jones', 'Bob'))


if __name__ == '__main__':
    unittest.main()
