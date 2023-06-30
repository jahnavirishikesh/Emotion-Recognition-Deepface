# Emotion Recognition with DeepFace

This program utilizes the DeepFace library to perform real-time emotion recognition from webcam video feed.

## Features

- Detects faces in the webcam video feed using the Haar cascade classifier.
- Analyzes the detected faces using DeepFace to determine the dominant emotion.
- Displays the bounding box around the detected face and the corresponding dominant emotion label in real-time.
- Calculates and displays the frames per second (FPS) of the video feed.

## Requirements

- Python 3.x
- OpenCV (`pip install opencv-python`)
- DeepFace (`pip install deepface`)

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/jahnavirishikesh/Emotion-Recognition-Deepface.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Emotion-Recognition-Deepface
   ```

3. Run the program:

   ```bash
   python emotion_recognition.py
   ```

4. A new window will open displaying the webcam video feed with the emotion recognition overlay.

5. Press 'q' to quit the program.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

This program utilizes the DeepFace library developed by [Rıza Alp Güler](https://www.linkedin.com/in/rizaalpguler/) and the Haar cascade classifier provided by OpenCV.

Enjoy emotion recognition with DeepFace!
