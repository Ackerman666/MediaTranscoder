import subprocess
import os
import sys

def convert_rmvb_to_mp4(input_file):
    """Convert a single .rmvb file to .mp4 using ffmpeg."""
    try:
        output_file = input_file.replace('.rmvb', '.mp4')
        subprocess.run([
            'ffmpeg', '-i', input_file, 
            '-c:v', 'libx264',  # Encode video using H.264 codec
            '-c:a', 'aac',       # Encode audio using AAC codec
            '-b:a', '192k',      # Set audio bitrate to 192kbps
            output_file
        ], check=True)
        print(f"Conversion completed. MP4 file saved at: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred during conversion: {e}")
    except FileNotFoundError:
        print("ffmpeg command not found. Please make sure ffmpeg is installed and added to PATH.")

def convert_directory(directory):
    """Convert all .rmvb files in the specified directory to .mp4."""
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path) and file_path.endswith('.rmvb'):
            print(f"Converting: {file_path}")
            convert_rmvb_to_mp4(file_path)

if __name__ == "__main__":
    # Ensure the user provides at least one directory as an argument
    if len(sys.argv) < 2:
        print("Usage: python script.py <directory1> <directory2> ...")
        sys.exit(1)
    
    # Process each directory provided as an argument
    for directory in sys.argv[1:]:
        if os.path.isdir(directory):
            convert_directory(directory)
        else:
            print(f"Skipping invalid directory: {directory}")
