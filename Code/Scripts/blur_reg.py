import cv2

# Load the video
video_path = "FP01.mkv"
cap = cv2.VideoCapture(video_path)

# Define the region to be anonymized
x, y, width, height = 50, 50, 200, 200

# Get the original video's width, height, and frames per second (fps)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Define the output video path and codec
output_path = "FP01-anonymous.mp4"
fourcc = cv2.VideoWriter_fourcc(
    *"mp4v"
)  # Adjust the codec based on the desired output video format

# Create the VideoWriter object
writer = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

# Iterate over frames
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Apply blur to the region of interest
    roi = frame[y : y + height, x : x + width]
    blurred_roi = cv2.blur(roi, (100, 100))  # Adjust the blur kernel size as desired
    frame[y : y + height, x : x + width] = blurred_roi

    # Display the resulting frame (optional)
    # cv2.imshow('Anonymized Video', frame)

    # Save the frame to the new video file
    writer.write(frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture and writer objects, and close windows
cap.release()
writer.release()
cv2.destroyAllWindows()
