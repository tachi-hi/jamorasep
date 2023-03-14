import unittest
import jamorasep
from jamorasep import parse


class TestJpmorasep(unittest.TestCase):

    def test_katakana(self):
        self.assertEqual(parse('アイウエオ'), ['ア', 'イ', 'ウ', 'エ', 'オ'])
        self.assertEqual(parse('カキクケコ'), ['カ', 'キ', 'ク', 'ケ', 'コ'])
        self.assertEqual(parse('サシスセソ'), ['サ', 'シ', 'ス', 'セ', 'ソ'])
        self.assertEqual(parse('タチツテト'), ['タ', 'チ', 'ツ', 'テ', 'ト'])
        self.assertEqual(parse('ナニヌネノ'), ['ナ', 'ニ', 'ヌ', 'ネ', 'ノ'])
        self.assertEqual(parse('ハヒフヘホ'), ['ハ', 'ヒ', 'フ', 'ヘ', 'ホ'])
        self.assertEqual(parse('マミムメモ'), ['マ', 'ミ', 'ム', 'メ', 'モ'])
        self.assertEqual(parse('ヤユヨ'), ['ヤ', 'ユ', 'ヨ'])
        self.assertEqual(parse('ラリルレロ'), ['ラ', 'リ', 'ル', 'レ', 'ロ'])
        self.assertEqual(parse('ワヲン'), ['ワ', 'ヲ', 'ン'])
        self.assertEqual(parse('ガギグゲゴ'), ['ガ', 'ギ', 'グ', 'ゲ', 'ゴ'])
        self.assertEqual(parse('ザジズゼゾ'), ['ザ', 'ジ', 'ズ', 'ゼ', 'ゾ'])
        self.assertEqual(parse('ダヂヅデド'), ['ダ', 'ヂ', 'ヅ', 'デ', 'ド'])
        self.assertEqual(parse('バビブベボ'), ['バ', 'ビ', 'ブ', 'ベ', 'ボ'])
        self.assertEqual(parse('パピプペポ'), ['パ', 'ピ', 'プ', 'ペ', 'ポ'])
        self.assertEqual(parse('ヴァヴィヴヴェヴォ'), ['ヴァ', 'ヴィ', 'ヴ', 'ヴェ', 'ヴォ'])
        self.assertEqual(parse('キャキュキェキョ'), ['キャ', 'キュ', 'キェ', 'キョ'])
        self.assertEqual(parse('シャシュシェショ'), ['シャ', 'シュ', 'シェ', 'ショ'])
        self.assertEqual(parse('チャチュチェチョ'), ['チャ', 'チュ', 'チェ', 'チョ'])
        self.assertEqual(parse('ツァツィツェツォ'), ['ツァ', 'ツィ', 'ツェ', 'ツォ'])
        self.assertEqual(parse('ニャニュニェニョ'), ['ニャ', 'ニュ', 'ニェ', 'ニョ'])
        self.assertEqual(parse('ヒャヒュヒェヒョ'), ['ヒャ', 'ヒュ', 'ヒェ', 'ヒョ'])
        self.assertEqual(parse('ミャミュミェミョ'), ['ミャ', 'ミュ', 'ミェ', 'ミョ'])
        self.assertEqual(parse('リャリュリェリョ'), ['リャ', 'リュ', 'リェ', 'リョ'])
        self.assertEqual(parse('ギャギュギェギョ'), ['ギャ', 'ギュ', 'ギェ', 'ギョ'])
        self.assertEqual(parse('ジャジュジェジョ'), ['ジャ', 'ジュ', 'ジェ', 'ジョ'])
        self.assertEqual(parse('ビャビュビェビョ'), ['ビャ', 'ビュ', 'ビェ', 'ビョ'])
        self.assertEqual(parse('ピャピュピェピョ'), ['ピャ', 'ピュ', 'ピェ', 'ピョ'])
        self.assertEqual(parse('ファフィフェフォ'), ['ファ', 'フィ', 'フェ', 'フォ'])
        self.assertEqual(parse('ウィウェウォ'), ['ウィ', 'ウェ', 'ウォ'])
        self.assertEqual(parse('クァクィクェクォ'), ['クァ', 'クィ', 'クェ', 'クォ'])
        self.assertEqual(parse('グァグィグェグォ'), ['グァ', 'グィ', 'グェ', 'グォ'])
        self.assertEqual(parse('ティディ'), ['ティ', 'ディ'])
        self.assertEqual(parse('トゥドゥ'), ['トゥ', 'ドゥ'])
        self.assertEqual(parse('テュデュ'), ['テュ', 'デュ'])
        self.assertEqual(parse('テェデェ'), ['テェ', 'デェ'])
        self.assertEqual(parse('テョデョ'), ['テョ', 'デョ'])
        self.assertEqual(parse('スィズィ'), ['スィ', 'ズィ'])

    def test_hiragana(self):
        self.assertEqual(parse('あいうえお'), ['あ', 'い', 'う', 'え', 'お'])
        self.assertEqual(parse('かきくけこ'), ['か', 'き', 'く', 'け', 'こ'])
        self.assertEqual(parse('さしすせそ'), ['さ', 'し', 'す', 'せ', 'そ'])
        self.assertEqual(parse('たちつてと'), ['た', 'ち', 'つ', 'て', 'と'])
        self.assertEqual(parse('なにぬねの'), ['な', 'に', 'ぬ', 'ね', 'の'])
        self.assertEqual(parse('はひふへほ'), ['は', 'ひ', 'ふ', 'へ', 'ほ'])
        self.assertEqual(parse('まみむめも'), ['ま', 'み', 'む', 'め', 'も'])
        self.assertEqual(parse('やゆよ'), ['や', 'ゆ', 'よ'])
        self.assertEqual(parse('らりるれろ'), ['ら', 'り', 'る', 'れ', 'ろ'])
        self.assertEqual(parse('わをん'), ['わ', 'を', 'ん'])
        self.assertEqual(parse('がぎぐげご'), ['が', 'ぎ', 'ぐ', 'げ', 'ご'])
        self.assertEqual(parse('ざじずぜぞ'), ['ざ', 'じ', 'ず', 'ぜ', 'ぞ'])
        self.assertEqual(parse('だぢづでど'), ['だ', 'ぢ', 'づ', 'で', 'ど'])
        self.assertEqual(parse('ばびぶべぼ'), ['ば', 'び', 'ぶ', 'べ', 'ぼ'])
        self.assertEqual(parse('ぱぴぷぺぽ'), ['ぱ', 'ぴ', 'ぷ', 'ぺ', 'ぽ'])
        self.assertEqual(parse('ゔぁゔぃゔゔぇゔぉ'), ['ゔぁ', 'ゔぃ', 'ゔ', 'ゔぇ', 'ゔぉ'])
        self.assertEqual(parse('きゃきゅきぇきょ'), ['きゃ', 'きゅ', 'きぇ', 'きょ'])
        self.assertEqual(parse('しゃしゅしぇしょ'), ['しゃ', 'しゅ', 'しぇ', 'しょ'])
        self.assertEqual(parse('ちゃちゅちぇちょ'), ['ちゃ', 'ちゅ', 'ちぇ', 'ちょ'])
        self.assertEqual(parse('つぁつぃつぇつぉ'), ['つぁ', 'つぃ', 'つぇ', 'つぉ'])
        self.assertEqual(parse('にゃにゅにぇにょ'), ['にゃ', 'にゅ', 'にぇ', 'にょ'])
        self.assertEqual(parse('ひゃひゅひぇひょ'), ['ひゃ', 'ひゅ', 'ひぇ', 'ひょ'])
        self.assertEqual(parse('みゃみゅみぇみょ'), ['みゃ', 'みゅ', 'みぇ', 'みょ'])
        self.assertEqual(parse('りゃりゅりぇりょ'), ['りゃ', 'りゅ', 'りぇ', 'りょ'])
        self.assertEqual(parse('ぎゃぎゅぎぇぎょ'), ['ぎゃ', 'ぎゅ', 'ぎぇ', 'ぎょ'])
        self.assertEqual(parse('じゃじゅじぇじょ'), ['じゃ', 'じゅ', 'じぇ', 'じょ'])
        self.assertEqual(parse('びゃびゅびぇびょ'), ['びゃ', 'びゅ', 'びぇ', 'びょ'])
        self.assertEqual(parse('ぴゃぴゅぴぇぴょ'), ['ぴゃ', 'ぴゅ', 'ぴぇ', 'ぴょ'])
        self.assertEqual(parse('ふぁふぃふぇふぉ'), ['ふぁ', 'ふぃ', 'ふぇ', 'ふぉ'])
        self.assertEqual(parse('うぃうぇうぉ'), ['うぃ', 'うぇ', 'うぉ'])
        self.assertEqual(parse('くぁくぃくぇくぉ'), ['くぁ', 'くぃ', 'くぇ', 'くぉ'])
        self.assertEqual(parse('ぐぁぐぃぐぇぐぉ'), ['ぐぁ', 'ぐぃ', 'ぐぇ', 'ぐぉ'])
        self.assertEqual(parse('てぃでぃ'), ['てぃ', 'でぃ'])
        self.assertEqual(parse('とぅどぅ'), ['とぅ', 'どぅ'])
        self.assertEqual(parse('てゅでゅ'), ['てゅ', 'でゅ'])
        self.assertEqual(parse('てぇでぇ'), ['てぇ', 'でぇ'])
        self.assertEqual(parse('てょでょ'), ['てょ', 'でょ'])
        self.assertEqual(parse('ふぃふぇ'), ['ふぃ', 'ふぇ'])
        self.assertEqual(parse('ふゃふゅふぉ'), ['ふゃ', 'ふゅ', 'ふぉ'])

    def test_mixed(self):
        self.assertEqual(parse('キゃきュきェキょ'), ['キゃ', 'きュ', 'きェ', 'キょ'])

    def test_romanize_kunrei(self):
        self.assertEqual(parse('キゃきュきェキょ', output_format="kunrei"), ['kya', 'kyu', 'kye', 'kyo'])
        self.assertEqual(parse('ワヲン', output_format="simple-ipa"), ['wa', 'o', 'N'])
        self.assertEqual(parse('ワヲン', output_format="kunrei"), ['wa', 'o', 'n'])

    def test_Q(self):
        self.assertEqual(parse('カッキックッケッコッ'), ['カ', 'ッ', 'キ', 'ッ', 'ク', 'ッ', 'ケ', 'ッ', 'コ', 'ッ'])
        self.assertEqual(parse('アッイッウッエッオッ'), ['ア', 'ッ', 'イ', 'ッ', 'ウ', 'ッ', 'エ', 'ッ', 'オ', 'ッ'])
        self.assertEqual(parse('カッキックッケッコッ',output_format="kunrei"), ['ka', 'k', 'ki', 'k', 'ku', 'k', 'ke', 'k', 'ko', ' '])
        self.assertEqual(parse('アッイッウッエッオッ',output_format="kunrei"), ['a', ' ', 'i', ' ', 'u', ' ', 'e', ' ', 'o', ' '])
        self.assertEqual(parse('カッッッッキッッッックッッッッケッッッッコッッッッ',output_format="kunrei"),
                        ['ka', 'k', 'k', 'k', 'k',
                         'ki', 'k', 'k', 'k', 'k',
                         'ku', 'k', 'k', 'k', 'k',
                         'ke', 'k', 'k', 'k', 'k',
                         'ko', ' ', ' ', ' ', ' '])
        self.assertEqual(parse('シャッシュッショッ',output_format="kunrei"),
                         ['sya', 's', 'syu', 's', 'syo', ' '])
        self.assertEqual(parse('シャッシュッショッ',output_format="kunrei", phoneme=True),
                         ['s', 'y', 'a', 's', 's', 'y', 'u', 's', 's', 'y', 'o', ' '])
        self.assertEqual(parse('しょっぱい'),
                         ['しょ', 'っ', 'ぱ', 'い'])
        self.assertEqual(parse('ッッッッッ'), ['ッ'] * 5),
        self.assertEqual(parse('ッッッッッ', output_format="simple-ipa"), ['Q'] * 5),
        self.assertEqual(parse('ッッッッッ', output_format="kunrei"), [' '] * 5),
        self.assertEqual(parse('ッッッッッ。', output_format="kunrei"), [' '] * 5 + ['。']),
        self.assertEqual(parse('ッ。ッ。ッ。ッ。ッ。', output_format="kunrei"), [' ', '。'] * 5),
        self.assertEqual(parse('アッカッサッタッチッナッハッマッヤッラッワッガッザッジャッダッバッパッヴァッア', output_format="hepburn"),
                         ['a', 'k', 'ka', 's', 'sa', 't', 'ta', 'c', 'chi',
                          'n', 'na', 'h', 'ha', 'm', 'ma', 'y', 'ya', 'r', 'ra',
                          'w', 'wa', 'g', 'ga', 'z', 'za', 'j', 'ja', 'd', 'da',
                          'b', 'ba', 'p', 'pa', 'v', 'va', ' ', 'a']),
        self.assertEqual(parse('ッカ', output_format="kunrei"), ['k', 'ka']),
        self.assertEqual(parse('ッア', output_format="kunrei"), [' ', 'a']),

    def test_successive_small(self):
        self.assertEqual(parse('アイウキャカァィゥエ'),
                         ['ア', 'イ', 'ウ', 'キャ', 'カ', 'ア', 'イ', 'ウ', 'エ'])
        self.assertEqual(parse('ァァァィィィィゥゥゥゥゥェェ'),
                         ['ア'] * 3 + ['イ'] * 4 + ['ウ'] * 5 + ['エ'] * 2)
        self.assertEqual(parse('ァアィイゥウェエォオ'),
                         ['ア'] * 2 + ['イ'] * 2 + ['ウ', 'ウェ', 'エ'] + ['オ'] * 2)

    def test_specific_words(self):
        self.assertEqual(parse('ジョスカン・デ・プレ'),
                         ['ジョ', 'ス', 'カ', 'ン', '・', 'デ', '・', 'プ', 'レ'])
        self.assertEqual(parse('ヴォルフガング・アマデウス・モーツァルト'),
                         ['ヴォ', 'ル', 'フ', 'ガ', 'ン', 'グ', '・', 'ア', 'マ', 'デ', 'ウ', 'ス', '・', 'モ', 'ー', 'ツァ', 'ル', 'ト'])
        self.assertEqual(parse('ルートヴィヒ・ヴァン・ベートーヴェン'),
                         ['ル', 'ー', 'ト', 'ヴィ', 'ヒ', '・', 'ヴァ', 'ン', '・', 'ベ', 'ー', 'ト', 'ー', 'ヴェ', 'ン'])
        self.assertEqual(parse('シェーンベルク'),
                         ['シェ', 'ー', 'ン', 'ベ', 'ル', 'ク']),
        self.assertEqual(parse('エイトクィーン'),
                         ['エ', 'イ', 'ト', 'クィ', 'ー', 'ン'])
        self.assertEqual(parse('ディープラーニング'), [
            'ディ', 'ー', 'プ', 'ラ', 'ー', 'ニ', 'ン', 'グ'])

if __name__ == '__main__':
    unittest.main()