import os

from algorithms.LZ77 import LZ77
from algorithms.RLE import RLE
from pathlib import Path

def process(filepath: Path, type: str):
    bytes = b''

    with open(filepath, 'rb') as f:
        bytes = f.read()

    print(f"{os.path.basename(filepath)}:\n")

    print(f"LZ77 {type}:")
    lz77 = LZ77(window_size=2048)
    lz77.compress(bytes, output_file_path=filepath.with_suffix('.lz77'))
    lz77.decompress(filepath.with_suffix('.lz77'), output_file_path=filepath.with_suffix('.lz77.decompressed'))
    print(f"Compressed Size: {os.path.getsize(filepath.with_suffix('.lz77'))}")
    print(f"Decompressed Size: {os.path.getsize(filepath.with_suffix('.lz77.decompressed'))}")

    print(f"\nRLE {type}:")
    rle = RLE(bytes)
    rle.compress(bytes, output_file_path=filepath.with_suffix('.rle'))
    rle.decompress(filepath.with_suffix('.rle'), output_file_path=filepath.with_suffix('.rle.decompressed'))
    print(f"Compressed Size: {os.path.getsize(filepath.with_suffix('.rle'))}")
    print(f"Decompressed Size: {os.path.getsize(filepath.with_suffix('.rle.decompressed'))}\n")

    # Cleanup after the program is done
    os.remove(filepath.with_suffix('.lz77'))
    os.remove(filepath.with_suffix('.lz77.decompressed'))
    os.remove(filepath.with_suffix('.rle'))
    os.remove(filepath.with_suffix('.rle.decompressed'))

if __name__ == "__main__":
    process(Path(__file__).resolve().parent / "assets/temp/asine.wav", 'WAV')
    process(Path(__file__).resolve().parent / "assets/temp/beach_and_seagulls.wav", 'WAV')
    process(Path(__file__).resolve().parent / "assets/temp/saw.wav", 'WAV')
    process(Path(__file__).resolve().parent / "assets/temp/seawave.wav", 'WAV')
    process(Path(__file__).resolve().parent / "assets/temp/sine.wav", 'WAV')
    process(Path(__file__).resolve().parent / "assets/temp/sinec4.wav", 'WAV')
    process(Path(__file__).resolve().parent / "assets/temp/square.wav", 'WAV')