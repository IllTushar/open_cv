import cv2


def draw_rect_angle(image_path):
    old_image = cv2.imread(image_path)
    old_resize_image = cv2.resize(old_image, (1000, 600))
    label = cv2.putText(old_resize_image, text="SayaCare ka admi", org=(650, 40), fontFace=cv2.FONT_HERSHEY_DUPLEX,
                        fontScale=1, color=(0, 255, 0), thickness=1, lineType=cv2.LINE_8, bottomLeftOrigin=False)
    new_image = cv2.rectangle(label, pt1=(850, 45), pt2=(650, 500), color=(0, 275, 0), thickness=4,
                              lineType=16)
    cv2.imshow("Tushar", new_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    path = r"C:\Users\gtush\Desktop\water_mark_image\output_image.png"
    draw_rect_angle(path)
