import cv2
from scipy.fftpack import dct, idct
import numpy as np
import pywt

def dct2(a):
    return dct(dct(a.T, norm='ortho').T, norm='ortho')

def idct2(a):
    return idct(idct(a.T, norm='ortho').T, norm='ortho')

def dct_based_watermarking(cover_image_path, watermark_image_path):
    # Load images
    img = cv2.imread(cover_image_path, 0)
    watermark = cv2.imread(watermark_image_path, 0)
    
    img = cv2.resize(img, (512, 512))
    watermark = cv2.resize(watermark, (512, 512))
    
    # DCT of cover image
    dct_img = dct2(img)
    # DCT of watermark image
    dct_watermark = dct2(watermark)

    alpha = 0.009
    beta = 0.1
    
    # Watermarked image
    dct_watermarked = dct_img + alpha * dct_watermark
    watermarked = idct2(dct_watermarked)
    watermarked = np.uint8(np.clip(watermarked, 0, 255))  # Convert to uint8
    cv2.imshow('Watermarked', watermarked)

    # Extracted watermark
    extracted_watermark = (dct_watermarked - dct_img) / beta
    extracted_watermark = idct2(extracted_watermark)
    extracted_watermark = np.uint8(np.clip(extracted_watermark, 0, 255))  # Convert to uint8
    cv2.imshow('Extracted Watermark', extracted_watermark)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def dwt_based_watermarking(cover_image_path, watermark_image_path):
    # Load images
    img = cv2.imread(cover_image_path, 0)
    watermark = cv2.imread(watermark_image_path, 0)
    
    img = cv2.resize(img, (512, 512))
    watermark = cv2.resize(watermark, (512, 512))
    
    # DWT of cover image
    coeffs_cover = pywt.dwt2(img, 'haar')
    cA_cover, (cH_cover, cV_cover, cD_cover) = coeffs_cover
    
    # DWT of watermark image
    coeffs_watermark = pywt.dwt2(watermark, 'haar')
    cA_watermark, (cH_watermark, cV_watermark, cD_watermark) = coeffs_watermark
    
    alpha = 0.01
    beta = 0.1
    
    # Watermarked image
    cA_watermarked = cA_cover + alpha * cA_watermark
    watermarked = pywt.idwt2((cA_watermarked, (cH_cover, cV_cover, cD_cover)), 'haar')
    watermarked = np.uint8(np.clip(watermarked, 0, 255))  # Convert to uint8
    cv2.imshow('Watermarked', watermarked)

    # Extracted watermark
    extracted_watermark = (cA_watermarked - cA_cover) / beta
    extracted_watermark = pywt.idwt2((extracted_watermark, (cH_cover, cV_cover, cD_cover)), 'haar')
    extracted_watermark = np.uint8(np.clip(extracted_watermark, 0, 255))  # Convert to uint8
    cv2.imshow('Extracted Watermark', extracted_watermark)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

dwt_based_watermarking('cover_image.png', 'watermark_image.png')
dct_based_watermarking('cover_image.png', 'watermark_image.png')

