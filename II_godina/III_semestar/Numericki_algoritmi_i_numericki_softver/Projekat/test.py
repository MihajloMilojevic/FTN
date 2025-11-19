import wave
import numpy as np

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
    min_amplitude = -(2**(8*sample_width - 1))
    max_amplitude = (2**(8*sample_width - 1)) - 1
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
k = 5
n = 10
# Shamir’s secret sharing scheme

def shamir_secret_sharing(k, n, audio, min_amplitude, max_amplitude) -> np.ndarray:
    mod = max_amplitude - min_amplitude + 1
    coef = np.random.uniform(0, mod, (k+2, len(audio))).astype(int)
    coef[0] = audio + min_amplitude
    coef %= mod
    y = [None] * n
    for i in range(1, n+1):
        x = np.ones(len(audio), dtype="int") * i
        powers = np.array([x**j for j in range(k+2)])
        powers %= mod
        print(powers.shape, coef.shape)
        y[i-1] = np.sum(coef * powers, axis=0) % mod + min_amplitude
    return np.array(y)

res = shamir_secret_sharing(k, n, audio_array, min_amplitude, max_amplitude)
for i in range(n):
    new_audio = res[i]
    output_file_path = f'output_share_{i+1}.wav'
    with wave.open(output_file_path, 'wb') as output_wav_file:
        output_wav_file.setnchannels(n_channels)
        output_wav_file.setsampwidth(sample_width)
        output_wav_file.setframerate(frame_rate)
        output_wav_file.writeframes(new_audio.astype(np.float16).tobytes())


def interpolate(x, y, min_amplitude, max_amplitude):
    def _extended_gcd(a, b):
        """
        Division in integers modulus p means finding the inverse of the
        denominator modulo p and then multiplying the numerator by this
        inverse (Note: inverse of A is B such that A*B % p == 1). This can
        be computed via the extended Euclidean algorithm
        http://en.wikipedia.org/wiki/Modular_multiplicative_inverse#Computation
        """
        x = 0
        last_x = 1
        y = 1
        last_y = 0
        while b != 0:
            quot = a // b
            a, b = b, a % b
            x, last_x = last_x - quot * x, x
            y, last_y = last_y - quot * y, y
        return last_x, last_y

    def _divmod(num, den, p):
        """Compute num / den modulo prime p

        To explain this, the result will be such that:
        den * _divmod(num, den, p) % p == num
        """
        inv, _ = _extended_gcd(den, p)
        return num * inv

    n = len(x)
    mod = max_amplitude - min_amplitude + 1
    res = np.zeros_like(x)
    for i in range(n):
        num = 1
        den = 1
        for j in range(n):
            if i == j:
                continue
            num *= -x[j]
            den *= x[i] - x[j]
        res += (y[i] * _divmod(int(num), int(den), mod)).astype(np.int16)
    return res % mod + min_amplitude

def reconstruct_audio(shares, k, min_amplitude, max_amplitude):
    n = len(shares)
    
    # Lagrange interpolation
    res = [None] * shares.shape[1]
    x = np.arange(1, n+1)
    for i in range(shares.shape[1]):
        y = shares[:, i]
        res[i] = interpolate(x, y, min_amplitude, max_amplitude)
    return np.array(res).astype(np.int16)

# Reconstruct the original audio from the shares
reconstructed_audio = reconstruct_audio(res, k, min_amplitude, max_amplitude)
output_file_path = 'reconstructed_audio.wav'
with wave.open(output_file_path, 'wb') as output_wav_file:
    output_wav_file.setnchannels(n_channels)
    output_wav_file.setsampwidth(sample_width)
    output_wav_file.setframerate(frame_rate)
    output_wav_file.writeframes(reconstructed_audio.tobytes())

