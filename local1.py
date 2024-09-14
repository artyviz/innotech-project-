import cv2
import mediapipe as mp
import pyttsx3

# Initialize MediaPipe Hands and TTS engine
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7)
engine = pyttsx3.init()

# Function to classify gestures (extended to more ASL letters)
def detect_asl(hand_landmarks, hand_label):
    tips = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky
    fingers = []

    # Thumb detection (same as before)
    if hand_label == "Right":
        if hand_landmarks.landmark[tips[0]].x < hand_landmarks.landmark[2].x:
            fingers.append(1)  # Thumb is open
        else:
            fingers.append(0)  # Thumb is closed
    elif hand_label == "Left":
        if hand_landmarks.landmark[tips[0]].x > hand_landmarks.landmark[2].x:
            fingers.append(1)  # Thumb is open
        else:
            fingers.append(0)  # Thumb is closed

    # Check if other fingers are open (extended)
    for tip in tips[1:]:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            fingers.append(1)  # Finger is open
        else:
            fingers.append(0)  # Finger is closed

    # Define gesture logic for various ASL letters:
    if fingers == [0, 0, 0, 0, 0]:
        return "A"  # Closed fist (A)
    elif fingers == [1, 1, 1, 1, 1]:
        return "B"  # Open palm (B)
    elif fingers == [0, 1, 1, 0, 0]:
        return "C"  # C shape (C)
    elif fingers == [0, 1, 0, 0, 0]:
        return "D"  # D: Index finger extended, others closed
    elif fingers == [1, 0, 0, 1, 1]:
        return "F"  # F: Thumb touching index finger, others extended
    elif fingers == [0, 1, 1, 1, 0]:
        return "W"  # W: Three fingers extended, thumb and pinky closed

    else:
        return "Unknown"

# Text-to-Speech function to speak detected letter
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

# Start capturing video from webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    # Convert the image color to RGB because MediaPipe uses RGB images
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the image and detect the hand landmarks
    result = hands.process(frame_rgb)

    # If hands are detected, draw the landmarks and classify the ASL letters
    if result.multi_hand_landmarks:
        for hand_landmarks, handedness in zip(result.multi_hand_landmarks, result.multi_handedness):
            # Draw the landmarks and hand connections
            mp_drawing.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get hand label (Left/Right)
            hand_label = handedness.classification[0].label

            # Detect the ASL letter
            asl_letter = detect_asl(hand_landmarks, hand_label)
            print(f"{hand_label} Hand Detected ASL Letter: {asl_letter}")

            # Display the gesture text on the frame
            cv2.putText(frame, f"{hand_label}: {asl_letter}", (50, 50 if hand_label == "Right" else 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

            # If a letter is detected, speak it out
            if asl_letter != "Unknown":
                speak_text(f"{hand_label} hand is showing {asl_letter}")

    # Display the frame
    cv2.imshow('ASL Recognition', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
