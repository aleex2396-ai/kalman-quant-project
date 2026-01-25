# \# Regime-Adaptive Statistical Arbitrage

# \## Parameter Calibration of the Ornstein-Uhlenbeck Process via MLE and Kalman Filtering

# 

# \### 📌 Project Overview

# This project implements a self-calibrating pairs trading framework designed to handle non-stationary financial time series. While traditional statistical arbitrage relies on static cointegration, this model treats the asset spread as a continuous-time \*\*Stochastic Differential Equation (SDE)\*\*. 

# 

# By applying a \*\*Kalman Filter\*\* for state estimation and \*\*Maximum Likelihood Estimation (MLE)\*\* for parameter optimization, the system dynamically adapts to market regime shifts, significantly reducing drawdowns during high-volatility events (e.g., the 2020 market crash).

# 

# \### 🧪 Mathematical Framework

# The core of the strategy models the price spread ($X\_t$) as an \*\*Ornstein-Uhlenbeck (OU) process\*\*:

# 

# $$dX\_t = \\theta (\\mu - X\_t)dt + \\sigma dW\_t$$

# 

# Where:

# \* \*\*$\\theta$\*\*: Rate of mean reversion.

# \* \*\*$\\mu$\*\*: Long-term equilibrium level.

# \* \*\*$\\sigma$\*\*: Diffusion coefficient (volatility).

# 

# The continuous SDE is discretized using the \*\*Euler-Maruyama method\*\* to facilitate a discrete-time State-Space representation suitable for Kalman Filtering.

# 

# \### 🚀 Key Features

# \* \*\*Manual NumPy Implementation\*\*: Discrete Kalman Filter built from scratch to track the hidden state (hedge ratio) without reliance on black-box libraries.

# \* \*\*Dynamic Calibration\*\*: MLE module using `scipy.optimize` to solve for optimal theta and sigma parameters in real-time.

# \* \*\*Regime Robustness\*\*: Benchmarked against standard Rolling Z-Score models, demonstrating a \*\*40% reduction in Max Drawdown\*\* during the March 2020 liquidity crisis.

# 

# \### 📂 Repository Structure

# \* `/docs`: Contains the full LaTeX derivation of the OU-SDE discretization.

# \* `/src`: Modular Python scripts for the Filter, Optimizer, and Backtester.

# \* `research\_main.ipynb`: Comprehensive walk-through of the hypothesis, math, and results.

# 

# \### 📈 Results summary

# | Metric | Static Z-Score | MLE-Kalman (This Model) |

# | :--- | :--- | :--- |

# | Annualized Return | 8.2% | 12.5% |

# | Max Drawdown | -22.1% | -13.2% |

# | Sharpe Ratio | 0.82 | 1.45 |

