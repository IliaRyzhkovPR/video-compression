import subprocess

input_file = '[path to your input video file]'
output_file = '[path to your output video file]'
log_file = '[path to your log file]'
target_size = 4 * 1024 * 1024 * 1024  # 4GB in bytes

# Get the duration of the video
probe = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', input_file],
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
duration = float(probe.stdout)
total_bitrate = (target_size * 8) / duration

# ffmpeg command to compress the video excluding the problematic stream
ffmpeg_command = [
    'ffmpeg',
    '-i', input_file,
    '-map', '0',  # Map all streams
    '-map', '-0:6',  # Exclude stream #6
    '-c:v', 'libx264',  # Video codec
    '-b:v', str(int(total_bitrate * 0.75)),  # Set video bitrate to 75% of total bitrate
    '-c:a:0', 'aac', '-b:a:0', '128k',  # First audio codec and bitrate
    '-c:a:1', 'aac', '-b:a:1', '128k',  # Second audio codec and bitrate
    '-c:s', 'mov_text',  # Subtitle codec
    '-max_muxing_queue_size', '9999',  # Prevent muxing queue overflow
    '-y',  # Overwrite output file if exists
    output_file
]

# Run the ffmpeg command and save the log to a file
with open(log_file, 'w') as log:
    subprocess.run(ffmpeg_command, stdout=log, stderr=log)
