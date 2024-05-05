import cv2

if __name__ == '__main__':
    read_img = cv2.imread(r"C:\Users\gtush\Desktop\FAQWebp\app_related.png")
    cv2.imshow("Tushar Image", read_img)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()
