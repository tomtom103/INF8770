from typing import Tuple
import numpy as np

from pathlib import Path
from scipy.io.wavfile import read as wavread

from algorithms.RLE import RLE
from algorithms.LZ77 import LZ77


if __name__ == "__main__":
    wav_file = Path(__file__).resolve().parent / "assets/example.wav"
    sample_rate, data = wavread(wav_file)
    data = data.tobytes().hex()
    # data = data[:100]
    # print(data[:100])
    # print("RLE:")
    # rle = RLE(data, counterSize=2)
    # print("Original length: {}".format(len(data)))
    # encoded = ''.join(rle.encode())
    # print("Encoded length: {}".format(len(encoded)))
    # decoded = rle.decode()
    # print("Decoded length: {}".format(len(decoded)))
    # print("Length Match: {}".format(len(data) == len(decoded)))


    print("\nLZ77:")
    # DICTSIZE ALWAYS SMALLER THAN LOOKAHEAD 
    lz77 = LZ77(data, dictSize=6, lookAhead=64)
    print(f"Original Message length: {len(data)}")
    encoded_triplets = lz77.encode()
    print(f"Encoded Message length: {len(encoded_triplets)}")
    decoded = lz77.decode()
    print("Length Match: {}".format(len(data) == len(decoded)))
    print("LZ77: Compression Rate: %.2f" % lz77.compression_rate())


    # message = "AAAABAAAAAABBBAABAAAACABBABCDAADACAAAAAAAAAAAAAAAAAAAAAABABABBBA"
    # print(np.asarray(message))
    # rle = RLE(message, counterSize=2)
    # print(f"RLE: Original Message: {message}")
    # print(f"RLE: Encoded Binary: {''.join(rle.encode())}")
    # print(f"RLE: Decoded Message: {rle.decode()}")
    # print("RLE: Compression Rate: %.2f" % (1 - len("".join(rle.encode())) / len(rle.message_as_binary())))

    # lz77_message = "CBAAAAAAAAAAAAAAAAAAAAABAABAACD"
    # lz77 = LZ77(lz77_message, dictSize=8)
    # print(f"LZ77: Original Message: {lz77_message}")
    # print(f"LZ77: Encoded triplets: {lz77.encode()}")
    # print(f"LZ77: Decoded Message: {lz77.decode()}")
    # print("LZ77: Compression Rate: %.2f" % lz77.compression_rate())