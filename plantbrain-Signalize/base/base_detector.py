from abc import ABC, abstractmethod
import numpy as np

class BaseDetector(ABC):
    """
    Base class for anomaly detection models.
    All anomaly detection models should inherit this class.
    """
    
    def __init__(self, threshold: float = 1.5):
        self.threshold = threshold  # The threshold to detect anomalies
        
    @abstractmethod
    def detect_anomalies(self, signal: np.ndarray) -> np.ndarray:
        """
        Abstract method to be implemented by child classes for anomaly detection.
        """
        pass
    
    def compute_anomalies(self, signal: np.ndarray) -> np.ndarray:
        """
        Detect anomalies by applying the model and comparing with threshold.
        """
        anomalies = self.detect_anomalies(signal)
        return anomalies > self.threshold
