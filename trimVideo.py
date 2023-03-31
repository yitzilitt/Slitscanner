# Resizes a video to 1080 pixels in height and extracts 1920 frames from the input video (for 1920 x 1080 slitscan)
import cv2

input_video = input("Enter the video title (e.g. 'example.mp4'):\n")
output_video = "TRIMMED " + input_video
desired_pixel_height = 1080
start_frame = 1  # Change this value to choose where to start extracting frames
frames_to_extract = 1080

# Open the input video
cap = cv2.VideoCapture(input_video)

# Get the original video properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Calculate the new width to maintain the aspect ratio
new_width = int((desired_pixel_height / height) * width)

# Set up the video writer
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(output_video, fourcc, fps, (new_width, desired_pixel_height))

# Set the starting frame
cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

# Read and process frames
for _ in range(frames_to_extract):
    ret, frame = cap.read()

    if not ret:
        break

    # Resize the frame
    resized_frame = cv2.resize(frame, (new_width, desired_pixel_height))

    # Write the frame to the output video
    out.write(resized_frame)

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()
