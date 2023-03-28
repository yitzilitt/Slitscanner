# This script takes a video ("input_video.mp4") as input, and outputs a video where:
# 1. The first frame is a photo which displays the
# leftmost vertical column of pixels (in the input video) as a split-scan image
# (so the output width is equal to the number of frames in the input).
# 2. The next displays the same thing, but with the column being sampled a single pixel to the right in the source...
# 3. ...and so on, all the way until the rightmost pixel column, at which point the video ends
# (so the number of frames in the output is equal to the width of the input).
import cv2
import numpy as np
from tqdm import tqdm


def slit_scan_video(input_file, output_file):
    # Open the video file
    cap = cv2.VideoCapture(input_file)

    # Check if video opened successfully
    if not cap.isOpened():
        print("Error: Could not open video file.")
        return

    # Get the total number of frames
    num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Get the video dimensions
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Initialize the array to store all columns from the video
    all_columns = np.zeros((height, num_frames, width, 3), dtype=np.uint8)

    # Process the video once and store all columns
    for frame_idx in tqdm(range(num_frames), desc="Processing input video"):
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame.")
            break

        # Store the columns from the frame
        all_columns[:, frame_idx, :, :] = frame

    # Set up the video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_file, fourcc, 30, (num_frames, height))

    # Create output frames using the stored columns
    for column in tqdm(range(width), desc="Creating output video"):
        final_frame = np.zeros((height, num_frames, 3), dtype=np.uint8)

        for frame_idx in range(num_frames):
            # Set the column index in the stored columns
            column_idx = column

            # Add the column data to the final frame
            final_frame[:, frame_idx] = all_columns[:, frame_idx, column_idx]

        # Write the frame to the output video
        out.write(final_frame)

    # Release the video capture and writer objects
    cap.release()
    out.release()

    print("Slit-scan video created successfully!")


if __name__ == "__main__":
    input_video = input("Make sure the video you want to use as your input is located in the same folder "
                        "as this script.\nEnter the complete name of the video file (e.g. 'example video.mp4'):\n")
    # replace the format "INPUT [description of video].mp4" with "OUTPUT [description of video].mp4"
    # Construct the output title using the extracted description
    output_video = "OUTPUT " + input_video

    slit_scan_video(input_video, output_video)
