#!/usr/bin/env python3
# usage : python3 transform.py ARGS file

import argparse
import html
import requests
import sys
from random import shuffle, choice
from typing import List

from dictionnaries import invisible_chars, dict_latin


def _dummy_output(text, file_name=None):
    if file_name:
        with open(file_name, "w", encoding="UTF-8") as f:
            f.write(text)
        return
    print(text)


class Scrambler:
    def __init__(
        self,
        confusables_file="../txt_files/confusablesSummary.txt",
    ):
        # The confusables can be found at:
        # https://www.unicode.org/Public/security/13.0.0/confusables.txt
        self.confusables_file = confusables_file
        self.invisible_chars = invisible_chars
        self.dict_latin = dict_latin
        self.parse_unicode_file()

    def __str__(self):
        return str(self.scramble("<__main__.Scrambler object>", level=4))

    __repr__ = __str__

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type:
            print(f"exc_type: {exc_type}", file=sys.stderr)
            print(f"exc_value: {exc_value}", file=sys.stderr)
            print(f"exc_traceback: {exc_traceback}", file=sys.stderr)

    def parse_unicode_file(self) -> dict:
        """return a dict of the unicode confusable given
        the self.confusables_file"""
        self.unicode_dict = {}
        file = open(self.confusables_file)
        ls_lines_confusable = []
        for _ in range(12):
            file.readline()
        for line in file:
            if line.startswith("#"):
                ls_lines_confusable.append(line[:-1])  # not taking the \n
        file.close()
        ls_lines_confusable = ls_lines_confusable[
            :-1
        ]  # not taking the last line (total)
        for line in ls_lines_confusable:
            _, char, *ls_chars = line.split("\t")
            if len(char) > 1:
                continue
            self.unicode_dict[char] = ls_chars

    def scramble(self, text: str, level: int = 1) -> str:
        """return the text scrambled
        eg: teststring-> 𝘁ｅ𝐬𝝉ꜱ𝐭𝐫𝖎𝝿𝐠

        :param text: the text to scramble
        :type text: str
        :param level:, defaults to 1
        :type level: int, optional
        level:
        1: inser non printable characters within the text
        2: replace some latin letters to their Greek or Cyrilic
                equivalent
        3: inser non printable characters and change the
                some latin letters to their Greek or Cyrilic
                equivalent
        4: insert non printable chraracters
             change all possible letter to a randomly picked
             unicode letter equivalent

        :return: the scrambled string
        :rtype: str
        """
        new_text = ""
        if level == 1:
            for char in text:
                new_text += char + choice(self.invisible_chars)
        elif level == 2:
            for char in text:
                new_text += choice(self.dict_latin.get(char, []) + [char])
            new_text += " "
        elif level == 3:
            for char in text:
                new_text += choice(self.dict_latin.get(char, []) + [char]) + choice(
                    self.invisible_chars
                )
        elif level == 4:
            for char in text:
                new_text += choice(self.unicode_dict.get(char, []) + [char]) + choice(
                    self.invisible_chars
                )
        else:
            raise ValueError(f"level '{level}' not implemented")
        return new_text[:-1]

    def generate(self, text: str, n: int = 1000, level: int = 3) -> List[str]:
        """return a list containing n versions of the text jammed

        :param text: the text to be scrambled
        :type text: str
        :param n: the number of time the text should be scrambled, defaults to 1000
        :type n: int, optional
        :param level: the level of the scrambling, defaults to 3
        :type level: int, optional
        :return: a list of scrambled texts, all differents
        :rtype: List[str]
        """
        ls_new_text = []
        num_generated = 0
        while True:
            new_text = self.scramble(text, level=level)
            if new_text not in ls_new_text:
                ls_new_text.append(new_text)
                num_generated += 1
            if num_generated == n:
                break
        return ls_new_text


def main(argv):

    parser = argparse.ArgumentParser(
        description="Print out the text file using different characters",
        usage="Usage : python main.py file",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("file", nargs="?", help="encoded in UTF-8")
    parser.add_argument(
        "-l",
        "--level",
        dest="level",
        default=1,
        type=int,
        help="""
        1: insert non printable characters within the text
        2: replace some latin letters to their Greek or Cyrilic equivalent
        3: insert non printable characters and change the some latin  to their Greek or Cyrilic equivalent
        4: insert non printable chraracters change all possible letter to a randomly picked unicode letter equivalent""",
    )
    parser.add_argument(
        "-g",
        "--generate",
        dest="generate",
        type=int,
        help="Scramble x times the string",
    )
    parser.add_argument(
        "-o",
        "--outfile",
        default=None,
        dest="outfile",
        type=str,
        help="The output file",
    )
    args = parser.parse_args(argv)

    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(1)

    with open(args.file) as input_file:
        text = input_file.read()
        scrambler = Scrambler()
        if args.generate:
            res = scrambler.generate(text, args.generate, args.level)
            _dummy_output("".join(res), file_name=args.outfile)
        else:
            res = scrambler.scramble(text, level=args.level)
            _dummy_output(res, file_name=args.outfile)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
