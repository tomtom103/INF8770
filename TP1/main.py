
from algorithms.RLE import RLE
from algorithms.LZ77 import LZ77

if __name__ == "__main__":
    message = "AAAABAAAAAABBBAABAAAACABBABCDAADACAAAAAAAAAAAAAAAAAAAAAABABABBBA"
    rle = RLE(message, counterSize=2)
    print(f"RLE: Original Message: {message}")
    print(f"RLE: Encoded Binary: {''.join(rle.encode())}")
    print(f"RLE: Decoded Message: {rle.decode()}")
    print("RLE: Compression Rate: %.2f" % (1 - len("".join(rle.encode())) / len(rle.message_as_binary())))

    lz77_message = "CBAAAAAAAAAAAAAAAAAAAAABAABAACD"
    lz77 = LZ77(lz77_message, dictSize=6)
    print(f"LZ77: Original Message: {lz77_message}")
    print(f"LZ77: Encoded triplets: {lz77.encode()}")
    print(f"LZ77: Decoded Message: {lz77.decode()}")

    print("LZ77: Compression Rate: %.2f" % lz77.compression_rate())