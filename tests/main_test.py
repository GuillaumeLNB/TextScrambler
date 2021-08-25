#!/bin/python3
import os
import string
import sys
import unittest

sys.path.insert(0, os.path.join("..", "src"))

import dictionnaries
import main


class TestScrambler(unittest.TestCase):

    alphabet = string.ascii_lowercase

    def setUp(self):
        self.scrambler = main.Scrambler()

    def tearDown(self):
        pass

    def test_length_latin_dict(self):
        self.assertTrue(len(dictionnaries.dict_latin) > 10)

    def test_latin_chars(self):
        for char in self.alphabet + self.alphabet.upper():
            if char not in dictionnaries.dict_latin:
                continue
            for different_letter in dictionnaries.dict_latin[char]:
                self.assertNotEqual(char, different_letter)

    def test_wrong_level(self):
        for wrong_level in [0, 5, 10, str]:
            self.assertRaises(
                ValueError, self.scrambler.scramble, self.alphabet, wrong_level
            )

    def test_scramble(self):
        for level in [1, 2, 3, 4]:
            new_text = self.scrambler.scramble(self.alphabet, level)
            self.assertNotEqual(new_text, self.alphabet)

    def test_generate(self):
        n_times = 1000
        for level in [1, 2, 3, 4]:
            res = self.scrambler.generate(self.alphabet, n=n_times, level=level)
            self.assertEqual(len(set(res)), len(res))


unittest.main()
