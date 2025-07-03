import numpy as np
from scipy.signal import medfilt

def remove_noise(signal: np.ndarray, kernel_size: int = 3) -> np.ndarray:
    """
    Apply median filter to remove noise from the signal.
    """
    return medfilt(signal, kernel_size)
