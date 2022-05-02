import cv2

img = cv2.imread("002.jpg", cv2.IMREAD_GRAYSCALE)

ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow("ORIGIN", img)
cv2.imshow("BINARY", th1)
cv2.imshow("BINARY_INV", th2)
cv2.imshow("TRUNC", th3)
cv2.imshow("TOZERO", th4)
cv2.imshow("TOZERO_INV", th5)
cv2.waitKey(0)