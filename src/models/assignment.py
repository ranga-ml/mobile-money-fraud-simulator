from dataclasses import dataclass


@dataclass(slots=True)
class DealerAssignment:
    customer_id: str
    dealer_id: str