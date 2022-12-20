import cv2

img = cv2.imread(r"D:\python\pyproject\PycharmProjects\tutorial\opencv\opencv-1\img\ikun.jpg", 0)
cv2.imshow("img", img)

key = cv2.waitKey(0) & 0xFF
if key == 27:
    #cv2.destroyAllWindows()
    cv2.imwrite(r"img/ikun_0.jpg", img)