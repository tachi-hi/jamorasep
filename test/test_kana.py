import unittest
import jamorasep

class TestJpmorasep(unittest.TestCase):
    def test_h2k(self):
        self.assertEqual(jamorasep.h2k('あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん'),
                         'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン')
        self.assertEqual(jamorasep.h2k('がぎぐげござじずぜぞだぢづでどばびぶべぼぱぴぷぺぽゔ'),
                         'ガギグゲゴザジズゼゾダヂヅデドバビブベボパピプペポヴ')
        self.assertEqual(jamorasep.h2k('ーっ'), 'ーッ')
        self.assertEqual(jamorasep.h2k('ぁぃぅぇぉゃゅょゎ'), 'ァィゥェォャュョヮ')
        self.assertEqual(jamorasep.h2k('ゐゑ'), 'ヰヱ')
        self.assertEqual(jamorasep.h2k('ゕゖ'), 'ヵヶ')
        self.assertEqual(jamorasep.h2k('abc123一二三,.、。「」'), 'abc123一二三,.、。「」')

    def test_k2h(self):
        self.assertEqual(jamorasep.k2h('アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン'),
                         'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん')
        self.assertEqual(jamorasep.k2h('ガギグゲゴザジズゼゾダヂヅデドバビブベボパピプペポヴ'),
                         'がぎぐげござじずぜぞだぢづでどばびぶべぼぱぴぷぺぽゔ')
        self.assertEqual(jamorasep.k2h('ーッ'), 'ーっ')
        self.assertEqual(jamorasep.k2h('ァィゥェォャュョヮ'), 'ぁぃぅぇぉゃゅょゎ')
        self.assertEqual(jamorasep.k2h('ヰヱ'), 'ゐゑ')
        self.assertEqual(jamorasep.k2h('ヵヶ'), 'ゕゖ')
        self.assertEqual(jamorasep.h2k('abc123一二三,.、。「」'), 'abc123一二三,.、。「」')

    def test_is_hiragana(self):
        self.assertTrue(jamorasep.is_hiragana('あいうえお'))
        self.assertTrue(jamorasep.is_hiragana('ぁぃぅぇぉ'))
        self.assertTrue(jamorasep.is_hiragana('ゃゅょ'))
        self.assertFalse(jamorasep.is_hiragana('アイウエオ'))
        self.assertFalse(jamorasep.is_hiragana('ァィゥェォ'))
        self.assertFalse(jamorasep.is_hiragana('ャュョ'))

    def test_is_katakana(self):
        self.assertTrue(jamorasep.is_katakana('アイウエオ'))
        self.assertTrue(jamorasep.is_katakana('ァィゥェォ'))
        self.assertTrue(jamorasep.is_katakana('ャュョ'))
        self.assertFalse(jamorasep.is_katakana('あいうえお'))
        self.assertFalse(jamorasep.is_katakana('ぁぃぅぇぉ'))
        self.assertFalse(jamorasep.is_katakana('ゃゅょ'))

    def test_is_kana(self):
        self.assertTrue(jamorasep.is_kana('あいうえおアイウエオ'))
        self.assertFalse(jamorasep.is_kana('あいうえおアイウエオa'))
if __name__ == '__main__':
    unittest.main()