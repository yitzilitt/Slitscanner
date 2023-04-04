# The goal here is to output a video which is exactly 1080 pixels high, and lasts for exactly 1440 frames.
# The width of the video should stay the same.
import cv2
import numpy as np


def resize_video(input_video, output_video, target_height, target_frames):
    # Open the input video
    cap = cv2.VideoCapture(input_video)

    # Get video properties
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    print("Resizing video...")

    # Calculate the new width while preserving the aspect ratio
    new_width = int(target_height * (width / height))

    # Calculate the frame indices to keep for the target number of frames
    frame_indices = np.linspace(0, total_frames - 1, num=target_frames, dtype=int)

    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video, fourcc, fps, (new_width, target_height))

    # Loop through the video, resize the frames and write to output video
    current_frame = 0
    for frame_idx in frame_indices:
        while current_frame <= frame_idx:
            ret, frame = cap.read()
            if not ret:
                break
            current_frame += 1

        if ret:
            # Resize the frame and write it to output video
            resized_frame = cv2.resize(frame, (new_width, target_height))
            out.write(resized_frame)

    # Release resources
    cap.release()
    out.release()
    cv2.destroyAllWindows()


def check_video_properties(input_vid):
    # Create a VideoCapture object to read the video file
    cap = cv2.VideoCapture(input_vid)

    # Check if the video file was successfully opened
    if not cap.isOpened():
        print("Error opening video file")

    # Get the total number of frames in the video
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    # Get the height and width of the video
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

    # Print the height and width of the video
    print("Height:", height)
    print("Width:", width)

    # Print the total number of frames in the video
    print("Total number of frames:", total_frames)

    # Release the VideoCapture object
    cap.release()


if __name__ == "__main__":
    input_video = input("Make sure the video you want to use as your input is located in the same folder "
                        "as this script.\nEnter the complete name of the video file (e.g. 'example video.mp4'):\n")
    output_video = "PREFORMATTED " + input_video
    target_height = 1080
    target_frames = 1440
    resize_video(input_video, output_video, target_height, target_frames)
    print("Done!\nOutput dimensions:")
    check_video_properties(output_video)
