import cv2 as cv


def video_demo():
    capture = cv.VideoCapture(0)
    while(True):
        ret, frame = capture.read()
        frame = cv.flip(frame,1)
        cv.imshow('video',frame)
        c = cv.waitKey(50)
        if c == 27:
            break


def get_image_info(image):
    print(type(image))
    print(image.size)
    print(image.shape)
    print(image.dtype)


print('hello python')
src = cv.imread('D:/openCV/images/3.jpg')
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
get_image_info(src)
video_demo()
cv.imshow("input image", src)
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
cv.imwrite('D:/openCV/images/result.png',gray)

cv.waitKey(0)
cv.destroyAllWindows()