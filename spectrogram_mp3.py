import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import librosa.display
import numpy as np

# Set the path to the directory containing the MP3 files
audio_path = "test audio mp3/"

# Initialize the PDF file
pdf_pages = PdfPages("spectrograms.pdf")

# Loop through all the audio files in the directory and generate their spectrograms
for filename in os.listdir(audio_path):
    if filename.endswith(".mp3"):
        file_path = os.path.join(audio_path, filename)
        y, sr = librosa.load(file_path, sr=44100)
        plt.figure(figsize=(10, 4))
        D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
        librosa.display.specshow(D, y_axis='linear', x_axis='time', sr=sr)
        plt.colorbar(format='%+2.0f dB')
        plt.title(filename)
        plt.tight_layout()
        pdf_pages.savefig()

# Close the PDF file
pdf_pages.close()
