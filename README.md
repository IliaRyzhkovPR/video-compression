# Video Compression Script

This Python script compresses an MKV video file to an MP4 format while preserving embedded subtitles and audio tracks. It uses `ffmpeg` to perform the compression and saves the log information to a specified text file.

## Prerequisites

- Python 3.x
- `ffmpeg` installed on your system
- `ffprobe` installed on your system

## Installation
### Install `ffmpeg` and `ffprobe` on your system. For macOS, you can use Homebrew:
   ```sh
   brew install ffmpeg
   ```
## Usage
#### Update the script with the paths to your input video file, output video file, and log file.

#### Run the script.

#### The script can be found in here:

[Video Compression Script](https://github.com/IliaRyzhkovPR/video-compression/blob/main/compress-video.py)

## Explanation
1. Calculate Duration and Bitrate:

- The script first calculates the duration of the input video using ffprobe.
- It then determines the total bitrate needed to compress the video to the target size of 4GB.

2. ffmpeg Command:

- The script constructs an ffmpeg command to compress the video.
- It maps all streams from the input file, excludes the problematic stream #6, and sets the video codec to libx264.
- The video bitrate is set to 75% of the calculated total bitrate.
- Audio tracks are encoded using the aac codec at 128k bitrate.
- Subtitles are encoded using the mov_text codec.
- The -max_muxing_queue_size option is set to prevent muxing queue overflow.
- The -y option is used to overwrite the output file if it already exists.

3. Run the Command:

- The ffmpeg command is executed, and the log output is saved to the specified log file.
## Logs
- The script saves detailed log information to the specified log file. This log can be reviewed to troubleshoot any issues that may arise during the compression process.
## Notes
- Adjust the audio bitrate if higher audio quality is needed.
