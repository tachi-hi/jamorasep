#!/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import pandas as pd
from typing import List

def h2k(text : str = ""):
    """Convert hiragana to katakana.
    Characters other than hiragana are not converted.
    Only Unicode is supported, which is the default code in Python3.

    Args:
        text (str): hiragana string
    Returns:
        str: katakana string
    """
    return ''.join([chr(ord(char)+0x60) if ord(char)>=0x3041 and ord(char)<=0x3097 else char for char in text])
    # return ''.join([chr(ord(char)+96) if ord(char)>=12353 and ord(char)<=12439 else char for char in text])

def k2h(text : str = ""):
    """Convert katakana to hiragana.
    Characters other than katakana are not converted.
    Only Unicode is supported, which is the default code in Python3.
    Hankaku katakana will not be converted.
    Some special katakana such as ヸ will not be converted, too.

    Args:
        text (str): katakana string
    Returns:
        str: hiragana string
    """
    return ''.join([chr(ord(char)-0x60) if ord(char)>=0x30A1 and ord(char)<=0x30F7 else char for char in text])
    # return ''.join([chr(ord(char)-96) if ord(char)>=12449 and ord(char)<=12535 else char for char in text])

class Kanamap:
    def __init__(self, kanamap_csv : str = None):
        self.kanamap = self.load_kanamap(kanamap_csv)

    def load_kanamap(self, kanamap_csv : str = None):
        if kanamap_csv is None:
            path = os.path.dirname(os.path.abspath(__file__))
            kanamap_csv = f"{path}/resource/kanamap.csv"
        kanamap = pd.read_csv(kanamap_csv,index_col=0)
        kanamap.fillna(False, inplace=True)
        return kanamap

    def __call__(self, kana):
        return self.kanamap.loc[kana].to_dict()

    def get_2letter_morae(self):
        return list(filter(lambda x: len(x) == 2, self.kanamap.index.to_list()))

    def lst_katakana(self):
        return self.kanamap.index

    def header(self):
        return self.kanamap.columns

class Morasep:
    def __init__(self, kanamap_csv : str = None):
        self.kanamap = Kanamap(kanamap_csv)
        self.mora_with_subs = self.kanamap.get_2letter_morae()
        self.subscript = list("ァィゥェォャュョヮぁぃぅぇぉゃゅょゎ")
        self.upper = {c : chr(ord(c) + 1) for c in self.subscript} # "ァ" -> "ア" etc.

    def check_if_successive_2chars_compose_mora(self, i, j):
        """Check if the successive 2 characters compose a mora.
            If so, return the mora. If not, return the list of morae depending on the relationship between the 2 characters.

            More specifically, assume that the input is a katakana string such as
                [BOS]アイウキャカァィゥエ[EOS]

            Then this function evaluates the successive 2 characters
                [BOS]ア, アイ, イウ, ウキ, キャ, ャカ, カァ, ァィ, ィゥ, ゥエ, エ[EOS]
            and returns the list of morae as follows
                [BOS]ア: -> [BOS] (RULE 4)
                アイ: -> ア (RULE 4)
                イウ: -> イ (RULE 4)
                ウキ: -> ウ (RULE 4)
                キャ: -> キャ (RULE 0)
                ャカ: -> [] (RULE 2)
                カァ: -> カ, ア (RULE 1)
                ァィ: -> イ (RULE 3)
                ィゥ: -> ウ (RULE 3)
                ゥエ: -> [] (RULE 2)
                エ[EOS]: -> エ (RULE 4)
            The [BOS] token should be eventually removed by the caller.

            Each rule is described in the following.
                RULE 0: i + j が「キャ」「シュ」など、辞書に記載のパターンに合致する場合
                RULE 1: 「カァ」のような、辞書に記載したパターンに合致せず1モーラを形成しない場合は「カア」などに変換して返す
                RULE 2: 「ァカ」のような、1文字目が小文字で、次の文字が大文字のパターンの場合は、ここでは何も返さない
                RULE 3: 「ァァ」のような、1文字目が小文字で、次の文字も小文字のパターンの場合は、2文字目のみを「ア」に変換した上で返す
                RULE 4: それ以外のパターンの場合は、1文字目のみを返す
        """
        I, J = h2k(i), h2k(j)

        if I + J in self.mora_with_subs:
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

    def kana2mora(self, txt : str) -> List[str]:
        """
        Convert a string of Japanese text (hiragana or katakana) into a list of morae. (Mora is a unit of Japanese syllable.)
        Symbols and characters other than hiragana/katakana are just separated character-wise and returned without any modification.
        For example,
            "あいうえお・きゃきゅきょ・一二三<tag>"
        will be converted into
            ["あ", "い", "う", "え", "お", "・", "きゃ", "きゅ", "きょ", "・", "一", "二", "三", "<", "t", "a", "g", ">"]

        Args:
            a string of Japanese text (hiragana or katakana).
        Returns:
            a list of morae.
        """
        bos_token = "[BOS]"
        eos_token = "[EOS]"
        lst = [bos_token] + list(txt) + [eos_token]
        lst1, lst2 = lst[:-1], lst[1:]
        morae = [self.check_if_successive_2chars_compose_mora(*v) for v in zip(lst1, lst2)]
        morae = sum(morae, [])
        morae = list(filter(lambda x: x not in [bos_token, eos_token], morae))
        return morae

    def modify_special_mora(self, morae : List[str]) -> List[str]:
        """
        Modify Q (ッ).
        If the last mora is Q, it should be replaced with a space.
        If the next mora starts with a vowel, Q should be replaced with a space.
        If the next mora starts with some kinds of consonants, Q should be replaced with the initial consonant of the following mora.

        Args:
            a list of morae.
        Returns:
            a list of morae.
        """
        for i in range(len(morae)-1 , -1, -1):
            if morae[i] == "Q":
                if i == len(morae)-1:
                    morae[i] = " " # space
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

    def convert_lst_of_mora(self, lst : List[str], output_format="katakana", phoneme=False) -> List[str]:
        """
        Convert a list of morae into a list of katakana or hiragana or other formats.

        Args:
            lst (list): A list of morae.
            output_format (str): The output format of the morae. Defaults to "katakana".
                Options are ["katakana", "hiragana"], and any of the columns in the kanamap.csv file,
                including ["kunrei", "hepburn", "simple-ipa"]. Defaults to "katakana".
        """

        if output_format == "hiragana":
            map_f = lambda _ : k2h(_) if _ in self.kanamap.lst_katakana() else _
            ret = list(map(map_f, lst))
        elif output_format == "katakana":
            map_f = lambda _ : h2k(_) if _ in self.kanamap.lst_katakana() else _
            ret = list(map(map_f, lst))
        elif output_format in self.kanamap.header():
            map_f = lambda _ : self.kanamap(_)[output_format] if _ in self.kanamap.lst_katakana() else _
            morae = list(map(map_f, map(h2k, lst)))
            if output_format != "simple-ipa":
                morae = self.modify_special_mora(morae)
            if phoneme:
                morae = list("".join(morae))
            ret = morae
        else:
            raise ValueError(f"output_format {output_format} is not supported.")
        return ret


    def parse(self, txt : str ="", **kwargs) -> List[str]:
        """
        Converts a string of katakana into a list of morae.

        Args:
            txt (str): A string of katakana.
            output_format (str): The output format of the morae. Defaults to None.
                If None, the output is a list of morae.
                Options are ["katakana", "hiragana"], and any of the columns in the kanamap.csv file,
                including ["kunrei", "hepburn", "simple-ipa"].
            phoneme (bool): If True, the output is a list of phonemes. Defaults to False.
                This flag is only valid when output_format is either of ["kunrei", "hepburn", "simple-ipa"].
        Returns:
            list: A list of morae.
        """
        output_format = kwargs["output_format"] if "output_format" in kwargs else None
        phoneme = kwargs["phoneme"] if "phoneme" in kwargs else False
        sep = self.kana2mora(txt)
        if not output_format:
            return sep
        else:
            return self.convert_lst_of_mora(sep, output_format, phoneme)

parse = Morasep().parse
