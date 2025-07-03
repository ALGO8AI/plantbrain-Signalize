import numpy as np
from scipy.fft import fft

def apply_fft(signal: np.ndarray) -> np.ndarray:
    """
    Apply FFT to the signal and return frequency components.
    """
    return fft(signal)

def compute_fft_magnitude(signal: np.ndarray) -> np.ndarray:
    """
    Compute the magnitude of the FFT result.
    """
    freq_signal = apply_fft(signal)
    return np.abs(freq_signal)
