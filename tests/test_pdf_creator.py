import unittest
from pdf_creator.creator import pdf_creator
import os


def binary_check(fpath: str, spath: str):
    nm = 0
    first = open(fpath, 'rb')
    second = open(spath, 'rb')
    fst = (string for string in first)
    snd = (string for string in second)
    fst.close()
    snd.close()
    for i in fst:
        for j in snd:
            if i != j:
                nm += 1
        break
    if nm > 2:
        return False
    return True


class test_pdf_creator(unittest.TestCase):

    common_size = 973
    text_size = 32290
    table_size = 32437
    image_size = 3697

    def test_save(self):
        test = pdf_creator('tests/save.pdf')
        test.save()
        self.assertTrue(os.path.exists('tests/save.pdf'))
        self.assertTrue((os.path.getsize('tests/save.pdf') == self.common_size))
        self.assertTrue(binary_check('tests/save.pdf', 'tests/pdfs/save.pdf'))
        os.remove('tests/save.pdf')

    def test_table(self):
        test = pdf_creator('tests/table.pdf')
        data = [
            ['a', 'b'],
            ['a2', 'b2']
        ]
        test.table(data, 100, 100)
        test.save()
        self.assertTrue(os.path.exists('tests/table.pdf'))
        self.assertTrue((os.path.getsize('tests/table.pdf') == self.table_size))
        self.assertTrue(binary_check('tests/table.pdf', 'tests/pdfs/table.pdf'))
        os.remove('tests/table.pdf')

    def test_text(self):
        test = pdf_creator('tests/text.pdf')
        test.text('test', 100, 100)
        test.save()
        self.assertTrue(os.path.exists('tests/text.pdf'))
        self.assertTrue((os.path.getsize('tests/text.pdf') == self.text_size))
        self.assertTrue(binary_check('tests/text.pdf', 'tests/pdfs/text.pdf'))
        os.remove('tests/text.pdf')

    def test_image(self):
        test = pdf_creator('tests/image.pdf')
        test.image('tests/test.jpg', 100, 100)
        test.save()
        self.assertTrue(os.path.exists('tests/image.pdf'))
        self.assertTrue((os.path.getsize('tests/image.pdf') == self.image_size))
        self.assertTrue(binary_check('tests/image.pdf', 'tests/pdfs/image.pdf'))
        os.remove('tests/image.pdf')

