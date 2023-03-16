import unittest
import jamorasep

class TestAccent(unittest.TestCase):
    def test_accent(self):
        self.assertEqual("".join(jamorasep.accent.embed('あいうえお', 0)),
            'あ[いうえお')
        self.assertEqual("".join(jamorasep.accent.embed('あいうえお', 1)),
            '[あ]いうえお')
        self.assertEqual("".join(jamorasep.accent.embed('あいうえお', 2)),
            'あ[い]うえお')
        self.assertEqual("".join(jamorasep.accent.embed('あいうえお', 3)),
            'あ[いう]えお')
        self.assertEqual("".join(jamorasep.accent.embed('あいうえお', 4)),
            'あ[いうえ]お')
        self.assertEqual("".join(jamorasep.accent.embed('あいうえお', 5)),
            'あ[いうえお]')

    def test_accent_moralist(self):
        self.assertEqual("".join(jamorasep.accent.embed(['あ', 'い', 'う', 'え', 'お'], 0)),
            'あ[いうえお')

    def test_initial_rising(self):
        self.assertEqual("".join(jamorasep.accent.embed('あいうえお', 0, initial_rising=True)),
            '[あいうえお')
        self.assertEqual("".join(jamorasep.accent.embed('あいうえお', 1, initial_rising=True)),
            '[あ]いうえお')
        self.assertEqual("".join(jamorasep.accent.embed('あいうえお', 2, initial_rising=True)),
            '[あい]うえお')
        self.assertEqual("".join(jamorasep.accent.embed('あいうえお', 3, initial_rising=True)),
            '[あいう]えお')
        self.assertEqual("".join(jamorasep.accent.embed('あいうえお', 4, initial_rising=True)),
            '[あいうえ]お')
        self.assertEqual("".join(jamorasep.accent.embed('あいうえお', 5, initial_rising=True)),
            '[あいうえお]')



    def test_assert(self):
        # invalid accent type
        self.assertRaises(AssertionError, jamorasep.accent.embed, 'あいうえお', -1)
        self.assertRaises(AssertionError, jamorasep.accent.embed, 'あいうえお', 6)
        # invalid input string
        self.assertRaises(AssertionError, jamorasep.accent.embed, '日本語', 1)

if __name__ == '__main__':
    unittest.main()