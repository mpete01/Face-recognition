import cv2
import pathlib
import keyboard

cascade_path = pathlib.Path(cv2.__file__).parent.absolute() / "data/haarcascade_frontalface_default.xml"

clf = cv2.CascadeClassifier(str(cascade_path))

cam = cv2.VideoCapture(0)
while(True):
    _ , frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = clf.detectMultiScale(
        gray,
        scaleFactor = 1.1,
        minNeighbors = 5,
        minSize = (30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )

    for(x, y, width, height) in faces:
        cv2.rectangle(frame, (x, y), (x+width, y+height), (255, 255, 0), 2)

    frame = cv2.flip(frame, 1)

    cv2.imshow('Press the esc button to quit', frame)
    if cv2.waitKey(1) & 0xFF == 27: #27 corresponds to "esc" in ASCII
        break


cam.release()

cv2.destroyAllWindows()
