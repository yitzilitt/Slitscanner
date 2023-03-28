# Takes a video as input (say, "input_video.mp4"), and outputs an image where a given vertical column of pixels is displayed on the left of the picture, and every column to the right (in the
# final picture) is the same location, but one frame ahead in the video.

import cv2
import numpy as np


def slit_scan(input_video, output_image, column):
    # Open the video file
    cap = cv2.VideoCapture(input_video)

    # Check if video opened successfully
    if not cap.isOpened():
        print("Error: Could not open video file.")
        return

    # Get the total number of frames
    num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Get the video dimensions
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Create an empty image with the same height and width equal to the number of frames
    final_image = np.zeros((height, num_frames, 3), dtype=np.uint8)

    # Process each frame
    for frame_idx in range(num_frames):
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame.")
            break

        # Get the specified column from the frame
        column_data = frame[:, column]

        # Add the column data to the final image
        final_image[:, frame_idx] = column_data

    # Save the final image
    cv2.imwrite(output_image, final_image)

    # Release the video capture object
    cap.release()

    print("Slit-scan image created successfully! Check the folder containing this script to find it.")


if __name__ == "__main__":
    input_video = input("Make sure the video file you want to make a slit-scan image of is located in the same folder "
                        "as this script.\nEnter the video title (e.g. 'example.mp4'):\n")
    output_image = "slitscanned " + input_video + ".png"
    column = input("Enter an integer value (e.g. '700') representing how many pixels from the left you want to use as "
                   "the 'slit' column:\n")  # Choose the column you want to use for the slit-scan effect
    intColumn = int(column)  # convert user's response to int format
    slit_scan(input_video, output_image, intColumn)  # run core code
    input("Press Enter to finish.")
