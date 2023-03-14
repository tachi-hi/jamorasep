from typing import Union, List

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

def is_hiragana(text : Union[str, List[str]] = ""):
    """Check if the input is hiragana.
    Only Unicode is supported, which is the default code in Python3.

    Args:
        text (str): string
    Returns:
        bool: True if the input is hiragana.
    """
    if isinstance(text, list):
        text = ''.join(text)
    return all([ord(char)>=0x3041 and ord(char)<=0x3097 for char in text])

def is_katakana(text : Union[str, List[str]] = ""):
    """Check if the input is katakana.
    Only Unicode is supported, which is the default code in Python3.

    Args:
        text (str): string
    Returns:
        bool: True if the input is katakana.
    """
    if isinstance(text, list):
        text = ''.join(text)
    return all([ord(char)>=0x30A1 and ord(char)<=0x30F7 for char in text])

def is_kana(text : Union[str, List[str]] = ""):
    """Check if the input is hiragana or katakana.
    Only Unicode is supported, which is the default code in Python3.

    Args:
        text (str): string
    Returns:
        bool: True if the input is hiragana or katakana.
    """
    return is_katakana(h2k(text))
