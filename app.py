import streamlit as st
import sounddevice as sd
import numpy as np
import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import librosa

# Load model and processor
@st.cache_resource
def load_asr_model():
    model = Wav2Vec2ForCTC.from_pretrained(r"D:\Intern\Khmer_Asr\StreamLit\Vituo\Model")
    processor = Wav2Vec2Processor.from_pretrained(r"D:\Intern\Khmer_Asr\StreamLit\Vituo\Processor")
    return model, processor

model, processor = load_asr_model()

# Function to record audio
def record_audio(duration=5, fs=16000):
    """Records audio for a fixed duration and sampling frequency"""
    st.write("Recording...")
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()  # Wait until recording is finished
    audio_data = np.squeeze(audio_data)
    st.write("Recording complete!")
    return audio_data, fs

# Function to transcribe audio with a progress bar and percentage display
def transcribe_audio_with_progress(audio, model, processor):
    """Transcribes audio data using the Wav2Vec2 model with a progress bar"""
    
    # Initialize the progress bar and status text
    progress_bar = st.progress(0)
    status_text = st.empty()

    # Update progress and status
    status_text.text(f"Transcribing... 0%")
    progress_bar.progress(0)

    # Step 1: Preprocessing (30% of progress)
    status_text.text(f"Transcribing... 30% (Preprocessing Audio)")
    input_values = processor(audio, return_tensors="pt", sampling_rate=16000).input_values
    progress_bar.progress(30)

    # Step 2: Inference (60% of progress)
    status_text.text(f"Transcribing... 60% (Performing Inference)")
    with torch.no_grad():
        logits = model(input_values).logits
    progress_bar.progress(60)

    # Step 3: Decoding (90% of progress)
    status_text.text(f"Transcribing... 90% (Decoding Results)")
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.decode(predicted_ids[0])
    progress_bar.progress(90)

    # Final Step: Completed (100%)
    progress_bar.progress(100)
    status_text.text(f"Transcription complete!")

    return transcription

# Function to load and process the uploaded audio file (FLAC)
def load_audio_file(uploaded_file):
    """Loads and processes an uploaded audio file"""
    audio, sr = librosa.load(uploaded_file, sr=16000)  # Load with a target sample rate of 16 kHz
    return audio, sr

# Streamlit interface
st.title("Khmer ASR with Wav2Vec2")

st.write("You can either record a 5-second audio clip or upload a .flac file for transcription.")

# Option 1: Record Audio
if st.button("Record Audio"):
    # Record for 5 seconds
    audio_data, fs = record_audio(duration=5)

    # Display audio data
    st.audio(audio_data, format="audio/wav", sample_rate=fs)

    # Transcribe the recorded audio with progress bar
    transcription = transcribe_audio_with_progress(audio_data, model, processor)

    # Display the transcription
    st.write("Transcription from recorded audio:")
    st.write(transcription)

# Option 2: Upload Audio File (FLAC)
uploaded_file = st.file_uploader("Upload a FLAC file", type=["flac"])

if uploaded_file is not None:
    # Load and process the uploaded audio file
    audio_data, fs = load_audio_file(uploaded_file)

    # Display the uploaded audio file
    st.audio(uploaded_file, format="audio/flac")

    # Transcribe the uploaded audio file with progress bar
    transcription = transcribe_audio_with_progress(audio_data, model, processor)

    # Display the transcription
    st.write("Transcription from uploaded file:")
    st.write(transcription)
