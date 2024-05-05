import cv2

if __name__ == '__main__':
    read_image = cv2.imread(r"C:\Users\gtush\Desktop\FAQWebp\images\Banner_1.png", 1)
    resize_image = cv2.resize(read_image, (500, 500))
    cv2.imshow("Tushar Image", resize_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(read_image.shape)
