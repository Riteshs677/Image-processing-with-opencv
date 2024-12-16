import cv2

img = cv2.imread("02.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.resize(img, (450, 450))

_, result = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

adaptive_result = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 5)

cv2.imshow("result", result)
cv2.imshow("original", img)
cv2.imshow("adaptive_result", adaptive_result)
cv2.waitKey(0)
cv2.destroyAllWindows()

