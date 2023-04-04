import numpy as np
import scipy.io.wavfile as wavfile

# Load the audio file
audio_file = input("Enter the audio file:")
sampling_rate, audio_data = wavfile.read(audio_file)

# Set the frame duration and frequency thresholds
frame_duration = 0.05  # seconds
freq0_min = 430  # Hz
freq0_max = 450  # Hz
freq1_min = 870  # Hz
freq1_max = 890  # Hz

# Divide the audio signal into frames
frame_length = int(frame_duration * sampling_rate)
num_frames = len(audio_data) // frame_length
frames = np.reshape(audio_data[:num_frames * frame_length], (num_frames, frame_length))

# Determine the binary string from the frequency peaks in each frame
binary_string = ''
for frame in frames:
    spectrum = np.abs(np.fft.fft(frame))
    freqs = np.fft.fftfreq(len(frame), 1.0/sampling_rate)
    freq0_mask = (freqs >= freq0_min) & (freqs <= freq0_max)
    freq1_mask = (freqs >= freq1_min) & (freqs <= freq1_max)
    if np.max(spectrum[freq0_mask]) > np.max(spectrum[freq1_mask]):
        binary_string += '0'
    else:
        binary_string += '1'

# Convert the binary string to text
print(binary_string)
text = ''
for i in range(0, len(binary_string), 8):
    byte_str = binary_string[i:i+8]
    byte = int(byte_str, 2)
    text += chr(byte)

print(text)
