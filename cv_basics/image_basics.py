import cv2
import numpy as np

def split_image(image_path):
    img = cv2.imread(image_path)
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    height = grey.shape[0]
    width = grey.shape[1]
    print(height, width)

    row_wise_split = list()
    for i in range(0, height, 2):
        row_wise_split.append(img[i:i + 2])

    rw = np.array(row_wise_split)
    column_wise_split = list(list())

    for i in range(0, width, 2):
        column_wise_split.append(rw[0:2, i:i + 2])

    return column_wise_split

def split_image_bgr(img):
    b = img[:, :, 0]
    g = img[:, :, 1]
    r = img[:, :, 2]
    return b, g, r


def split_image_bgr_by_path(image_path):
    img = cv2.imread("foo.jpg")
    b = img[:, :, 0]
    g = img[:, :, 1]
    r = img[:, :, 2]


def resize_image(image, original, scale=1):
    width = int(original.shape[1] * scale)
    height = int(original.shape[0] * scale)
    return cv2.resize(image, (height, width))


def resize_image_by_path(image_path, original_image_path):
    img = cv2.imread(image_path, 0 )
    org = cv2.imread(original_image_path)
    return resize_image(img, org, 1)


def read_image(image_path):
    img = cv2.imread(image_path)
    return img


def read_mask_image(image_path):
    img = cv2.imread(image_path, 0)
    return img


def crop_image(image_path, h, w):
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    return img[0:h, 0:w]


def get_image_size(image_path):
    """
    :rtype: image, flattened image
    """
    # read image
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

    # get dimensions of image
    dimensions = img.shape

    # height, width, number of channels in image
    height = img.shape[0]
    width = img.shape[1]
    channels = img.shape[2]

    print('Image Dimension    : ', dimensions)
    print('Image Height       : ', height)
    print('Image Width        : ', width)
    print('Number of Channels : ', channels)
    print('total length', height * width)
    return dimensions


def get_flattened_array(image_path):
    """
    :rtype: image, flattened image
    """
    # read image
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

    # get dimensions of image
    dimensions = img.shape

    # height, width, number of channels in image
    height = img.shape[0]
    width = img.shape[1]
    channels = img.shape[2]

    print('Image Dimension    : ', dimensions)
    print('Image Height       : ', height)
    print('Image Width        : ', width)
    print('Number of Channels : ', channels)
    print('total length', height * width)
    print(img.dtype)
    pix_value = list(img)
    pix_val_flat = [x for sets in pix_value for x in sets]
    return img, pix_val_flat
