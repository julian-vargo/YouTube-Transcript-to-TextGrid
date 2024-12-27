# Welcome to the youtube_to_textgrid.py script! 

# Vargo, Julian (2024). Youtube Transcript to TextGrid Converter [Python Script].
# Department of Spanish & Portuguese. University of California, Berkeley.

# REQUIREMENTS:
    # Req 1) A .txt file in the format below. You can get this by opening a youtube video and copy-pasting the transcript into NotePad or TextEdit and saving it as a .txt
        # 00:00
        # Hello my name is Julian Vargo
        # 00:02
        # and I'm a linguist
    # Req 2) A .wav file of the audio from the YouTube video that is greater than or equal to the duration of the transcript

# STEPS:
# Copy and paste file paths for input_txt_path, audio_file_path into the script below.
# Write up a desired output path. The script will be writing up a new file for you, so you get to decide where it goes and what it's called.
# Save your script
# Run the script in your python environment
# Open the output .TextGrid file in Praat with your .wav file!

# USAGE:
# This script takes a transcript from a YouTube video and a .wav file and creates a .TextGrid file that can be used in Praat.
# Any irregularities in the transcript will need to be cleaned up.
# The output TextGrids are set up for usage in a forced aligner for bulk acoustic analysis of speech data.
# The script currently cannot handle videos over 1 hour in length or transcripts with milliseconds.

input_txt_path = r'C:\Users\julia\Downloads\coding\python_scripts\youtube_to_textgrid\rainbolt_test.txt'
audio_file_path = r'C:\Users\julia\Downloads\coding\python_scripts\youtube_to_textgrid\rainbolt_test.wav'
output_textgrid_path = r'C:\Users\julia\Downloads\coding\python_scripts\youtube_to_textgrid\output.TextGrid'

import wave

#Open the audio file and get its duration (this will be the value of the final xmax in the TextGrid file)
def get_audio_duration(audio_file):
    with wave.open(audio_file, 'r') as audio:
        frames = audio.getnframes()
        rate = audio.getframerate()
        duration = frames / float(rate)
        return duration
duration = get_audio_duration(audio_file_path)

#Convert Minutes:Seconds to seconds (Note that youtube transcripts don't have milliseconds. One limitation is that videos over 1 hour break this function)
def timestamp_to_seconds(timestamp):
    minutes, seconds = map(int, timestamp.split(":"))
    return minutes * 60 + seconds

#Read the transcript file
with open(input_txt_path, 'r') as file:
    content = file.read()

#Extract odd and even lines. Odd lines represent timestamps, even lines represent phrases
lines = content.splitlines()
odd_lines = [line for i, line in enumerate(lines) if line and i % 2 == 0]
even_lines = [line for i, line in enumerate(lines) if line and i % 2 != 0]

#Convert odd lines (timestamps) to seconds
odd_lines_seconds = [timestamp_to_seconds(ts) for ts in odd_lines]

#Gather the number of intervals (i.e. the number of timestamps)
num_intervals = len(odd_lines_seconds)

#Write the actual formatted TextGrid file
with open(output_textgrid_path, 'w') as file:
    file.write('File type = "ooTextFile"\n')
    file.write('Object class = "TextGrid"\n\n')
    file.write('xmin = 0\n')
    file.write(f'xmax = {duration:.6f}\n')
    file.write('tiers? <exists>\n')
    file.write('size = 1\n')
    file.write('item []:\n')
    file.write('\titem [1]:\n')
    file.write('\t\tclass = "IntervalTier"\n')
    file.write('\t\tname = "phrases"\n')
    file.write('\t\txmin = 0\n')
    file.write(f'\t\txmax = {duration:.6f}\n')
    file.write(f'\t\tintervals: size = {num_intervals}\n')
    for i in range(num_intervals):
        file.write(f'\t\tintervals [{i+1}]:\n')
        file.write(f'\t\t\txmin = {odd_lines_seconds[i]:.6f}\n')
        if i + 1 < len(odd_lines_seconds):
            file.write(f'\t\t\txmax = {odd_lines_seconds[i+1]:.6f}\n')
        else:
            file.write(f'\t\t\txmax = {duration:.6f}\n')
        file.write(f'\t\t\ttext = "{even_lines[i]}"\n')
