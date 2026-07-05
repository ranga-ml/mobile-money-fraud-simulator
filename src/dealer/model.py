"""
Dealer Domain Model
"""

from dataclasses import dataclass
from datetime import date


@dataclass(slots=True)
class Dealer:

    dealer_id: str

    dealer_name: str

    dealer_type: str

    parent_dealer_id: str | None

    region: str

    district: str

    registration_date: date

    active: bool

    float_balance: float

    cash_balance: float

    commission_balance: float

    customer_capacity: int

    current_customer_count: int = 0

    merchant_capacity: int

    current_merchant_count: int = 0


    @property
    def customer_capacity_remaining(self) -> int:
        return (
            self.customer_capacity
            - self.current_customer_count
        )