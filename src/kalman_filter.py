import numpy as np


class KalmanFilter:
    def __init__(self, dt, theta, mu, sigma):
        """
        Initialize the filter parameters based on the OU Process derivation.

        Args:
            dt (float): Time step (e.g., 1/252 for daily data).
            theta (float): Mean reversion speed.
            mu (float): Long-term mean equilibrium.
            sigma (float): Volatility (process noise).
        """
        self.dt = dt
        self.theta = theta
        self.mu = mu
        self.sigma = sigma

        # --- 1. STATE INITIALIZATION ---
        # x: The hidden state (True Spread). Start at mu (equilibrium).
        self.x = mu

        # P: The uncertainty covariance. Start with 1.0 (some uncertainty).
        self.P = 1.0

        # --- 2. DEFINE MATRICES (From your PDF) ---
        # F: State Transition (Decay factor)
        # "Memory of the past"
        self.F = np.exp(-theta * dt)

        # B: Control Input (Drift factor)
        # "Pull of the mean"
        self.B = mu * (1 - self.F)

        # Q: Process Noise Variance (The Integral solution)
        # "New uncertainty entering the system every day"
        self.Q = (sigma ** 2 / (2 * theta)) * (1 - np.exp(-2 * theta * dt))

        # R: Measurement Noise (Sensor Error)
        # For now, we fix this. Later, MLE will solve it.
        self.R = 0.001

    def predict(self):
        """
        Step 1: Physics Prediction
        Estimate where the spread SHOULD be based on the OU equation.
        """
        # x_pred = F * x_prev + B
        self.x = (self.F * self.x) + self.B

        # P_pred = F * P_prev * F + Q
        self.P = (self.F * self.P * self.F) + self.Q

        return self.x

    def update(self, measurement):
        """
        Step 2: Sensor Correction
        Correct the prediction using the actual observed price.
        """
        # y: The "Innovation" (Surprise) = Measurement - Prediction
        y = measurement - self.x

        # S: System Uncertainty = P + R
        S = self.P + self.R

        # K: Kalman Gain = How much do we trust the new measurement?
        # If S is large (lot of noise), K is small (trust physics).
        K = self.P / S

        # Update State (x)
        self.x = self.x + (K * y)

        # Update Uncertainty (P)
        self.P = (1 - K) * self.P

        return self.x