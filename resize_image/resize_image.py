import cv2
import numpy as np

if __name__ == '__main__':
    read_image = cv2.imread(r"C:\Users\gtush\Desktop\FAQWebp\app_related.png")
    new_resize_image = cv2.resize(read_image, (200, 200))  # Resize image
    horizontal_resize = np.hstack((new_resize_image, new_resize_image, new_resize_image))  # horizontal image
    vertical_resize = np.vstack((horizontal_resize, horizontal_resize, horizontal_resize))  # vertical image
    cv2.imshow("Resize Image", vertical_resize)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
