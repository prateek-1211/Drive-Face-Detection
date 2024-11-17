import cv2
import mediapipe as mp
from scipy.spatial import distance
from pygame import mixer

# Initialize mixer for playing alert sound
mixer.init()
mixer.music.load("alert.mp3")

# Function to calculate Eye Aspect Ratio (EAR)
def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

# Parameters
thresh = 0.25
frame_check = 20
flag = 0

# Initialize MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Webcam capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Flip frame horizontally for mirror effect
    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # Extract eye landmarks for left and right eyes
            landmarks = face_landmarks.landmark
            left_eye = [(landmarks[i].x * w, landmarks[i].y * h) for i in [362, 385, 387, 263, 373, 380]]
            right_eye = [(landmarks[i].x * w, landmarks[i].y * h) for i in [33, 160, 158, 133, 153, 144]]

            # Calculate EAR for both eyes
            left_ear = eye_aspect_ratio(left_eye)
            right_ear = eye_aspect_ratio(right_eye)
            ear = (left_ear + right_ear) / 2.0

            # Visualize eyes with convex hull
            for point in left_eye + right_eye:
                cv2.circle(frame, (int(point[0]), int(point[1])), 2, (0, 255, 0), -1)

            # Check if EAR falls below threshold
            if ear < thresh:
                flag += 1
                if flag >= frame_check:
                    cv2.putText(frame, "****************ALERT!****************", (10, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    cv2.putText(frame, "****************ALERT!****************", (10, 325),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    mixer.music.play()
            else:
                flag = 0

    # Display the frame
    cv2.imshow("Frame", frame)

    # Quit on 'q' key press
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()