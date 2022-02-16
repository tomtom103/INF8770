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
    img = Image.open(current_path / './assets/almonds.png')
    img.convert("RGB").save(current_path / './assets/full_quality_jpeg2000.jp2', 'JPEG2000')
    img.convert("RGB").save(current_path / './assets/compressed_jpeg2000.jp2', 'JPEG2000', quality_mode='rates', quality_layers=[9])

    img.convert("RGB").save(current_path / './assets/full_quality_jpeg.jpg', 'JPEG', quality=95)
    img.convert("RGB").save(current_path / './assets/compressed_jpeg.jpg', 'JPEG', quality=85)
    im1 = cv2.imread('./TP2/assets/compressed_jpeg2000.jp2')
    im2 = cv2.imread('./TP2/assets/full_quality_jpeg2000.jp2')
    print("JPEG2000: ", cv2.PSNR(im1, im2))
    im1 = cv2.imread('./TP2/assets/full_quality_jpeg.jpg')
    im2 = cv2.imread('./TP2/assets/compressed_jpeg.jpg')
    print("JPEG: ", cv2.PSNR(im1, im2))