import cv2

# Open the video file
video_capture = cv2.VideoCapture('video output.mp4')

# Get the frames per second (fps) of the video
fps = int(video_capture.get(cv2.CAP_PROP_FPS))

# Get the width and height of the video frame
width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Create a VideoWriter object to write the output video file
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_video = cv2.VideoWriter('reversed_output.mp4', fourcc, fps, (width, height))

# Create an empty numpy array to hold the reversed frames
reversed_frames = []

# Loop through the video frames and add them to the reversed_frames array
while True:
    ret, frame = video_capture.read()
    if not ret:
        break
    reversed_frames.append(frame)

# Loop through the reversed_frames array in reverse order and write the frames to the output video
for frame in reversed(reversed_frames):
    output_video.write(frame)

# Release the video capture and writer objects
video_capture.release()
output_video.release()

