from pykalman import KalmanFilter

def apply_kalman_filter(signal: np.ndarray) -> np.ndarray:
    """
    Apply Kalman Filter to the signal and return the smoothed result.
    """
    kf = KalmanFilter(initial_state_mean=0, n_dim_obs=1)
    state_means, _ = kf.filter(signal)
    return state_means.flatten()
