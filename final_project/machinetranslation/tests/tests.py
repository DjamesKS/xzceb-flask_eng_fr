import unittest

from translator import english_to_french, french_to_english

class TestFrenchToEnglish(unittest.TestCase):
    def test(self):
        self.assertEqual(french_to_english(None), None)
        self.assertEqual(french_to_english(''), '')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

class TestEnglishToFrench(unittest.TestCase):
    def test(self):
        self.assertEqual(english_to_french(None), None)
        self.assertEqual(english_to_french(''), '')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

unittest.main()
