Certainly! Below is a `README.md` file that provides an overview of the script, its usage, and instructions on how to run it.

### README.md

```markdown
# Audio Splitter Script

This script splits an audio file into segments based on a provided cut list. Each segment is named according to the titles specified in the cut list.

## Features

- Supports various audio file formats: MP3, WAV, OGG, FLAC, AAC, AIFF, M4A, MP4, WMA, ALAC.
- Sanitizes titles to ensure they are safe for use as file names.
- Provides progress information during the splitting process.

## Usage

### Command Line Arguments

- `-c`, `--cutlist`: Path to the cut list file.
- `-i`, `--input`: Path to the input audio file.
- `-o`, `--output`: Path to the output folder where the segments will be saved.
- `-f`, `--format`: Format of the input audio file (e.g., mp3, wav, ogg, flac, aac, aiff, m4a, mp4, wma, alac).

### Example Command

```bash
python split_audio.py -c cutlist.txt -i input.mp3 -o output_folder -f mp3
```

### Cut List Format

The cut list file should contain lines in the following format:

```
<time_mark> <title>
```

- `<time_mark>`: Time in the format `mm:ss` (minutes:seconds).
- `<title>`: The name of the segment.

### Example Cut List

```
0:00 The_Beginning_of_an_Epic_Adventure
1:30 The_Rise_of_the_Hero's_Journey
3:45 The_Climax_of_the_Story!
```

In this example:
- The first segment is named `The_Beginning_of_an_Epic_Adventure` and starts at 0:00.
- The second segment is named `The_Rise_of_the_Hero's_Journey` and starts at 1:30.
- The third segment is named `The_Climax_of_the_Story!` and starts at 3:45.

### Notes

- The script sanitizes the titles to ensure they are safe for use as file names.
- Unsafe characters (e.g., /, \, :, *, ?, ", <, >, |, ') are replaced with underscores (_).

## Installation

### Prerequisites

- Python 3.x
- `pydub` library

### Install Dependencies

```bash
pip install pydub
```

## Running the Script

1. Ensure Python is installed and added to your system's PATH.
2. Install the required dependencies using the command above.
3. Create a cut list file in the specified format.
4. Run the script with the appropriate command line arguments.

## Example

### Cut List File (`cutlist.txt`)

```
0:00 The_Beginning_of_an_Epic_Adventure
1:30 The_Rise_of_the_Hero's_Journey
3:45 The_Climax_of_the_Story!
```

### Running the Script

```bash
python split_audio.py -c cutlist.txt -i input.mp3 -o output_folder -f mp3
```

This will split the `input.mp3` file into segments based on the cut list and save them in the `output_folder`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## Author

- [Your Name]

## Acknowledgments

- Thanks to the `pydub` library for providing the audio processing capabilities.
```

### Explanation

1. **Overview**:
   - Provides a brief description of the script and its features.

2. **Usage**:
   - Details the command line arguments and provides an example command.

3. **Cut List Format**:
   - Explains the format of the cut list file.

4. **Example Cut List**:
   - Provides an example cut list to demonstrate the format.

5. **Installation**:
   - Lists the prerequisites and installation steps.

6. **Running the Script**:
   - Provides instructions on how to run the script.

7. **Example**:
   - Includes an example cut list file and a command to run the script.

8. **License**:
   - Indicates the license under which the project is distributed.

9. **Contributing**:
   - Encourages contributions and provides instructions on how to contribute.

10. **Author**:
    - Lists the author of the script.

11. **Acknowledgments**:
    - Acknowledges the `pydub` library.

This `README.md` file should provide all the necessary information for users to understand and use the script effectively.