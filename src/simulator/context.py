"""
Simulation Context

Central object shared across the simulator.
"""

from dataclasses import dataclass, field
from random import Random

from src.common.config import ConfigManager
from src.common.logger import Logger
from src.common.reference_data import ReferenceData
from src.simulator.loader import CountryLoader
from src.registry.registry import EntityRegistry

@dataclass(slots=True)
class SimulationContext:
    """
    Holds all shared simulator state.
    """

    config: dict = field(init=False)

    country: object = field(init=False)

    reference_data: dict = field(init=False)

    logger: object = field(init=False)

    random: Random = field(init=False)

    registry: EntityRegistry = field(init=False)

    def __post_init__(self):

        self.registry = EntityRegistry()

        self.config = ConfigManager().get()

        self.country = CountryLoader.load()

        self.reference_data = ReferenceData.load()

        self.logger = Logger.get_logger()

        seed = self.config["simulation"]["random_seed"]

        self.random = Random(seed)

        self.logger.info("Simulation Context initialized.")