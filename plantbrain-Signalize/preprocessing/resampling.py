import numpy as np
from scipy.signal import resample

def resample_signal(signal: np.ndarray, target_length: int) -> np.ndarray:
    """
    Resample the signal to the target length.
    """
    return resample(signal, target_length)
