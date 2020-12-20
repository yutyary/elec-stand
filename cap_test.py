import cv2

# VideoCapture オブジェクトを取得します
capture = cv2.VideoCapture(0)

ret, frame = capture.read()
# resize the window
windowsize = (800, 600)
frame = cv2.resize(frame, windowsize)

cv2.imwrite('test.png', frame) 

capture.release()
cv2.destroyAllWindows()
