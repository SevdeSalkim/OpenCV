import cv2 

# read webcam 
webcam = cv2.VideoCapture(0)

ret = True
# visualize webcam 
while True:
    ret , frame = webcam.read()
    
    cv2.imshow('frame', frame)
    if  cv2.waitKey(40) & 0xFF == ord('q'):
        break


webcam.release()
