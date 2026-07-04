"""
Entry point for the Mobile Money Fraud Analytics Accelerator.
"""

from src.simulator.context import SimulationContext
from src.simulator.engine import SimulationEngine


def main():

    context = SimulationContext()

    engine = SimulationEngine(context)

    engine.run()


if __name__ == "__main__":
    main()