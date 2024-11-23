"""
This script splits an MP3 file into segments based on a provided cut list.
Each segment is named according to the titles specified in the cut list.

Usage:
    python split_mp3.py -c cutlist.txt -i input.mp3 -o output_folder

Arguments:
    -c, --cutlist: Path to the cut list file.
    -i, --input: Path to the input MP3 file.
    -o, --output: Path to the output folder where the segments will be saved.

Cut List Format:
    The cut list file should contain lines in the following format:
    <time_mark> <title>
    - <time_mark>: Time in the format 'mm:ss' (minutes:seconds).
    - <title>: The name of the segment.

Example Cut List:
    0:00 The_Beginning_of_an_Epic_Adventure
    1:30 The_Rise_of_the_Hero's_Journey
    3:45 The_Climax_of_the_Story!

In this example:
- The first segment is named 'The_Beginning_of_an_Epic_Adventure' and starts at 0:00.
- The second segment is named 'The_Rise_of_the_Hero's_Journey' and starts at 1:30.
- The third segment is named 'The_Climax_of_the_Story!' and starts at 3:45.

Note:
- The script sanitizes the titles to ensure they are safe for use as file names.
- Unsafe characters (e.g., /, \, :, *, ?, ", <, >, |, ') are replaced with underscores (_).
"""

import argparse
from pydub import AudioSegment
import os
import re

def parse_cut_list(file_path):
    cut_list = []
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()  # Remove leading/trailing whitespace
            if not line:  # Skip empty lines
                continue
            parts = line.split(' ', 1)
            if len(parts) != 2:
                print(f"Error: Line {line_number} in cut list file is not in the correct format.")
                print(f"Line: '{line}'")
                continue
            time_mark, title = parts
            try:
                minutes, seconds = map(int, time_mark.split(':'))
                time_in_ms = (minutes * 60 + seconds) * 1000
                cut_list.append((time_in_ms, title))
            except ValueError:
                print(f"Error: Invalid time mark format on line {line_number}.")
                print(f"Line: '{line}'")
    return cut_list

def sanitize_filename(filename):
    # Replace or remove characters that are not allowed in file names
    sanitized = re.sub(r'[<>:"/\\|?*\'`]', '_', filename)
    return sanitized

def format_time(milliseconds):
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    return f"{minutes:02}:{seconds:02}"

def split_mp3(input_file, cut_list, output_folder):
    audio = AudioSegment.from_mp3(input_file)
    os.makedirs(output_folder, exist_ok=True)

    for i in range(len(cut_list) - 1):
        start_time = cut_list[i][0]
        end_time = cut_list[i + 1][0]
        title = cut_list[i][1]
        sanitized_title = sanitize_filename(title)
        segment = audio[start_time:end_time]
        output_file = os.path.join(output_folder, f"{sanitized_title}.mp3")
        
        # Print progress information
        start_time_str = format_time(start_time)
        end_time_str = format_time(end_time)
        print(f"Extracting '{title}' from {start_time_str} to {end_time_str}...")
        
        segment.export(output_file, format="mp3")
        print(f"Saved {output_file}")

    # Handle the last segment
    last_start_time = cut_list[-1][0]
    last_title = cut_list[-1][1]
    sanitized_last_title = sanitize_filename(last_title)
    last_segment = audio[last_start_time:]
    last_output_file = os.path.join(output_folder, f"{sanitized_last_title}.mp3")
    
    # Print progress information for the last segment
    start_time_str = format_time(last_start_time)
    print(f"Extracting '{last_title}' from {start_time_str} to end...")
    
    last_segment.export(last_output_file, format="mp3")
    print(f"Saved {last_output_file}")

def main():
    parser = argparse.ArgumentParser(description="Split an MP3 file at specified time marks.")
    parser.add_argument('-c', '--cutlist', required=True, help='Path to the cut list file')
    parser.add_argument('-i', '--input', required=True, help='Path to the input MP3 file')
    parser.add_argument('-o', '--output', required=True, help='Path to the output folder')

    args = parser.parse_args()

    cut_list = parse_cut_list(args.cutlist)
    split_mp3(args.input, cut_list, args.output)

if __name__ == "__main__":
    main()