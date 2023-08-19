import cv2
import pyautogui
import time

# Load the cascade for the eye
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Load the input video
cap = cv2.VideoCapture(0)

# Define the counter to keep track of the number of consecutive frames with closed eyes
counter = 0

# Define the threshold for the number of consecutive frames with closed eyes before pausing the media
threshold = 30

# Start the media
pyautogui.press('play')

while True:
    # Capture a frame from the video
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect eyes in the grayscale frame
    eyes = eye_cascade.detectMultiScale(gray, 1.1, 4)

    # Loop through the detected eyes
    for (x, y, w, h) in eyes:
        # Draw a rectangle around the eye
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Check if the eye is closed
        roi_gray = gray[y:y+h, x:x+w]
        if roi_gray.mean() < 120:
            # Increment the counter if the eye is closed
            counter += 1
            print("Closed Eye")
        else:
            # Reset the counter if the eye is open
            counter = 0
            print("Open Eye")

    # Pause the media if the counter reaches the threshold
    if counter >= threshold:
        pyautogui.press('pause')
        time.sleep(1)

    # Display the frame with the detected eyes
    cv2.imshow('Eye Detection', frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()

