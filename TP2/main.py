#JPEG and JPEG2000
from PIL import Image
from skimage.metrics import structural_similarity as compare_ssim
from pathlib import Path
import cv2

if __name__ == "__main__":
    # Get current file path
    current_path = Path(__file__).parent.absolute()
    img = Image.open(current_path / './assets/almonds.png')
    img.convert("RGB").save(current_path / './assets/full_quality_jpeg2000.jp2', 'JPEG2000')
    img.convert("RGB").save(current_path / './assets/compressed_jpeg2000.jp2', 'JPEG2000', quality_mode='dB', quality_layers=[27])

    img.convert("RGB").save(current_path / './assets/full_quality_jpeg.jpg', 'JPEG', quality=95)
    img.convert("RGB").save(current_path / './assets/compressed_jpeg.jpg', 'JPEG', quality=38)
    im1 = cv2.imread('./TP2/assets/compressed_jpeg2000.jp2')
    im2 = cv2.imread('./TP2/assets/full_quality_jpeg2000.jp2')
    print("JPEG2000 PSNR: ", cv2.PSNR(im1, im2))

    gray1 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)

    (score, diff) = compare_ssim(gray1, gray2, full=True)
    diff = (diff * 255).astype("uint8")
    print("JPEG2000 SSIM: {}".format(score))


    im1 = cv2.imread('./TP2/assets/full_quality_jpeg.jpg')
    im2 = cv2.imread('./TP2/assets/compressed_jpeg.jpg')
    print("JPEG PSNR: ", cv2.PSNR(im1, im2))

    gray1 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)

    (score, diff) = compare_ssim(gray1, gray2, full=True)
    diff = (diff * 255).astype("uint8")
    print("JPEG SSIM: {}".format(score))