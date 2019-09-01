import cv2,time,pandas
from datetime import datetime

class Camera:
    def start_capture(self,sensitivity):
        first_frame = None
        motion_list = [None,None] # Stores values for motion and no motion
        motion_times = [] # Stores times where each object entered and exited the frame
        df = pandas.DataFrame(columns=["Start","End"])
        video = cv2.VideoCapture(0)
        while True:
            motion = 0
            check, frame = video.read()
            gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # Creates a grayscale version of the video frame
            gray_frame = cv2.GaussianBlur(gray_frame,(21,21),0) # Blurs the frame for better accuracy in motion detection

            if first_frame is None:
                first_frame = gray_frame
                continue

            delta_frame = cv2.absdiff(first_frame,gray_frame) # Difference between first frame and current frame

            thresh_frame = cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1] # Stores the threshold frame from delta_frame

            (cnts,_) = cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) # Stores the contours from thresh_frame

            for c in cnts:
                if cv2.contourArea(c) < sensitivity: # Checks if the motion was greater than a certain amount
                    continue
                else:
                    motion = 1
                    (x,y,w,h) = cv2.boundingRect(c) # stores dimensions for rectangle around moving object
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3) # draws the rectangle on the displayed video
            motion_list += [motion]
            if motion_list[-1] == 1 and motion_list[-2] == 0: # Motion to No Motion
                motion_times += [datetime.now().time().strftime('%H:%M:%S')]
            if motion_list[-1] == 0 and motion_list[-2] == 1: # No Motion to Motion
                motion_times += [datetime.now().time().strftime('%H:%M:%S')]
            cv2.imshow('Motion Detection Alarm',frame)

            key_press = cv2.waitKey(1)
            if key_press ==ord('q'):
                if motion == 1: # Adds the time for last object if application was quit
                    motion_times += [datetime.now()]
                break

        for i in range(0,len(motion_times),2):
            df=df.append({"Start":motion_times[i],"End":motion_times[i+1]},ignore_index=True)
        df.to_csv("Times.csv")

        video.release()
        cv2.destroyAllWindows()

cam = Camera()
cam.start_capture(10000)
