import os
import whisper

def transcribe_audio(file_path):
    # Load the model; consider using "medium" if "large" is too resource-intensive
    model = whisper.load_model("large")

    # Transcribe the audio
    result = model.transcribe(file_path)
    return result['text']

if __name__ == "__main__":
    # Directory where the script and audio files are located
    directory = os.getcwd()

    # Loop through all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".mp3"):
            # Construct the full file path
            full_path = os.path.join(directory, filename)
            # Transcribe the audio file
            transcription = transcribe_audio(full_path)
            # Create a new text file for the output
            output_filename = os.path.splitext(filename)[0] + ".txt"
            output_path = os.path.join(directory, output_filename)

            # Write the transcription to the file with UTF-8 encoding
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(transcription)
            print(f"Transcribed '{filename}' to '{output_filename}'")

