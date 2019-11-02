import unittest
import sorter
from entry import Entry

class TestLoadEntries(unittest.TestCase):
    def test_entries_equal_method_with_same_order(self):
        expected = [
            Entry("key_a", "value_a", "utf8", "allow"),
            Entry("key_b", "value_b", "utf8", "allow"),
            Entry("key_c", "value_c", "utf8", "allow")
        ]

        actual = [
            Entry("key_a", "value_a", "utf8", "allow"),
            Entry("key_b", "value_b", "utf8", "allow"),
            Entry("key_c", "value_c", "utf8", "allow")
        ]

        self.__entries_equal(actual, expected)


    def test_entries_equal_method_with_different_order(self):
        expected = [
            Entry("key_a", "value_a", "utf8", "allow"),
            Entry("key_b", "value_b", "utf8", "allow"),
            Entry("key_c", "value_c", "utf8", "allow")
        ]

        actual = [
            Entry("key_b", "value_b", "utf8", "allow"),
            Entry("key_c", "value_c", "utf8", "allow"),
            Entry("key_a", "value_a", "utf8", "allow")
        ]

        self.__entries_equal(actual, expected)

    
    def test_entries_equal_method_with_empty_lists(self):
        expected = []
        actual = []

        self.__entries_equal(actual, expected)


    def test_entries_equal_method_with_different_keys(self):
        expected = [
            Entry("key_a", "value_a", "utf8", "allow"),
            Entry("key_b", "value_b", "utf8", "allow"),
            Entry("key_c", "value_c", "utf8", "allow")
        ]

        actual = [
            Entry("key_b", "value_b", "utf8", "allow"),
            Entry("key_d", "value_c", "utf8", "allow"),
            Entry("key_a", "value_a", "utf8", "allow")
        ]

        try:
            self.__entries_equal(actual, expected)
        except AssertionError:
            return
        self.fail()


    def test_entries_equal_method_with_different_values(self):
        expected = [
            Entry("key_a", "value_a", "utf8", "allow"),
            Entry("key_b", "value_b", "utf8", "allow"),
            Entry("key_c", "value_c", "utf8", "allow")
        ]

        actual = [
            Entry("key_b", "value_b", "utf8", "allow"),
            Entry("key_c", "value_d", "utf8", "allow"),
            Entry("key_a", "value_a", "utf8", "allow")
        ]

        try:
            self.__entries_equal(actual, expected)
        except AssertionError:
            return
        self.fail()


    def test_entries_equal_method_with_different_length(self):
        expected = [
            Entry("key_a", "value_a", "utf8", "allow"),
            Entry("key_b", "value_b", "utf8", "allow"),
            Entry("key_c", "value_c", "utf8", "allow")
        ]

        actual = [
            Entry("key_b", "value_b", "utf8", "allow"),
            Entry("key_a", "value_a", "utf8", "allow")
        ]

        try:
            self.__entries_equal(actual, expected)
        except AssertionError:
            return
        self.fail()


    def test_valid_entries(self):
        entries = [
            Entry("ala ma kota", "", "utf8", "allow"),
            Entry("kota i psa", "", "utf8", "allow"),
            Entry("kanapki i pyszności", "", "utf8", "allow"),
            Entry("ala ma", "", "utf8", "allow"),
            Entry("ma kota", "", "utf8", "allow"),
            Entry("kota i", "", "utf8", "allow"),
            Entry("psa", "", "utf8", "allow"),
            Entry("pyszności", "", "utf8", "allow"),
            Entry("ma", "", "utf8", "allow"),
            Entry("ma kota", "", "utf8", "allow"),
            Entry("kota", "", "utf8", "allow"),
            Entry("pysz", "", "utf8", "allow"),
            Entry("ści", "", "utf8", "allow")
        ]

        expected_sort = [
            [
                Entry("ala ma kota", "", "utf8", "allow"),
                Entry("kota i psa", "", "utf8", "allow"),
                Entry("kanapki i pyszności", "", "utf8", "allow")
            ],
            [
                Entry("ala ma", "", "utf8", "allow"),
                Entry("ma kota", "", "utf8", "allow"),
                Entry("psa", "", "utf8", "allow"),
                Entry("kota i", "", "utf8", "allow"),
                Entry("ma kota", "", "utf8", "allow"),
                Entry("pyszności", "", "utf8", "allow")
            ],
            [
                Entry("ma", "", "utf8", "allow"),
                Entry("kota", "", "utf8", "allow"),
                Entry("pysz", "", "utf8", "allow"),
                Entry("ści", "", "utf8", "allow")
            ]
        ]

        self.__test_sorted(expected_sort, entries)


    def test_empty_list(self):
        entries = []
        expected_sort = []

        self.__test_sorted(expected_sort, entries)


    def test_same_word(self):
        entries = [
            Entry("lew", "", "utf8", "allow"),
            Entry("lew", "", "utf8", "allow"),
            Entry("lew", "", "utf8", "allow")
        ]

        expected_sort = [
            [
                Entry("lew", "", "utf8", "allow"),
                Entry("lew", "", "utf8", "allow"),
                Entry("lew", "", "utf8", "allow")
            ]
        ]

        self.__test_sorted(expected_sort, entries)


    def test_overlaping_words(self):
        entries = [
            Entry("this moment. ", "", "utf8", "allow"),
            Entry("I am wat", "", "utf8", "allow"),
            Entry("ment. Sad movie.", "", "utf8", "allow"),
            Entry("green mile at this", "", "utf8", "allow"),
            Entry("m watching", "", "utf8", "allow"),
            Entry("hing gree", "", "utf8", "allow")
        ]

        expected_sort = [
            [
                Entry("I am wat", "", "utf8", "allow"),
                Entry("m watching", "", "utf8", "allow"),
                Entry("hing gree", "", "utf8", "allow"),
                Entry("green mile at this", "", "utf8", "allow"),
                Entry("this moment. ", "", "utf8", "allow"),
                Entry("ment. Sad movie.", "", "utf8", "allow")
            ]
        ]

        self.__test_sorted(expected_sort, entries)


    def test_single_word_in_single_level(self):
        entries = [
            Entry("so", "", "utf8", "allow"),
            Entry("This is just some sentence", "", "utf8", "allow"),
            Entry("", "", "utf8", "allow"),
            Entry("some", "", "utf8", "allow"),
            Entry("is just some", "", "utf8", "allow"),
            Entry("just some", "", "utf8", "allow")
        ]

        expected_sort = [
            [
                Entry("This is just some sentence", "", "utf8", "allow")
            ],
            [
                Entry("is just some", "", "utf8", "allow")
            ],
            [
                Entry("just some", "", "utf8", "allow")
            ],
            [
                Entry("some", "", "utf8", "allow")
            ],
            [
                Entry("so", "", "utf8", "allow")
            ],
            [
                Entry("", "", "utf8", "allow")
            ]
        ]

        self.__test_sorted(expected_sort, entries)


    def __test_sorted(self, expected_sort, entries):
        actual_sort = sorter.sort(entries)
        self.assertEqual(len(actual_sort), len(expected_sort))
        for i in range(len(actual_sort)):
            self.__entries_equal(expected_sort[i], actual_sort[i])


    def __entries_equal(self, expected_entries, actual_entries):
        self.assertEqual(len(expected_entries), len(actual_entries))
        for exp_entry in iter(expected_entries):
            for act_entry in iter(actual_entries):
                if exp_entry.key == act_entry.key and exp_entry.value == act_entry.value:
                    break
            else:
                self.fail()
