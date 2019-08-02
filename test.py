import cv2 as cv

print('hello python')
src = cv.imread('D:/opencv-study/images/1.png')
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)

cv.waitKey(0)
cv.destroyAllWindows()