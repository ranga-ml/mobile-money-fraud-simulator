"""
Mobile Money Fraud Analytics Accelerator

Common Enumerations
"""

from enum import Enum


class EntityType(str, Enum):
    """Supported entity types."""

    CUSTOMER = "CUS"
    DEALER = "DLR"
    MERCHANT = "MER"
    WALLET = "WLT"
    TRANSACTION = "TXN"
    DEVICE = "DEV"
    SIM = "SIM"
    LOAN = "LON"
    REFERRAL = "REF"
    COMMISSION = "COM"
    FLOAT = "FLT"