import wave

import numpy as np
import matplotlib.pyplot as plt

# Open the WAV file
file_path = 'input.wav'

with wave.open(file_path, 'rb') as wav_file:
    # Extract raw audio from the WAV file
    n_channels = wav_file.getnchannels()
    sample_width = wav_file.getsampwidth()
    frame_rate = wav_file.getframerate()
    n_frames = wav_file.getnframes()
    audio_data = wav_file.readframes(n_frames)
    # Determine the theoretical minimum and maximum amplitude values
    min_amplitude = -(2 ** (8 * sample_width - 1))
    max_amplitude = (2 ** (8 * sample_width - 1)) - 1
    mod = max_amplitude - min_amplitude + 1
    # print(f"Theoretical minimum amplitude: {min_amplitude}")
    # print(f"Theoretical maximum amplitude: {max_amplitude}")
    # print(f"Modulus: {mod}")
    # print(f"Number of channels: {n_channels}")
    # print(f"Sample width: {sample_width}")
    # print(f"Frame rate: {frame_rate}")
    # print(f"Number of frames: {n_frames}")

# Convert the raw audio data to a numpy array
type_map = {
    1: np.int8,
    2: np.int16,
    4: np.int32
}
audio_array = np.frombuffer(audio_data, dtype=type_map[sample_width])
print(f"Audio data as numpy array: {audio_array.shape}")

# Plot the audio data
plt.figure(figsize=(12, 6))
plt.plot(audio_array)
plt.title('Audio Data')
plt.show()