"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2
from gaze_tracking import GazeTracking
from pynput.mouse import Controller
from pynput.mouse import Button as PynputButton
from gpiozero import Button as GPIOButton
import time as t

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)
mouse = Controller()

try:
     while True:
        # We get a new frame from the webcam
        _, frame = webcam.read()

        # We send this frame to GazeTracking to analyze it
        gaze.refresh(frame)

        frame = gaze.annotated_frame()
        text = ""

        if gaze.is_blinking():
            text = "Blinking"
            mouse.position=(960,810)
        elif gaze.is_up():
            text = "Looking up"
            mouse.position=(960,270)
        elif gaze.is_right():
            text = "Looking right"
            mouse.position=(1440,540)
        elif gaze.is_left():
            text = "Looking left"
            mouse.position=(480,540)
        elif gaze.is_center():
            text = "Looking center"
            mouse.position=(960,540)
        
        print(gaze.vertical_ratio())

        cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

        left_pupil = gaze.pupil_left_coords()
        right_pupil = gaze.pupil_right_coords()
        cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
        cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

        cv2.imshow("Demo", frame)

        if cv2.waitKey(1) == 27:
            break
           
     webcam.release()
     cv2.destroyAllWindows()

except KeyboardInterrupt:
    webcam.release()
    cv2.destroyAllWindows()
