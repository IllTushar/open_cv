import cv2

if __name__ == '__main__':
    path = r"C:\Users\gtush\Desktop\FAQWebp\images"
    image_path = path + "\\" + "Banner_1.png"
    read_image = cv2.imread(image_path)
    resize_image = cv2.resize(read_image, (500, 500))
    # normal text
    text_on_image = cv2.putText(img=resize_image, text="Edited Image", org=(50, 60), fontFace=cv2.FONT_HERSHEY_DUPLEX,
                                fontScale=1, color=(0, 0, 255), thickness=2, lineType=cv2.LINE_8, bottomLeftOrigin=False)

    # mirror text
    mirror_image = cv2.putText(img=resize_image, text="Edited Image", org=(50, 80), fontFace=cv2.FONT_HERSHEY_DUPLEX,
                                fontScale=1, color=(250, 0, 255), thickness=2, lineType=cv2.LINE_8,
                                bottomLeftOrigin=True)
    cv2.imshow("Tushar Image", mirror_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
