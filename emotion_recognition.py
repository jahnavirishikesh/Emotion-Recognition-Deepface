import cv2
from deepface import DeepFace
import time

fps_start_time = 0
fps = 0

# Load the Haar cascade classifier for face detection
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Open the video capture
cap = cv2.VideoCapture(0)

while cap.isOpened():
    # Read the video frame
    _, frame = cap.read()

    # Resize the frame for faster processing
    frame = cv2.resize(frame, (320, 240))

    # Calculate frames per second (FPS)
    fps_end_time = time.time()
    time_diff = fps_end_time - fps_start_time
    fps = 1 / time_diff
    fps_start_time = fps_end_time
    fps_text = f"FPS: {fps:.2f}"

    # Set the font for displaying FPS and emotion label
    font = cv2.FONT_HERSHEY_PLAIN

    # Convert the frame to grayscale for face detection
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    num_faces = face_detector.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)
    for (x, y, w, h) in num_faces:
        # Draw a rectangle around the detected face
        cv2.rectangle(frame, (x, y - 50), (x + w, y + h + 10), (0, 255, 0), 4)

        try:
            # Analyze the detected face for emotion using DeepFace
            analyze = DeepFace.analyze(frame, actions=['emotion'])

            # Retrieve the dominant emotion label
            dominant_emotion = analyze[0]['dominant_emotion']

            # Display the dominant emotion label on the frame
            cv2.putText(frame, dominant_emotion, (x + 5, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2,
                        cv2.LINE_AA)

            # Display the FPS on the frame
            cv2.putText(frame, fps_text, (10, 200), font, 1, (0, 0, 0), 2, cv2.LINE_AA)

            # Show the video frame with overlays
            cv2.imshow('video', frame)

        except:
            print("no face detected")
            # Exit the program when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
