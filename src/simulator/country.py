"""
Country Model

Represents the entire simulated country.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Region:

    name: str

    urban_ratio: float

    income_multiplier: float

    dealer_density: float

    fraud_risk: float


@dataclass(slots=True)
class Country:

    name: str

    currency: str

    population: int

    mobile_money_users: int

    regions: list[Region]