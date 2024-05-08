import cv2
import numpy as np


def rotation_image(path):
    read_image = cv2.imread(path)
    resize_image = cv2.resize(read_image, (500, 500))
    w, h = resize_image.shape[0], resize_image.shape[1]
    rotated_image = cv2.getRotationMatrix2D((w / 2, h / 2), 180, 1)
    new_image = cv2.warpAffine(resize_image, rotated_image, (h, w))
    v = np.hstack((resize_image, new_image))
    cv2.imshow("Image Rotation", v)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    path = r"C:\Users\gtush\Desktop\water_mark_image\ninja.jpg"
    rotation_image(path)
