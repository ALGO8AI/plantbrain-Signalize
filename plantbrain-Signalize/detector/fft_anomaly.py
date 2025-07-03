import numpy as np
from base.base_detector import BaseDetector
from ops.fft import compute_fft_magnitude

class FFTAnomalyDetector(BaseDetector):
    """
    Anomaly detection using FFT (Fast Fourier Transform).
    """
    
    def __init__(self, threshold: float = 1.5):
        super().__init__(threshold)
        
    def detect_anomalies(self, signal: np.ndarray) -> np.ndarray:
        """
        Detect anomalies by analyzing the frequency domain of the signal.
        """
        magnitude = compute_fft_magnitude(signal)
        mean = np.mean(magnitude)
        std = np.std(magnitude)
        return magnitude > (mean + self.threshold * std)
