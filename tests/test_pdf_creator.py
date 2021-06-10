import unittest
from pdf_creator.creator import pdf_creator
import os


class test_pdf_creator(unittest.TestCase):

    common_size = 973
    text_size = 32290
    table_size = 32437
    image_size = 3697

    def test_save(self):
        test = pdf_creator('new.pdf')
        test.save()
        self.assertTrue(os.path.exists('new.pdf'))
        self.assertTrue((os.path.getsize('new.pdf') == self.common_size))
        os.remove('new.pdf')

    def test_table(self):
        test = pdf_creator('new.pdf')
        data = [
            ['a', 'b'],
            ['a2', 'b2']
        ]
        test.table(data, 100, 100)
        test.save()
        self.assertTrue(os.path.exists('new.pdf'))
        self.assertTrue((os.path.getsize('new.pdf') == self.table_size))
        os.remove('new.pdf')

    def test_text(self):
        test = pdf_creator('new.pdf')
        test.text('test', 100, 100)
        test.save()
        self.assertTrue(os.path.exists('new.pdf'))
        self.assertTrue((os.path.getsize('new.pdf') == self.text_size))
        os.remove('new.pdf')

    def test_image(self):
        test = pdf_creator('new.pdf')
        test.image('tests/test.jpg', 100, 100)
        test.save()
        self.assertTrue(os.path.exists('new.pdf'))
        self.assertTrue((os.path.getsize('new.pdf') == self.image_size))
        os.remove('new.pdf')
