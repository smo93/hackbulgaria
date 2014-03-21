import unittest
import solution
from subprocess import call, check_output


class WCTest(unittest.TestCase):
    """docstring for WCTest"""

    def setUp(self):
        story = ['Now indulgence dissimilar for his thoroughly has terminated.'\
        ' Agreement offending commanded my an. Change wholly say why eldest'\
        'period. Are projection put celebrated particular unreserved joy '\
        'unsatiable its. In then dare good am rose bred or. On am in nearer '\
        'square wanted.', ' ',
        'Of resolve to gravity thought my prepare chamber so. Unsatiable '\
        'entreaties collecting may sympathize nay interested instrument. '\
        'If continue building numerous of at relation in margaret. '\
        'Lasted engage roused mother an am at. Other early while if by do to. '\
        'Missed living excuse as be. Cause heard fat above first shall for. '\
        'My smiling to he removal weather on anxious.', ' ',
        'Ferrars all spirits his imagine effects amongst neither. It bachelor '\
        'cheerful of mistaken. Tore has sons put upon wife use bred seen. '\
        'Its dissimilar invitation ten has discretion unreserved. Had you '\
        'him humoured jointure ask expenses learning. Blush on in jokes '\
        'sense do do. Brother hundred he assured reached on up no. On am '\
        'nearer missed lovers. To it mother extent temper figure better.']

        story_file = open('story.txt', 'w')
        story_file.write('\n'.join(story))
        story_file.close()

    def test_wc_chars(self):
        actual = int(check_output('py solution.py chars story.txt',
            shell=True).decode())
        self.assertEqual(1032, actual)

    def test_wc_words(self):
        actual = int(check_output('py solution.py words story.txt',
            shell=True).decode())
        self.assertEqual(165, actual)

    def test_wc_lines(self):
        actual = int(check_output('py solution.py lines story.txt',
            shell=True).decode())
        self.assertEqual(5, actual)

    def tearDown(self):
        call('rm story.txt', shell=True)

if __name__ == '__main__':
    unittest.main()
