import unittest
from cv_basics import image_basics


class TestImageBasics(unittest.TestCase):
    def test_image_size(self):
        a, b = image_basics.get_flattened_array(r'../data/20190116_143516.jpg')
        print(a[0:5, 0:5])
        for i in range(0, 5):
            for j in range(0, 5):
                print(b[i * j + j])
        self.assertEqual(len(b), 15872256)

    def test_resize_image(self):
        img = image_basics.resize_image_by_path(r'../data/savedMasks/animals_nature_life_221468-mask.png',
                                        r'../data/Originals/animals_nature_life_221468.jpg')
        self.assertEqual(1, True)


if __name__ == '__main__':
    unittest.main()
