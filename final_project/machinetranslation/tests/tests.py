import unittest
from translator import frenchToEnglish, englishToFrench

class TessTranslatorAPI(unittest.TestCase):
    
    def test_translate_to_english_to_french(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")

    def test_error_for_null_input_translate_to_english_to_french(self):
        self.assertEqual(englishToFrench(""), "Null value")

    def test_translate_to_english_to_french_always_correct(self):
        self.assertNotEqual(englishToFrench("Hello"), "No")

    def test_translate_french_to_english(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")

    def test_error_for_null_input_translate_english_to_french(self):
        self.assertEqual(frenchToEnglish(""), "Null value")

    def test_translate_english_to_french_(self):
        self.assertNotEqual(frenchToEnglish("Bonsoir"), "Banane")


if __name__ == "__main__":
    unittest.main()