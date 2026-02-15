#!/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import csv
from typing import List, Dict, Optional
from .kana_util import h2k, k2h

class Kanamap:
    def __init__(self, kanamap_csv: Optional[str] = None) -> None:
        self.kanamap = self.load_kanamap(kanamap_csv)

    def load_kanamap(self, kanamap_csv: Optional[str] = None) -> Dict[str, Dict[str, str]]:
        if kanamap_csv is None:
            path = os.path.dirname(os.path.abspath(__file__))
            kanamap_csv = f"{path}/resource/kanamap.csv"
        kanamap = {}
        with open(kanamap_csv, "r", encoding="utf-8") as f:
            csv_ = csv.DictReader(f)
            for row in csv_:
                kanamap[row["katakana"]] = row
        return kanamap

    def __call__(self, kana: str) -> Dict[str, str]:
        return self.kanamap[kana]

    def get_2letter_morae(self) -> List[str]:
        return list(filter(lambda x: len(x) == 2, self.kanamap.keys()))

    def lst_katakana(self) -> List[str]:
        return list(self.kanamap.keys())

    def header(self) -> List[str]:
        return list(self.kanamap["ア"].keys())

class Morasep:
    def __init__(self, kanamap_csv: Optional[str] = None) -> None:
        self.kanamap = Kanamap(kanamap_csv)
        self.two_letter_morae = self.kanamap.get_2letter_morae()
        self.subscript = list("ァィゥェォャュョヮぁぃぅぇぉゃゅょゎ")
        self.upper = {c: chr(ord(c) + 1) for c in self.subscript}  # "ァ" -> "ア" etc.

    def check_if_successive_2chars_compose_mora(self, i: str, j: str) -> List[str]:
        """Check if the successive 2 characters compose a mora.

        If so, return the mora. If not, return the list of morae
        depending on the relationship between the 2 characters.

        Rules:
            RULE 0: i + j forms a known two-letter mora (e.g., "キャ", "シュ")
            RULE 1: i is normal kana + j is subscript but not a valid mora -> convert subscript to normal (e.g., "カァ" -> ["カ", "ア"])
            RULE 2: i is subscript + j is normal kana -> return [] (handled by previous pair)
            RULE 3: i is subscript + j is subscript -> convert j to normal (e.g., "ァァ" -> ["ア"])
            RULE 4: Otherwise -> return [i]
        """
        I, J = h2k(i), h2k(j)

        if I + J in self.two_letter_morae:
            # Rule 0
            return [i + j]
        elif ((not I in self.subscript) and (    J in self.subscript)):
            # Rule 1
            return [i, self.upper[j]]
        elif ((    I in self.subscript) and (not J in self.subscript)):
            # Rule 2
            return []
        elif ((    I in self.subscript) and (    J in self.subscript)):
            # Rule 3
            return [self.upper[j]]
        else:
            # Rule 4
            return [i]

    def kana2mora(self, txt: str) -> List[str]:
        """Convert a string of Japanese text (hiragana or katakana) into a list of morae.

        Symbols and characters other than hiragana/katakana are separated
        character-wise and returned without modification.

        Example:
            "あいうえお・きゃきゅきょ" -> ["あ", "い", "う", "え", "お", "・", "きゃ", "きゅ", "きょ"]

        Args:
            txt: A string of Japanese text (hiragana or katakana).
        Returns:
            A list of morae.
        """
        bos_token = "[BOS]"
        eos_token = "[EOS]"
        lst = [bos_token] + list(txt) + [eos_token]
        lst1, lst2 = lst[:-1], lst[1:]
        morae = [self.check_if_successive_2chars_compose_mora(*v) for v in zip(lst1, lst2)]
        morae = sum(morae, [])
        morae = list(filter(lambda x: x not in [bos_token, eos_token], morae))
        return morae

    def modify_special_mora(self, morae: List[str]) -> List[str]:
        """Modify Q (ッ) in a romanized mora list.

        - If Q is the last mora, replace with a space.
        - If the next mora starts with a consonant, replace Q with that consonant.
        - If the next mora starts with a vowel or symbol, replace Q with a space.

        Args:
            morae: A list of morae.
        Returns:
            A list of morae with Q replaced.
        """
        for i in range(len(morae) - 1, -1, -1):
            if morae[i] == "Q":
                if i == len(morae) - 1:
                    morae[i] = " "  # space
                else:
                    next_char = morae[i + 1][0]
                    if next_char in ["k", "g", "s", "z", "j", "t", "c", "d", "n", "h", "p", "b", "f", "m", "y", "r", "w", "v"]:
                        morae[i] = next_char
                    elif next_char in ["a", "i", "u", "e", "o"]:
                        morae[i] = " "
                    else:
                        # if next_char is a symbol (such as period) or others.
                        morae[i] = " "
        return morae

    def _convert_to_hiragana(self, lst: List[str]) -> List[str]:
        map_f = lambda _: k2h(_) if _ in self.kanamap.lst_katakana() else _
        return list(map(map_f, lst))

    def _convert_to_katakana(self, lst: List[str]) -> List[str]:
        map_f = lambda _: h2k(_) if _ in self.kanamap.lst_katakana() else _
        return list(map(map_f, lst))

    def _convert_to_other_format(self, lst: List[str], output_format: str) -> List[str]:
        map_f = lambda _: self.kanamap(_)[output_format] if _ in self.kanamap.lst_katakana() else _
        morae = list(map(map_f, map(h2k, lst)))
        if output_format != "simple-ipa":
            morae = self.modify_special_mora(morae)
        return morae

    def convert_lst_of_mora(self, lst: List[str], output_format: str = "katakana", phoneme: bool = False) -> List[str]:
        """Convert a list of morae into katakana, hiragana, or other formats.

        Args:
            lst: A list of morae.
            output_format: The output format. Options are "katakana", "hiragana",
                and any column in kanamap.csv (e.g., "kunrei", "hepburn", "simple-ipa").
            phoneme: If True, split the output into individual phonemes.
                Only effective when output_format is a romanization format.
        Returns:
            A list of morae in the specified format.
        """
        if output_format == "hiragana":
            ret = self._convert_to_hiragana(lst)
        elif output_format == "katakana":
            ret = self._convert_to_katakana(lst)
        elif output_format in self.kanamap.header():
            ret = self._convert_to_other_format(lst, output_format)
            if phoneme:
                ret = list("".join(ret))
        else:
            raise ValueError(f"output_format '{output_format}' is not supported. Valid options are 'katakana', 'hiragana', or a column name in kanamap.csv")
        return ret

    def parse(self, txt: str = "", output_format: Optional[str] = None, phoneme: bool = False, **kwargs) -> List[str]:
        """Convert a kana string into a list of morae.

        Args:
            txt: A string of katakana or hiragana.
            output_format: The output format. If None, return morae as-is.
                Options are "katakana", "hiragana", and any column in kanamap.csv
                (e.g., "kunrei", "hepburn", "simple-ipa").
            phoneme: If True, split the output into individual phonemes.
        Returns:
            A list of morae.
        """
        # Support legacy kwargs interface
        if output_format is None and "output_format" in kwargs:
            output_format = kwargs["output_format"]
        if not phoneme and "phoneme" in kwargs:
            phoneme = kwargs["phoneme"]

        sep = self.kana2mora(txt)
        if not output_format:
            return sep
        else:
            return self.convert_lst_of_mora(sep, output_format, phoneme)

parse = Morasep().parse
