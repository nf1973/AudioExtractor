import sys
import os
from pydub import AudioSegment

def convert_mp4_to_mp3(mp4_file):
    """
    Converts the audio from an MP4 file to MP3 format without loss of quality.
    
    Args:
        mp4_file (str): Path to the input MP4 file.
    """
    try:
        # Check if the input file exists
        if not os.path.isfile(mp4_file):
            print(f"Error: The file '{mp4_file}' does not exist.")
            return
        
        # Derive the output file path with the same name but .mp3 extension
        output_file = os.path.splitext(mp4_file)[0] + ".mp3"

        # Load the MP4 file
        audio = AudioSegment.from_file(mp4_file, format="mp4")
        
        # Export as MP3
        audio.export(output_file, format="mp3", parameters=["-q:a", "0"])  # -q:a 0 ensures maximum quality
        print(f"Successfully converted '{mp4_file}' to '{output_file}'.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Ensure a filename is passed as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python mp4_to_mp3.py <path_to_mp4_file>")
        sys.exit(1)
    
    input_mp4 = sys.argv[1]  # Get the input filename from command-line argument
    convert_mp4_to_mp3(input_mp4)
