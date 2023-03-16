from typing import List, Union
from .. import parse, is_kana

def embed(morae : Union[List[str], str],
          aType : int,
          initial_rising = False,
          up : str = "[",
          down : str ="]") -> List[str]:
    """Embed accent to morae.

    Args:
        morae (Union(List[str], str)): List of morae or a hiragana/katakana string.
        aType (int): Accent type. 0: heiban, 1: atamadaka, 2~n-1: nakadaka, n: odaka
        initial_rising (bool, optional): Initial rising accent. Defaults to False.
        up (str, optional): Accent up mark. Defaults to "[".
        down (str, optional): Accent down mark. Defaults to "]".

    Returns:
        List[str]: List of morae with accent.
    """
    if isinstance(morae, str):
        morae = parse(morae)

    # assert
    assert(is_kana(morae))
    assert(aType >= 0)
    assert(aType <= len(morae))

    # accent types
    if aType == 0:
        if initial_rising:
            morae = [up] + morae[0:]
        else:
            morae = morae[0:1] + [up] + morae[1:]
    elif aType == 1:
        morae = [up] + morae[0:1] + [down] + morae[1:]
    elif aType >= 2:
        if initial_rising:
            morae = [up] + morae[0:aType] + [down] + morae[aType:]
        else:
            morae = morae[0:1] + [up] + morae[1:aType] + [down] + morae[aType:]
    return morae