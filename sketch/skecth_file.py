import cv2
import numpy as np


def sketch_image(image_path):
    # Read the image
    image = cv2.imread(image_path)
    h, w, _ = image.shape
    resize_image = cv2.resize(image, (w//2, h//2))

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(resize_image, cv2.COLOR_BGR2GRAY)

    # Invert the grayscale image
    inverted_gray_image = 255 - gray_image

    # Apply Gaussian blur to the inverted image
    blurred_image = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)

    # Invert the blurred image
    inverted_blurred_image = 255 - blurred_image

    # Blend the inverted blurred image with the original grayscale image
    sketch_image = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)

    # Convert sketch image to pseudo-color (3 channels)
    sketch_color = cv2.cvtColor(sketch_image, cv2.COLOR_GRAY2BGR)
    flip_image = cv2.flip(sketch_color, 1)

    # Stack resized image and sketch image horizontally
    images = np.hstack((resize_image, flip_image))

    # Show the sketch image
    cv2.imshow("Sketch Image", images)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    sketch_image(r"C:\Users\gtush\Desktop\water_mark_image\prime.jpg")
