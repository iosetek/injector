import os
import unittest
from translator import Translator

class TestTranslations(unittest.TestCase):
    def test_simple_test(self):
        translator = Translator("tests/test_data/translate/file_to_translate",
            "tests/test_data/translate/actual_file",
            "tests/test_data/translate/entries.json")

        translator.translate("tests/test_data/translate/actual_file")
        os.remove("tests/test_data/translate/actual_file")
    # def test_longer_first(self):
    #     shorter_entry = TranslationEntry("phrase", "A")
    #     longer_entry = TranslationEntry("longer phrase", "B")

    #     entries = [shorter_entry, longer_entry]

    #     to_translate = "longer phrase phrase"
    #     expected = "B A"

    
    # def test_shorter_first(self):
    #     shorter_entry = TranslationEntry("phrase", "A")
    #     longer_entry = TranslationEntry("longer phrase", "B")

    #     to_translate = "phrase longer phrase"
    #     expected = "A B"


    # def test_missing_shorter_entry(self):
    #     shorter_entry = TranslationEntry("phrase", "A")
    #     longer_entry = TranslationEntry("longer phrase", "B")

    #     to_translate = "longer phrase"
    #     expected_translation = "B"
    #     expected_missing = ["phrase"]


    # def test_two_entries_inside_third_entry(self):
    #     long_entry = TranslationEntry("quite long testing sentence", "A")
    #     first_short_entry = TranslationEntry("long", "B")
    #     second_short_entry = TranslationEntry("testing", "C")

    #     to_translate = "this is quite long testing sentence"
    #     expected_translation = "this is A"
    #     expected_missing = ["long", "testing"]


    # def test_two_collisions(self):
    #     first_entry = TranslationEntry("test", "A")
    #     second_entry = TranslationEntry("ting", "B")

    #     to_translate = "testing"

    #     # the order is not important
    #     expected_collisions = ["test", "ting"]


    # def test_three_collisions(self):
    #     first_entry = TranslationEntry("test", "A")
    #     second_entry = TranslationEntry("sti", "B")
    #     third_entry = TranslationEntry("ting", "C")

    #     to_translate = "testing"

    #     # the order is not important
    #     expected_collisions = ["test", "sti", "ting"]