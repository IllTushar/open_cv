import cv2
import numpy as np


def find_edges(path):
    read_image = cv2.imread(path)
    resize_image = cv2.resize(read_image, (450, 450))

    edges = cv2.Canny(resize_image, 150, 50, apertureSize=5, L2gradient=True)
    # Convert the grayscale edge image to a BGR color image
    edges_bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    image_array = np.hstack((resize_image, edges_bgr))

    cv2.imshow("Edges", image_array)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    path = r"C:\Users\gtush\Desktop\water_mark_image\ninja.jpg"
    find_edges(path)
