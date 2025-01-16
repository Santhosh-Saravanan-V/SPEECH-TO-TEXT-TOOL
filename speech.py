import speech_recognition as sr

# Creating a Recognizer for instance
recognizer = sr.Recognizer()

# Defining the path for the audio file
audio_file_path = "C:\\Users\\santhosh saravanan\\Downloads\\harvard.wav"  

try:
    # Opening the audio files for processing
    with sr.AudioFile(audio_file_path) as source:
        print("Reading the audio file...")
        audio_data = recognizer.record(source)  # Capturing the entire content of the audio file
        
        # Using the Google's speech recognition API to transcribe the audio
        transcription = recognizer.recognize_google(audio_data)
        print("\nTranscription Result:\n", transcription)
except FileNotFoundError:
    print(f"Error: The file at '{audio_file_path}' was not found.")
except sr.UnknownValueError:
    print("Error: Unable to understand the audio content.")
except sr.RequestError as error:
    print(f"Error: Unable to process the request due to {error}.")
