# This takes every video file in a given directory and applies the slitscan effect to them.
from SlitScanner_final import slit_scan_video
from trim_video import resize_video
import os

print("This script takes a given folder as input, and for each .mp4 file inside, outputs a 1440x1080px slit-scanned "
      "video. The length of the output vid depends on the width of the input video.")


# Accepts a user-input file path and normalizes it to work on both Mac and Windows systems
def get_directory_input(prompt):
    while True:
        directory = input(prompt)
        if directory.startswith(("'", '"')) and directory.endswith(("'", '"')):
            return directory[1:-1]
        elif " " in directory or "\\" in directory or "/" in directory:
            return directory
        else:
            print("Please make sure to include the full path, with either forward slashes or backslashes.")


directory = get_directory_input(
    "Paste the full path to a folder which contains the input video(s) which you wish to "
    "apply the effect to (e.g. 'C:\\Users\\Bob\\Desktop\\example folder' on Windows or "
    "'/home/Bob/Desktop/example folder' on Mac). Make sure it's only videos in the folder, and to enclose the path you give in quotes, if you are running this via terminal on Mac or Linux (this shouldn't be necessary on Windows):" + "\n"
)

# Convert user input path to a platform-independent format
directory = os.path.normpath(directory)

for filename in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, filename)):
        input_path = os.path.join(directory, filename)
        output_filename = "OUTPUT_{}".format(filename)
        output_path = os.path.join(directory, output_filename)
        target_height = 1080
        target_frames = 1440
        resize_video(input_path, output_path, target_height, target_frames)
        slit_scan_video(output_path, output_path)
        print("Finished! Check your folder to see the output video(s).")
