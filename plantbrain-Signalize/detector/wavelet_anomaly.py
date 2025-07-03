import numpy as np
from base.base_detector import BaseDetector
from ops.wavelet import apply_wavelet_transform, extract_wavelet_detail_coeffs

class WaveletAnomalyDetector(BaseDetector):
    """
    Anomaly detection using Wavelet Transform.
    """
    
    def __init__(self, threshold: float = 1.5):
        super().__init__(threshold)
        
    def detect_anomalies(self, signal: np.ndarray) -> np.ndarray:
        """
        Detect anomalies by decomposing the signal using Wavelet Transform.
        """
        coeffs = apply_wavelet_transform(signal)
        detail_coeffs = extract_wavelet_detail_coeffs(coeffs)
        mean = np.mean(detail_coeffs)
        std = np.std(detail_coeffs)
        return np.abs(detail_coeffs) > (mean + self.threshold * std)
