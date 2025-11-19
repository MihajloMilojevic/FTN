"""
The following Python implementation of Shamir's secret sharing is
released into the Public Domain under the terms of CC0 and OWFa:
https://creativecommons.org/publicdomain/zero/1.0/
http://www.openwebfoundation.org/legal/the-owf-1-0-agreements/owfa-1-0

See the bottom few lines for usage. Tested on Python 2 and 3.
"""

from __future__ import division
from __future__ import print_function

import random
import functools
import wave
import numpy as np

# Open the WAV file
file_path = 'input11.wav'
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

# 12th Mersenne Prime
_PRIME = 2 ** 16

_RINT = functools.partial(random.SystemRandom().randint, 0)

def _eval_at(poly, x, prime):
    """Evaluates polynomial (coefficient tuple) at x, used to generate a
    shamir pool in make_random_shares below.
    """
    accum = 0
    for coeff in reversed(poly):
        accum *= x
        accum += coeff
        accum %= prime
    return accum

def make_random_shares(secret, minimum, shares, prime=_PRIME):
    """
    Generates a random shamir pool for a given secret, returns share points.
    """
    if minimum > shares:
        raise ValueError("Pool secret would be irrecoverable.")
    poly = [secret] + [_RINT(prime - 1) for i in range(minimum - 1)]
    points = [(i, _eval_at(poly, i, prime))
              for i in range(1, shares + 1)]
    return points

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

def _lagrange_interpolate(x, x_s, y_s, p):
    """
    Find the y-value for the given x, given n (x, y) points;
    k points will define a polynomial of up to kth order.
    """
    k = len(x_s)
    assert k == len(set(x_s)), "points must be distinct"
    def PI(vals):  # upper-case PI -- product of inputs
        accum = 1
        for v in vals:
            accum *= v
        return accum
    nums = []  # avoid inexact division
    dens = []
    for i in range(k):
        others = list(x_s)
        cur = others.pop(i)
        nums.append(PI(x - o for o in others))
        dens.append(PI(cur - o for o in others))
    den = PI(dens)
    num = sum([_divmod((((nums[i] * den) % p) * y_s[i]) % p, dens[i], p)
               for i in range(k)])
    return (_divmod(num, den, p) + p) % p

def recover_secret(shares, prime=_PRIME):
    """
    Recover the secret from share points
    (points (x,y) on the polynomial).
    """
    if len(shares) < 3:
        raise ValueError("need at least three shares")
    x_s, y_s = zip(*shares)
    return _lagrange_interpolate(0, x_s, y_s, prime)

def main():
    """Main function"""
    # Use each sample in the audio file as secret and store it in shares list for later recovery
    shares = []
    for sample in audio_array:
        shares.append([x[1] for x in make_random_shares((int(sample) + _PRIME) % _PRIME, 3, 6, prime=_PRIME)])
    # save the shares as audio files
    for i, share in enumerate(np.array(shares).T):
        share = np.array(share)
        share = share.astype(np.int16)
        with wave.open(f'share{i}.wav', 'wb') as wav_file:
            wav_file.setnchannels(n_channels)
            wav_file.setsampwidth(sample_width)
            wav_file.setframerate(frame_rate)
            wav_file.setnframes(n_frames)
            wav_file.writeframes(share.tobytes())
    print("Shares saved as audio files.")

    # Recover the secret from the shares
    recovered_secret = []
    for share in shares:
        recovered_secret.append(recover_secret([(i, share[i]) for i in range(6)], prime=_PRIME) + min_amplitude )
    recovered_secret = np.array(recovered_secret).astype(np.int16)
    with wave.open('recovered.wav', 'wb') as wav_file:
        wav_file.setnchannels(n_channels)
        wav_file.setsampwidth(sample_width)
        wav_file.setframerate(frame_rate)
        wav_file.setnframes(n_frames)
        wav_file.writeframes(recovered_secret.tobytes())
    print("Secret recovered and saved as recovered.wav")

if __name__ == '__main__':
    main()