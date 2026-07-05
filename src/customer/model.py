"""
Customer domain model.
"""

from dataclasses import dataclass
from datetime import date


@dataclass(slots=True)
class Customer:
    customer_id: str
    first_name: str
    last_name: str

    gender: str

    age: int

    date_of_birth: date

    dealer_id: str

    wallet_id: str

    device_id: str

    sim_id: str

    registration_date: date

    occupation: str

    monthly_income: int

    region: str

    district: str

    kyc_level: str

    wallet_status: str

    risk_band: str