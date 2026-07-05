from __future__ import annotations

from random import Random

from simulator.models.assignment import DealerAssignment


class DealerAssignmentService:
    """Assign customers to dealers."""

    def assign(
        self,
        customers,
        dealers,
        rng: Random,
    ) -> list[DealerAssignment]:
        raise NotImplementedError