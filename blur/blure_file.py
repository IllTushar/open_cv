import cv2
import numpy as np


class Blur:
    def blur_image(self, path):
        read_image = cv2.imread(path)
        resize_image = cv2.resize(read_image, (300, 300))
        gaussian_blur = cv2.GaussianBlur(resize_image, (7, 7), 0)
        median_blur = cv2.medianBlur(resize_image, 5)
        bilateral_filter = cv2.bilateralFilter(resize_image, 9, 100, 100)
        image = np.hstack((resize_image, gaussian_blur, median_blur,bilateral_filter))
        cv2.imshow("Blur Images", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == '__main__':
    blur = Blur()
    path = r"C:\Users\gtush\Desktop\water_mark_image\prime.jpg"
    blur.blur_image(path)
