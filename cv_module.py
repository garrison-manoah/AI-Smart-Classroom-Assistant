import cv2
import numpy as np

# OpenCV's built-in Haar Cascade face detector.
CASCADE_PATH = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"

def detect_faces_from_image(image_bytes):
    array = np.frombuffer(image_bytes, dtype=np.uint8)
    frame = cv2.imdecode(array, cv2.IMREAD_COLOR)

    if frame is None:
        return {"count": 0, "message": "Invalid image"}

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    detector = cv2.CascadeClassifier(CASCADE_PATH)
    faces = detector.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(40, 40)
    )

    return {
        "count": len(faces),
        "message": f"Computer Vision detected {len(faces)} face(s)."
    }
