"""
Mobile Money Fraud Simulator

Custom Exceptions
"""


class SimulatorError(Exception):
    """Base exception for the simulator."""


class ConfigurationError(SimulatorError):
    """Raised when configuration cannot be loaded."""


class ValidationError(SimulatorError):
    """Raised when configuration is invalid."""