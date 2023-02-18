import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:

    success, frame = cap.read()

    points1 = np.array([[160, 130], [350, 130], [350, 300], [160, 300] ]) # potentially the landmark of the eye outline
    # points2 = np.array([[210, 150], [300, 150], [200, 250]]) # the real postion of the eye on the screen

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #thres_gray = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)[1]  # threshold (binarize) the image


    # cv2.fillPoly(gray, [points2], (255,0,0)) # draw a triangle representing the eye 
    
    # cv2.fillPoly(thres_gray, [points2], (0,0,0)) # draw a triangle representing the eye 
    # cv2.imshow("testing frame", thres_gray)
    cv2.imshow("testing frame", gray)

    
    height, width = frame.shape[:2]
    # print(height, width) #  720, 1280
    black_frame = np.zeros((height, width), np.uint8)
    # white_frame = np.ones((height, width), np.uint8)
    # cv2.imshow("black", black_frame)
    # cv2.imshow("white", white_frame)


    mask = np.full((height, width), 255, np.uint8)
    cv2.imshow("mask before", mask)

    cv2.fillPoly(mask, [points1], (0, 0, 0))
    cv2.imshow("mask after", mask)

    # eye = cv2.bitwise_not(black_frame, thres_gray, mask=mask)
    eye = cv2.bitwise_not(black_frame, gray, mask=mask)
    # eye = cv2.bitwise_not(black_frame, frame.copy(), mask=mask)
    #eye = cv2.bitwise_not(white_frame, black_frame , mask = mask)

    cv2.imshow("eye", eye)
    #cv2.imshow("frame after", frame)


    if cv2.waitKey(1) == 27:
        break


cap.release()
cv2.destroyAllWindows()