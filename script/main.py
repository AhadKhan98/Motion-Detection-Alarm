from webcam import Camera

def main():
    print("Welcome to the Motion Detection Alarm. \nHow sensitive do you want the motion detection? (1=Low, 2=Med, 3=High)")

    while True:
        try:
            sensitivity = int(input("Enter Sensitivity: "))
            break
        except:
            print("Please enter a valid number. (1=Low, 2=Med, 3=High)")

    print("\nMotion detection starting. Press 'q' on the camera screen to exit the video..")
    video = Camera()
    if sensitivity == 1: video.start_capture(20000)
    if sensitivity == 2: video.start_capture(15000)
    if sensitivity == 3: video.start_capture(10000)

if __name__=="__main__":
    main()
