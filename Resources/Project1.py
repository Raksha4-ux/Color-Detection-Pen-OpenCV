# # # import cv2
# # # import numpy as np
# # #
# # # frameWidth = 640
# # # frameHeight = 480
# # # cap = cv2.VideoCapture(0)   # changed to 0 for default camera
# # # cap.set(3, frameWidth)
# # # cap.set(4, frameHeight)
# # # cap.set(10, 150)
# # #
# # # # ==== CUSTOM COLORS (in HSV) ====
# # # # [Hue_min, Sat_min, Val_min, Hue_max, Sat_max, Val_max]
# # # myColors = [
# # #     [56, 13, 11, 76, 93, 91],     # Green
# # #     [0, 19, 39, 18, 99, 119],     # Orange
# # #     [166, 4, 21, 179, 84, 101]    # Pink
# # # ]
# # #
# # # # ==== DRAWING COLORS (BGR values for display) ====
# # # myColorValues = [
# # #     [0, 255, 0],        # Green
# # #     [0, 165, 255],      # Orange
# # #     [203, 192, 255]     # Pink
# # # ]
# # #
# # # myPoints = []  # [x, y, colorId]
# # #
# # #
# # # # ---------------------------------------------------------
# # # def findColor(img, myColors, myColorValues):
# # #     imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# # #     count = 0
# # #     newPoints = []
# # #
# # #     for color in myColors:
# # #         lower = np.array(color[0:3])
# # #         upper = np.array(color[3:6])
# # #         mask = cv2.inRange(imgHSV, lower, upper)
# # #         x, y = getContours(mask)
# # #         cv2.circle(imgResult, (x, y), 15, myColorValues[count], cv2.FILLED)
# # #         if x != 0 and y != 0:
# # #             newPoints.append([x, y, count])
# # #         count += 1
# # #         # Uncomment below to view individual color masks
# # #         # cv2.imshow(str(color[0]), mask)
# # #     return newPoints
# # #
# # #
# # # # ---------------------------------------------------------
# # # def getContours(img):
# # #     contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# # #     x, y, w, h = 0, 0, 0, 0
# # #     for cnt in contours:
# # #         area = cv2.contourArea(cnt)
# # #         if area > 500:
# # #             peri = cv2.arcLength(cnt, True)
# # #             approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
# # #             x, y, w, h = cv2.boundingRect(approx)
# # #     return x + w // 2, y
# # #
# # #
# # # # ---------------------------------------------------------
# # # def drawOnCanvas(myPoints, myColorValues):
# # #     for point in myPoints:
# # #         cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)
# # #
# # #
# # # # ---------------------------------------------------------
# # # while True:
# # #     success, img = cap.read()
# # #     if not success:
# # #         print("Failed to read from camera.")
# # #         break
# # #
# # #     imgResult = img.copy()
# # #     newPoints = findColor(img, myColors, myColorValues)
# # #
# # #     if len(newPoints) != 0:
# # #         for newP in newPoints:
# # #             myPoints.append(newP)
# # #
# # #     if len(myPoints) != 0:
# # #         drawOnCanvas(myPoints, myColorValues)
# # #
# # #     cv2.imshow("Result", imgResult)
# # #     if cv2.waitKey(1) & 0xFF == ord('q'):
# # #         break
# # #
# # # cap.release()
# # # cv2.destroyAllWindows()
# # import cv2
# # import numpy as np
# #
# # frameWidth = 640
# # frameHeight = 480
# # cap = cv2.VideoCapture(0)   # default camera
# # cap.set(3, frameWidth)
# # cap.set(4, frameHeight)
# # cap.set(10, 150)
# #
# # # ==== CUSTOM COLORS (HSV ranges) ====
# # # [Hue_min, Sat_min, Val_min, Hue_max, Sat_max, Val_max]
# # myColors = [
# #     [56, 13, 11, 76, 93, 91],     # Green
# #     [166, 4, 21, 179, 84, 101]    # Pink
# # ]
# #
# # # ==== DRAWING COLORS (BGR) ====
# # myColorValues = [
# #     [60, 129, 75],        # Green
# #     [203, 192, 255]     # Pink
# # ]
# #
# # myPoints = []  # [x, y, colorId]
# #
# #
# # # ---------------------------------------------------------
# # def findColor(img, myColors, myColorValues):
# #     imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# #     count = 0
# #     newPoints = []
# #
# #     for color in myColors:
# #         lower = np.array(color[0:3])
# #         upper = np.array(color[3:6])
# #         mask = cv2.inRange(imgHSV, lower, upper)
# #         x, y = getContours(mask)
# #         cv2.circle(imgResult, (x, y), 10, myColorValues[count], cv2.FILLED)
# #         if x != 0 and y != 0:
# #             newPoints.append([x, y, count])
# #         count += 1
# #     return newPoints
# #
# #
# # # ---------------------------------------------------------
# # def getContours(img):
# #     contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# #     x, y, w, h = 0, 0, 0, 0
# #     for cnt in contours:
# #         area = cv2.contourArea(cnt)
# #         if area > 500:
# #             peri = cv2.arcLength(cnt, True)
# #             approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
# #             x, y, w, h = cv2.boundingRect(approx)
# #     return x + w // 2, y
# #
# #
# # # ---------------------------------------------------------
# # def drawOnCanvas(myPoints, myColorValues):
# #     for point in myPoints:
# #         cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)
# #
# #
# # # ---------------------------------------------------------
# # while True:
# #     success, img = cap.read()
# #     if not success:
# #         print("Failed to read from camera.")
# #         break
# #
# #     imgResult = img.copy()
# #     newPoints = findColor(img, myColors, myColorValues)
# #
# #     if len(newPoints) != 0:
# #         for newP in newPoints:
# #             myPoints.append(newP)
# #
# #     if len(myPoints) != 0:
# #         drawOnCanvas(myPoints, myColorValues)
# #
# #     cv2.imshow("Result", imgResult)
# #     if cv2.waitKey(1) & 0xFF == ord('q'):
# #         break
# #
# # cap.release()
# # cv2.destroyAllWindows()
# #
# import cv2
# import numpy as np
#
# frameWidth = 640
# frameHeight = 480
# cap = cv2.VideoCapture(0)
# cap.set(3, frameWidth)
# cap.set(4, frameHeight)
# cap.set(10, 150)
#
# # ==== CUSTOM COLORS (HSV ranges) ====
# # [Hue_min, Sat_min, Val_min, Hue_max, Sat_max, Val_max]
# myColors = [
#     [56, 13, 11, 76, 93, 91],     # Green
#     [166, 4, 21, 179, 84, 101]    # Pink
# ]
#
# # ==== DRAWING COLORS (BGR) ====
# myColorValues = [
#     [0, 255, 0],        # Green
#     [203, 192, 255]     # Pink
# ]
#
# myPoints = []  # [x, y, colorId]
#
#
# # ---------------------------------------------------------
# def findColor(img, myColors, myColorValues):
#     imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#     count = 0
#     newPoints = []
#
#     for color in myColors:
#         lower = np.array(color[0:3])
#         upper = np.array(color[3:6])
#         mask = cv2.inRange(imgHSV, lower, upper)
#         x, y = getContours(mask)
#         if x != 0 and y != 0:
#             newPoints.append([x, y, count])
#             cv2.circle(imgResult, (x, y), 7, myColorValues[count], cv2.FILLED)
#         count += 1
#     return newPoints
#
#
# # ---------------------------------------------------------
# def getContours(img):
#     contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#     x, y, w, h = 0, 0, 0, 0
#     for cnt in contours:
#         area = cv2.contourArea(cnt)
#         if area > 500:
#             peri = cv2.arcLength(cnt, True)
#             approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
#             x, y, w, h = cv2.boundingRect(approx)
#     return x + w // 2, y
#
#
# # ---------------------------------------------------------
# def drawOnCanvas(myPoints, myColorValues):
#     # Draw continuous circles and lines between consecutive points of the same color
#     for i in range(len(myPoints)):
#         x, y, colorId = myPoints[i]
#         cv2.circle(imgResult, (x, y), 5, myColorValues[colorId], cv2.FILLED)
#
#         # Draw a line from this point to the previous point of same color
#         if i > 0 and myPoints[i][2] == myPoints[i - 1][2]:
#             prevX, prevY, _ = myPoints[i - 1]
#             cv2.line(imgResult, (prevX, prevY), (x, y), myColorValues[colorId], 3)
#
#
# # ---------------------------------------------------------
# while True:
#     success, img = cap.read()
#     if not success:
#         print("Failed to read from camera.")
#         break
#
#     imgResult = img.copy()
#     newPoints = findColor(img, myColors, myColorValues)
#
#     if len(newPoints) != 0:
#         for newP in newPoints:
#             myPoints.append(newP)
#
#     if len(myPoints) != 0:
#         drawOnCanvas(myPoints, myColorValues)
#
#     cv2.imshow("Result", imgResult)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()
import cv2
import numpy as np
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)

myColors = [[5,107,0,19,255,255],
            [133,56,0,159,156,255],
            [57,76,0,100,255,255],
            [90,48,0,118,255,255],
            [166, 4, 21, 179, 84, 101] ]
myColorValues = [[51,153,255],          ## BGR
                 [255,0,255],
                 [0,255,0],
                 [255,0,0],
                 [203, 192, 255]
                 ]

myPoints =  []  ## [x , y , colorId ]

def findColor(img,myColors,myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints=[]
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV,lower,upper)
        x,y=getContours(mask)
        cv2.circle(imgResult,(x,y),15,myColorValues[count],cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count +=1
        #cv2.imshow(str(color[0]),mask)
    return newPoints

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:
            #cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2,y

def drawOnCanvas(myPoints,myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)


while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img, myColors,myColorValues)
    if len(newPoints)!=0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints)!=0:
        drawOnCanvas(myPoints,myColorValues)


    cv2.imshow("Result", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
