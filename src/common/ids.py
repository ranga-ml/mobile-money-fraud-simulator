"""
ID Generator

Creates consistent IDs across the simulator.
"""

from src.common.enums import EntityType


class IDGenerator:
    """
    Centralized ID generation.

    Example

    CUS000000001

    DLR000000001

    TXN000000000001
    """

    @staticmethod
    def generate(entity: EntityType, number: int) -> str:

        if entity == EntityType.TRANSACTION:
            width = 15
        else:
            width = 9

        return f"{entity.value}{number:0{width}d}"