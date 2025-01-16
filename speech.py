import speech_recognition as sr

# Create a Recognizer instance
recognizer = sr.Recognizer()

# Define the path to the audio file
audio_file_path = "C:\\Users\\santhosh saravanan\\Downloads\\harvard.wav"  # Change to the actual file name

try:
    # Open the audio file for processing
    with sr.AudioFile(audio_file_path) as source:
        print("Reading the audio file...")
        audio_data = recognizer.record(source)  # Capture the entire content of the audio file
        
        # Use Google's speech recognition API to transcribe the audio
        transcription = recognizer.recognize_google(audio_data)
        print("\nTranscription Result:\n", transcription)
except FileNotFoundError:
    print(f"Error: The file at '{audio_file_path}' was not found.")
except sr.UnknownValueError:
    print("Error: Unable to understand the audio content.")
except sr.RequestError as error:
    print(f"Error: Unable to process the request due to {error}.")
