import os

from algorithms.LZ77 import LZ77
from algorithms.RLE import RLE
from pathlib import Path


def process(filepath: Path, type: str):
    bytes = b''

    with open(filepath, 'rb') as f:
        bytes = f.read()

    print(f"\nLZ77 {type}:")
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
    print(f"Decompressed Size: {os.path.getsize(filepath.with_suffix('.rle.decompressed'))}")

if __name__ == "__main__":
    # process(Path(__file__).resolve().parent / "assets/images/blanc.bmp", 'image')
    process(Path(__file__).resolve().parent / "assets/binary/5000", 'Binary')