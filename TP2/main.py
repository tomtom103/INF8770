#JPEG and JPEG2000
from PIL import Image

from pathlib import Path
import cv2

# def png_to_jpeg2000(path: Union[Path, str]):
#     """
#     Convert a PNG image to a JPEG2000 image.
#     """
#     img = Image.open(path)
#     img.convert("RGB").save(path.with_suffix('.jp2'), 'JPEG2000', quality_mode='rates', quality_layers=[30])

# def png_to_jpg(path: Union[Path, str]):
#     """
#     Convert a PNG image to a JPEG image.
#     """
#     img = Image.open(path)
#     img.convert("RGB").save(path.with_suffix('.jpg'), 'JPEG')

if __name__ == "__main__":
    # Get current file path
    current_path = Path(__file__).parent.absolute()
    img = Image.open(current_path / './assets/baboon.png')
    img.convert("RGB").save(current_path / './assets/baboon2.jp2', 'JPEG2000', quality_mode='dB', quality_layers=[25])

    im1 = cv2.imread('./TP2/assets/baboon.jp2')
    im2 = cv2.imread('./TP2/assets/baboon2.jp2')
    print(cv2.PSNR(im1, im2))