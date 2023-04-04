import wave
import struct
import numpy as np
def text_to_binary(text):
    binary = ''
    for char in text:
        binary += bin(ord(char))[2:].zfill(8)


    return binary



def binary_to_audio(binary, file_name):
    sample_rate = 44100.0
    duration = 0.05
    freq0 = 440.0
    freq1 = 880.0

    wave_file = wave.open(file_name, 'w')
    wave_file.setparams((1, 2, int(sample_rate), 0, 'NONE', 'not compressed'))

    for b in binary:
        if b == '0':
            freq = freq0
        elif b == '1':
            freq = freq1
        else:
            continue

        num_samples = int(duration * sample_rate)
        time_array = np.arange(num_samples, dtype=np.float32) / sample_rate
        signal = np.sin(2.0 * np.pi * freq * time_array) * 0.5
        signal *= 32767 / np.max(np.abs(signal))  # Normalize the signal
        signal = signal.astype(np.int16)
        data = struct.pack('<' + str(len(signal)) + 'h', *signal)
        wave_file.writeframesraw(data)

    wave_file.close()


if __name__ == '__main__':
    file_name = input("Enter the location of the file:")

    with open(file_name, 'r') as f:
        text = f.read().strip()

    binary = text_to_binary(text)
    binary_to_audio(binary, file_name+'output.mp3')  #new audio file will be stored in the file where input file is present
    print("Done successfully")
