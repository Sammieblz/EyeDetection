# EyeDetection
Python code that detects when an eye blinks and performs a play/pause action. This is going to be part of a bigger project.
This code is a Python script that uses the OpenCV library to detect closed eyes in real-time video frames from your webcam. It then interacts with the PyAutoGUI library to control media playback based on the detection of closed eyes.

Here's a step-by-step explanation of the code:

1. **Import Libraries:**
   - `cv2`: This is the OpenCV library, used for computer vision tasks.
   - `pyautogui`: This library is used for simulating keyboard and mouse inputs.
   - `time`: This library provides functions for time-related tasks.

2. **Load Cascade Classifier:**
   The code loads a pre-trained Haar Cascade classifier for detecting eyes from the 'haarcascade_eye.xml' file. Haar Cascades are used for object detection, and in this case, they help detect eyes in the video frames.

3. **Load Video Capture:**
   The code initializes the webcam capture using `cv2.VideoCapture(0)` to capture frames from the default camera (index 0).

4. **Variables:**
   - `counter`: This variable keeps track of the number of consecutive frames with closed eyes.
   - `threshold`: This is the number of consecutive frames with closed eyes required before pausing the media.
   
5. **Start Media Playback:**
   The script sends a 'play' command using `pyautogui.press('play')` to start the media playback.

6. **Main Loop:**
   The main loop iterates infinitely, capturing frames from the webcam in each iteration.

7. **Preprocessing:**
   - The captured frame is converted to grayscale using `cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)` to simplify processing.
   
8. **Eye Detection:**
   - The Haar Cascade classifier is used to detect eyes in the grayscale frame using `eye_cascade.detectMultiScale()`.
   - Detected eyes are stored as rectangles with their (x, y) coordinates and width and height (w, h) in the `eyes` array.
   
9. **Eye Status Classification:**
   - The code iterates through the detected eyes and draws a blue rectangle around each eye.
   - For each detected eye, a region of interest (ROI) is extracted from the grayscale frame using the eye's coordinates.
   - The average pixel intensity (mean) of the ROI is calculated. If it's below a threshold (120 in this case), the eye is classified as closed; otherwise, it's classified as open.
   
10. **Counter and Playback Control:**
    - If a closed eye is detected, the `counter` is incremented, and "Closed Eye" is printed.
    - If an open eye is detected, the `counter` is reset, and "Open Eye" is printed.
    - If the `counter` reaches the defined `threshold`, media playback is paused using `pyautogui.press('pause')`, and there's a 1-second pause using `time.sleep(1)` to prevent rapid toggling.
    
11. **Display Frame:**
    The current frame with detected eyes (drawn rectangles) is displayed using `cv2.imshow()`.

12. **Exit Condition:**
    The loop continues until the user presses the 'q' key. Upon pressing 'q', the loop breaks, and the script releases the video capture and closes all OpenCV windows.

This code essentially detects closed eyes using the Haar Cascade classifier, tracks consecutive frames with closed eyes, and controls media playback using the PyAutoGUI library. Note that the accuracy of eye detection might vary based on lighting conditions, head orientation, and the quality of the camera feed.
