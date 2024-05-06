import cv2
import numpy as np


def arithmetic_operations(path1, path2):
    image_1 = cv2.imread(path1)
    image_2 = cv2.imread(path2)
    resize_image_1 = cv2.resize(image_1, (500, 500))
    resize_image_2 = cv2.resize(image_2, (500, 500))
    new_add_image = cv2.addWeighted(resize_image_1, 1, resize_image_2, 1, 1)
    new_multiple_image = cv2.multiply(resize_image_1, resize_image_2)
    cv2.imshow("Add", new_add_image)
    cv2.imshow("Multiple", new_multiple_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def arithmetic_or(path1, path2):
    image_1 = cv2.imread(path1)
    image_2 = cv2.imread(path2)

    resize_image_1 = cv2.resize(image_1, (500, 500))
    resize_image_2 = cv2.resize(image_2, (500, 500))

    resultant_image = cv2.bitwise_or(resize_image_1, resize_image_2)

    image_set = np.hstack((resize_image_1, resize_image_2, resultant_image))

    cv2.imshow("OR", image_set)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    path_1 = r"C:\Users\gtush\Desktop\water_mark_image\ninja.jpg"
    path_2 = r"C:\Users\gtush\Desktop\water_mark_image\prime.jpg"
    arithmetic_or(path_1, path_2)
