'''
Requirement: opencv
pip3 install opencv-contrib-python
'''
import cv2
from picamera2 import Picamera2, Preview


# Initialize camera
camera = Picamera2()
counter = 1
while True:
    camera.start()

    # Capture frame from camera and resize it
    frame = camera.capture_array()
    frame_small = cv2.resize(frame, (640, 480))
    cv2.imshow('frame', frame_small)

    key = cv2.waitKey(1)
    # Press 'q' to quit, 'p' to take a snapshot
    if key == ord('q'):
        break
    elif key == ord('p'):
        cv2.imwrite('cap-'+str(counter)+'.jpg', frame)
        print('Photo snapped.')
        counter = counter + 1
