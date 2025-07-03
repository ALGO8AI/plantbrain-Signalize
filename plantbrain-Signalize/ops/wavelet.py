import numpy as np
import pywt

def apply_wavelet_transform(signal: np.ndarray, level: int = 4) -> list:
    """
    Apply wavelet transform to the signal and return wavelet coefficients.
    """
    return pywt.wavedec(signal, 'db4', level=level)

def extract_wavelet_detail_coeffs(coeffs: list) -> np.ndarray:
    """
    Extract the detail coefficients from wavelet transform.
    """
    return coeffs[1]  # Detail coefficients at level 1
