#!/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import csv
from typing import List, Union, Dict
from .kana_util import h2k, k2h

class Kanamap:
    def __init__(self, kanamap_csv : Union[str, None] = None) -> None:
        self.kanamap = self.load_kanamap(kanamap_csv)

    def load_kanamap(self, kanamap_csv : Union[str, None] = None) -> Dict:
        if kanamap_csv is None:
            path = os.path.dirname(os.path.abspath(__file__))
            kanamap_csv = f"{path}/resource/kanamap.csv"
        kanamap = {}
        with open(kanamap_csv, "r", encoding="utf-8") as f:
            csv_ = csv.DictReader(f)
            for row in csv_:
                kanamap[row["katakana"]] = row
        return kanamap

    def __call__(self, kana: str) -> Dict:
        return self.kanamap[kana]

    def get_2letter_morae(self) -> List[str]:
        return list(filter(lambda x: len(x) == 2, self.kanamap.keys()))

    def lst_katakana(self) -> List[str]:
        return self.kanamap.keys()

    def header(self) -> List[str]:
        return self.kanamap["ア"].keys()

class Morasep:
    def __init__(self, kanamap_csv : Union[str, None] = None) -> None:
        self.kanamap = Kanamap(kanamap_csv)
        self.two_letter_morae = self.kanamap.get_2letter_morae()
        self.subscript = list("ァィゥェォャュョヮぁぃぅぇぉゃゅょゎ")
        self.upper = {c : chr(ord(c) + 1) for c in self.subscript} # "ァ" -> "ア" etc.

    def _is_mora_with_subs(self, i: str, j: str) -> bool:
        I, J = h2k(i), h2k(j)
        return I + J in self.two_letter_morae

    def _handle_rule1(self, i: str, j: str) -> List[str]:
        return [i, self.upper[j]]

    def _handle_rule3(self, i: str, j: str) -> List[str]:
        return [self.upper[j]]

    def _handle_default_case(self, i: str) -> List[str]:
        return [i]

    def check_if_successive_2chars_compose_mora(self, i: str, j: str) -> List[str]:
        I, J = h2k(i), h2k(j)

        if self._is_mora_with_subs(i, j):
            # Rule 0
            return [i + j]
        elif ((not I in self.subscript) and (    J in self.subscript)):
            # Rule 1
            return self._handle_rule1(i, j)
        elif ((    I in self.subscript) and (not J in self.subscript)):
            # Rule 2
            return []
        elif ((    I in self.subscript) and (    J in self.subscript)):
            # Rule 3
            return [self.upper[j]]
        else:
            # Rule 4
            return self._handle_default_case(i)

    def kana2mora(self, txt : str) -> List[str]:
        bos_token = "[BOS]"
        eos_token = "[EOS]"
        lst = [bos_token] + list(txt) + [eos_token]
        lst1, lst2 = lst[:-1], lst[1:]
        morae = [self.check_if_successive_2chars_compose_mora(*v) for v in zip(lst1, lst2)]
        morae = sum(morae, [])
        morae = list(filter(lambda x: x not in [bos_token, eos_token], morae))
        return morae

    def modify_special_mora(self, morae: List[str]) -> List[str]:
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
        map_f = lambda _ : k2h(_) if _ in self.kanamap.lst_katakana() else _
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

    def convert_lst_of_mora(self, lst : List[str], output_format="katakana", phoneme=False) -> List[str]:
        if output_format == "hiragana":
            ret = self._convert_to_hiragana(lst)
        elif output_format == "katakana":
            ret = self._convert_to_katakana(lst)
        elif output_format in self.kanamap.header():
            ret = self._convert_to_other_format(lst, output_format)
            if phoneme:
                ret = list("".join(ret))
        else:
            raise ValueError(f"output_format {output_format} is not supported.")
        return ret

    def parse(self, txt : str ="", **kwargs) -> List[str]:
        output_format = kwargs["output_format"] if "output_format" in kwargs else None
        phoneme = kwargs["phoneme"] if "phoneme" in kwargs else False
        sep = self.kana2mora(txt)
        if not output_format:
            return sep
        else:
            return self.convert_lst_of_mora(sep, output_format, phoneme)

parse = Morasep().parse
