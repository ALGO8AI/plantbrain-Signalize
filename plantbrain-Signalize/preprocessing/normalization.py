import numpy as np

def normalize_signal(signal: np.ndarray) -> np.ndarray:
    """
    Normalize the signal to a range of [0, 1].
    """
    return (signal - np.min(signal)) / (np.max(signal) - np.min(signal))
