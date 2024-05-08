import cv2
import numpy as np


def flip_images(image_path):
    # Read the image
    image = cv2.imread(image_path)
    h, w, _ = image.shape
    resize_image = cv2.resize(image, (w // 6, h // 6))
    flip_image = cv2.flip(resize_image, 1)
    images_array = np.hstack((resize_image, flip_image))
    # Show the sketch image
    cv2.imshow("Sketch Image", images_array)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    flip_images(r"C:\Users\gtush\Desktop\water_mark_image\ninja.jpg")
