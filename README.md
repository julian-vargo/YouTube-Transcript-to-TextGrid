# YouTube-Transcript-to-TextGrid

**Vargo, Julian (2024). Youtube Transcript to TextGrid Converter [Python Script].**  
*Department of Spanish & Portuguese. University of California, Berkeley.*

---

## **Overview**

This script converts a YouTube transcript and its corresponding audio file into a `.TextGrid` file for use in Praat. It is particularly useful for forced alignment and bulk acoustic analysis of speech data.

---

## **Requirements**

1. **Transcript File (.txt):**  
   A `.txt` file in the format below, obtained by copying the YouTube video transcript into a plain text editor (e.g., NotePad or TextEdit) and saving it as a `.txt` file:

2. **Audio File (.wav):**  
A `.wav` file of the audio from the YouTube video. The audio duration must be **greater than or equal** to the transcript duration.

---

## **Steps**

1. Edit the script by providing:
- The file path to your input `.txt` transcript (`input_txt_path`).
- The file path to your `.wav` audio file (`audio_file_path`).
- A desired output path for the resulting `.TextGrid` file.

2. Save your changes to the script.

3. Run the script in your Python environment.

4. Open the generated `.TextGrid` file in Praat along with your `.wav` file to view and analyze the transcription.

---

## **Usage**

- This script processes the provided transcript and audio file to generate a `.TextGrid` that aligns timestamps with the transcript text.
- **Note:** Ensure the transcript is free of irregularities before running the script.
- The output `.TextGrid` is formatted for use with forced aligners and facilitates bulk acoustic analysis of speech data.

---

## **Limitations**

- The script does not support:
- Videos longer than 1 hour.
- Transcripts containing millisecond timestamps.
