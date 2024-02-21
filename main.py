from gtts import gTTS
import os
from PyPDF2 import PdfReader

def pdf_to_text(pdf_path):
    # Open the PDF file in binary mode
    with open(pdf_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PdfReader(file)
        
        # Initialize an empty string to store text
        text = ""
        
        # Iterate through each page in the PDF file
        for page_num in range(len(pdf_reader.pages)):
            # Extract text from the page and append it to the string
            text += pdf_reader.pages[page_num].extract_text()
        
    return text

def text_to_audio(text, output_path):
    # Initialize gTTS with English language
    tts = gTTS(text, lang='en')

    # Save the speech as an MP3 file
    tts.save(output_path)

def main():
    pdf_path = 'test.pdf'  # Path to your PDF file
    output_path = 'output.mp3'  # Output path for the MP3 file
    
    # Convert PDF to text
    text = pdf_to_text(pdf_path)
    
    # Convert text to audio and save as MP3
    text_to_audio(text, output_path)
    
    print("Conversion completed successfully!")

if __name__ == "__main__":
    main()



