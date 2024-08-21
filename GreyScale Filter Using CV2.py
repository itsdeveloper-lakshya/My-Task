import cv2

# Initialize the webcam capture
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

while True:
    # Capture each frame
    ret, frame = cap.read()

    # Check if frame is read correctly
    if not ret:
        print("Failed to grab frame.")
        break

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the grayscale video
    cv2.imshow('Grayscale Live Footage', gray_frame)

    # Press ‘q’ to exit the video stream
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close any open windows
cap.release()
cv2.destroyAllWindows()
