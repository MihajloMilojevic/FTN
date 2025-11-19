import wave
import numpy as np
import os

# Utility functions for Shamir's Secret Sharing

def mod_inverse(a, p):
    """Calculate the modular inverse of a under modulo p using Extended Euclidean Algorithm."""
    original_p = p
    x0, x1 = 0, 1
    while a > 1:
        if p == 0:
            raise ValueError(f"No modular inverse for {a} under modulo {original_p}")
        q = a // p
        a, p = p, a % p
        x0, x1 = x1 - q * x0, x0
    return x1 + original_p if x1 < 0 else x1


def lagrange_interpolation(x, x_points, y_points, p):
    """Perform Lagrange interpolation to find f(x) in finite field Zp."""
    total = 0
    for i in range(len(x_points)):
        xi, yi = x_points[i], y_points[i]
        product = yi
        for j in range(len(x_points)):
            if i != j:
                xj = x_points[j]
                numerator = (x - xj) % p
                denominator = (xi - xj) % p
                product = (product * numerator * mod_inverse(denominator, p)) % p
        total = (total + product) % p
    return total

def split_secret(secret, n_shares, threshold, p=104729):
    """Split a secret into n_shares using Shamir's Secret Sharing."""
    import random
    coefficients = [random.randint(0, p - 1) for _ in range(threshold - 1)]
    coefficients.append(secret)
    shares = []
    for x in range(1, n_shares + 1):
        y = sum([(int(coeff) % p * pow(int(x), i, p) % p) % p for i, coeff in enumerate(coefficients)]) % p
        shares.append((x, y))
    return shares

def reconstruct_secret(shares, p=104729):
    """Reconstruct a secret from shares using Shamir's Secret Sharing."""
    x_points, y_points = zip(*shares)
    return lagrange_interpolation(0, x_points, y_points, p)

def load_wav_file(file_path):
    """Load a WAV audio file and return the frame rate, sample width, and audio frames."""
    with wave.open(file_path, 'rb') as wav_file:
        frame_rate = wav_file.getframerate()
        sample_width = wav_file.getsampwidth()
        n_frames = wav_file.getnframes()
        frames = wav_file.readframes(n_frames)
        
        audio_data = np.frombuffer(frames, dtype=np.int16)  # Assuming 16-bit PCM
    
    return frame_rate, sample_width, audio_data

def save_wav_file(file_path, frame_rate, sample_width, audio_data):
    """Save the given audio data as a WAV file."""
    with wave.open(file_path, 'wb') as wav_file:
        wav_file.setnchannels(1)  # Mono audio
        wav_file.setsampwidth(sample_width)  # 16-bit samples
        wav_file.setframerate(frame_rate)  
        wav_file.writeframes(audio_data.tobytes())

def split_audio_into_shares(audio_data, n_shares=5, threshold=3):
    """Split the audio data into SSS shares per sample."""
    shares_per_sample = []
    for sample in audio_data:
        sample = np.uint16(sample)  # Convert to unsigned 16-bit to ensure correct bit pattern
        shares = split_secret(sample, n_shares, threshold)  # Use unsigned 16-bit value
        shares_per_sample.append(shares)
    return shares_per_sample

def reconstruct_audio_from_shares(shares_per_sample, threshold=3):
    """Reconstruct the audio data from SSS shares per sample."""
    reconstructed_samples = []
    for shares in shares_per_sample:
        secret = reconstruct_secret(shares[:threshold])  # Use only the threshold number of shares
        reconstructed_samples.append(secret if secret <= 32767 else secret - 65536)  # Convert to signed 16-bit int
    audio_data = np.array(reconstructed_samples, dtype=np.int16)
    return audio_data

def save_shares_to_files(shares_per_sample, output_dir):
    """Save the SSS shares as text files in the specified directory."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for i, shares in enumerate(shares_per_sample):
        file_path = os.path.join(output_dir, f'sample_{i+1}.txt')
        with open(file_path, 'w') as f:
            for share in shares:
                f.write(f"{share[0]},{share[1]}\n")

def load_shares_from_files(input_dir, n_samples, n_shares):
    """Load SSS shares from files in the specified directory."""
    shares_per_sample = []
    for i in range(1, n_samples + 1):
        file_path = os.path.join(input_dir, f'sample_{i}.txt')
        with open(file_path, 'r') as f:
            shares = [tuple(map(int, line.strip().split(','))) for line in f]
            shares_per_sample.append(shares[:n_shares])  # Load only the necessary number of shares per sample
    return shares_per_sample

def main():
    input_audio_path = 'input.wav'  # Path to the input WAV file
    shares_dir = 'shares'  # Directory to save the SSS shares
    output_audio_path = 'reconstructed.wav'  # Path to save the reconstructed WAV file
    
    # Step 1: Load the audio file
    print("Loading audio file...")
    frame_rate, sample_width, audio_data = load_wav_file(input_audio_path)
    print(f"Loaded audio with {len(audio_data)} samples, frame rate = {frame_rate} Hz, sample width = {sample_width} bytes")
    
    # Step 2: Split the audio into SSS shares
    print("Splitting audio into SSS shares...")
    n_shares = 5
    threshold = 3
    shares_per_sample = split_audio_into_shares(audio_data, n_shares, threshold)
    save_shares_to_files(shares_per_sample, shares_dir)
    print(f"Saved {len(shares_per_sample)} samples with {n_shares} SSS shares each to {shares_dir}/")
    
    # Step 3: Load shares from files (simulating a real-world reconstruction)
    print("Loading shares from files...")
    loaded_shares = load_shares_from_files(shares_dir, len(audio_data), threshold)  # Load only the threshold number of shares per sample
    print(f"Loaded shares for {len(loaded_shares)} samples for reconstruction.")
    
    # Step 4: Reconstruct the audio from the shares
    print("Reconstructing audio from shares...")
    reconstructed_audio_data = reconstruct_audio_from_shares(loaded_shares, threshold)
    
    # Step 5: Save the reconstructed audio to a new WAV file
    print("Saving reconstructed audio...")
    save_wav_file(output_audio_path, frame_rate, sample_width, reconstructed_audio_data)
    print(f"Reconstructed audio saved to {output_audio_path}")

if __name__ == "__main__":
    main()
