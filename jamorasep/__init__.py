__copyright__ = 'Copyright (C) 2023 Hideyuki Tachibana.'
__version__ = '0.0.2'
__license__ = 'MIT'
__author__ = 'Hideyuki Tachibana'
__author_email__ = 'h_tachibana@pkshatech.com'

__all__ = ['main', 'kana_util', 'accent']

import jamorasep.main
from jamorasep.main import parse
from jamorasep.main import Morasep
from jamorasep.kana_util import h2k, k2h, is_hiragana, is_katakana, is_kana

import jamorasep.accent
