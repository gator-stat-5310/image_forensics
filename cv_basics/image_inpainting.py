import numpy as np
import cv2


def read_image(image_path):
    img = cv2.imread(image_path)
    return img


def read_mask_image(masked_image_path):
    img = cv2.imread(masked_image_path, 0)
    return img


def inpaint_image(original, mask, inpaint= None):
    # Inpaint.
    result = cv2.inpaint(original, mask, 3, cv2.INPAINT_NS)
    return result


def inpaint_image_path(original_path, mask_path, inpaint= None):
    # Open the image.
    img = cv2.imread(original_path)

    # Load the mask.
    mask = cv2.imread(mask_path, 0)

    # Inpaint.
    result = cv2.inpaint(img, mask, 3, cv2.INPAINT_NS)

    # Write the output.
    if inpaint is not None:
        cv2.imwrite(inpaint, result)
    return result