import cv2
import numpy as np
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
draw_color = (255, 255, 255)  # Color for drawing
erase_color = (0, 0, 0)        # Color for erasing

# Initialize webcam
cap = cv2.VideoCapture(0)

# Create a blank canvas to draw
canvas = np.zeros((480, 640, 3), dtype=np.uint8)

# Initialize previous position variables for drawing hand
prev_draw_x, prev_draw_y = 0, 0

# Initialize previous position variables for erasing hand
prev_erase_x, prev_erase_y = 0, 0

# Function to draw lines on canvas
def draw_line(canvas, start, end, color, thickness=2):
    cv2.line(canvas, start, end, color, thickness)

# Function to erase drawn areas on canvas
def erase_area(canvas, center, radius, color):
    cv2.circle(canvas, center, radius, color, -1)

# Main loop
while True:
    # Read frame from webcam
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to RGB for MediaPipe
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect hand landmarks
    results = hands.process(frame_rgb)

    # Draw landmarks and get hand positions
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            hand_landmarks = hand_landmarks.landmark
            handedness = results.multi_handedness[0].classification[0].label
            if handedness == 'Right':
                for id, lm in enumerate(hand_landmarks):
                    # Get x, y coordinates of each landmark
                    h, w, c = frame.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    if id == 8:  # Index finger tip of right hand
                        cv2.circle(frame, (cx, cy), 5, (255, 0, 0), -1)
                        if prev_draw_x != 0 and prev_draw_y != 0:
                            draw_line(canvas, (prev_draw_x, prev_draw_y), (cx, cy), draw_color)
                        prev_draw_x, prev_draw_y = cx, cy
            elif handedness == 'Left':
                for id, lm in enumerate(hand_landmarks):
                    # Get x, y coordinates of each landmark
                    h, w, c = frame.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    if id == 8:  # Index finger tip of left hand
                        cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)
                        erase_area(canvas, (cx, cy), 20, erase_color)
                    
    # Display frame and canvas
    cv2.imshow('Frame', frame)
    cv2.imshow('Canvas', canvas)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
