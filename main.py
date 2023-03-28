# This takes every video file in a given directory and applies the slitscan effect to them.
from SlitScanner_final import slit_scan_video
import os

# Accepts a user-input file path and normalizes it to work on both Mac and Windows systems
directory = input("Paste the full path to a folder which contains the input video(s) which you wish to "
                  "apply the effect to (e.g. 'C:\\Users\\Bob\\Desktop\\example folder' on Windows or "
                  "'/home/Bob/Desktop/example folder' on Mac; also make sure it's only videos in the folder):" + "\n")

# Convert user input path to a platform-independent format
directory = os.path.normpath(directory)

for filename in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, filename)):
        input_path = os.path.join(directory, filename)
        output_filename = f"OUTPUT_{filename}"
        output_path = os.path.join(directory, output_filename)
        slit_scan_video(input_path, output_path)
        print("Finished! Check your folder to see the output video(s).")
