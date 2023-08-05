import pyttsx3
import PyPDF2

def pdf_to_audio(pdf_path, audio_path, voice_id):
    # Open the PDF file
    with open(pdf_path, 'rb') as pdf_file:
        # Initialize a PDF reader object
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Initialize a text-to-speech engine
        engine = pyttsx3.init()

        # Set the desired voice
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[voice_id].id)

        # Iterate over each page in the PDF
        for page_number in range(len(pdf_reader.pages)):
            # Extract the text from the current page
            page_text = pdf_reader.pages[page_number].extract_text()

            # Add the text to the speech engine
            engine.say(page_text)

        # Save the audio to a file
        engine.save_to_file('', audio_path)

        # Run the speech engine and wait for the speech to be completed
        engine.runAndWait()

# Provide the path to your PDF file, desired audio file, and voice ID
pdf_path = 'G:/PBL Project 2023/python code/book/small.pdf'
audio_path = 'G:/PBL Project 2023/python code/book/audio.mp3'
voice_id = 1  # Change the voice ID to the desired voice (0 for the default voice)

# Convert the PDF to audio using the specified voice
pdf_to_audio(pdf_path, audio_path, voice_id)
