import unittest
from cv_basics import image_inpainting
from cv_basics import image_basics

class TestInpaintImages(unittest.TestCase):
    def test_image_inpaint(self):
        org = r'D:\pics for Inpainttool\Originals\110.jpg'
        masked = r'D:\pics for Inpainttool\Masked Pics\110.jpg'
        final = r'D:\pics for Inpainttool\final\110.jpg'
        inpaint = r'D:\pics for Inpainttool\Inpaint Pics\110.jpg'
        new_mask = image_basics.resize_image_by_path(masked, org)
        new_org = image_basics.read_image(org)
        new_inpaint = image_basics.read_image(inpaint)
        inpaint_generated = image_inpainting.inpaint_image(new_org, new_mask, final)
        self.assertEqual(new_inpaint, inpaint_generated)


if __name__ == '__main__':
    unittest.main()
