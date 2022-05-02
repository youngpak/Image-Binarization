import cv2

test_image = cv2.imread("002.jpg", cv2.IMREAD_COLOR)

gray_tr01 =cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)

border01, binary01 = cv2.threshold(gray_tr01, 150, 240, cv2.THRESH_BINARY)

#cv2.imshow("Original Image", test_image)

cv2.imshow("Binary Image", binary01)

cv2.waitKey(0)
cv2.destroyAllWindows()