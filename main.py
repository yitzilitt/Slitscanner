# This takes every video file in a given directory, and applies the slitscan effect to them.
from SlitScanner_final import slit_scan_video
import os


directory = r'C:\Users\yitzi\Pictures\cloud slitscan stuff'

for filename in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, filename)):
        input_path = os.path.join(directory, filename)
        output_filename = f"OUTPUT_{filename}"
        output_path = os.path.join(directory, output_filename)
        slit_scan_video(input_path, output_path)
