import os
import cv2

if __name__ == '__main__':
    all_images = os.listdir(r"C:\Users\gtush\Desktop\FAQWebp\images")
    path = r"C:\Users\gtush\Desktop\FAQWebp\images"
    for images in all_images:
        new_image = path + "\\" + images
        read_image = cv2.imread(new_image)
        resize_new_image = cv2.resize(read_image, (200, 200))
        cv2.imshow("Tushar Images", resize_new_image)
        cv2.waitKey(1000)

    cv2.destroyAllWindows()
