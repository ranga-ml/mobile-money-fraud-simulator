"""
Dealer Assignment Service

Responsible for assigning customers to dealers while
respecting regional affinity and dealer capacity.
"""

from __future__ import annotations

from collections import defaultdict
from random import Random

from models.assignment import DealerAssignment
from customer.model import Customer
from dealer.model import Dealer


class DealerAssignmentService:
    """Assign customers to dealers."""

    def assign(
        self,
        customers: list[Customer],
        dealers: list[Dealer],
        rng: Random,
    ) -> list[DealerAssignment]:

        region_index = self._build_region_index(dealers)

        assignments: list[DealerAssignment] = []

        for customer in customers:

            dealer = self._select_dealer(
                customer.region,
                region_index,
                rng,
            )

            assignments.append(
                DealerAssignment(
                    customer_id=customer.customer_id,
                    dealer_id=dealer.dealer_id,
                )
            )

            dealer.current_customer_count += 1

        return assignments

    def _build_region_index(
        self,
        dealers: list[Dealer],
    ) -> dict[str, list[Dealer]]:

        index: dict[str, list[Dealer]] = defaultdict(list)

        for dealer in dealers:
            if dealer.active:
                index[dealer.region].append(dealer)

        return dict(index)

    def _select_dealer(
        self,
        region: str,
        region_index: dict[str, list[Dealer]],
        rng: Random,
    ) -> Dealer:

        dealers = [
            dealer
            for dealer in region_index.get(region, [])
            if dealer.customer_capacity_remaining > 0
        ]

        if not dealers:
            raise ValueError(
                f"No dealer with capacity found in region '{region}'."
            )

        weights = [
            dealer.customer_capacity_remaining
            for dealer in dealers
        ]

        return rng.choices(
            dealers,
            weights=weights,
            k=1,
        )[0]