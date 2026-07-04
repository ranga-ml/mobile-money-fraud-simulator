"""
Simulation Engine

Coordinates the execution of the simulator.
"""

from dataclasses import asdict
from pathlib import Path

import pandas as pd

from src.customer.generator import CustomerGenerator


class SimulationEngine:
    """Main orchestration class."""

    def __init__(self, context):

        self.context = context

        self.logger = context.logger

        self.config = context.config

        self.country = context.country

    def run(self):

        self.logger.info("=" * 70)
        self.logger.info("Starting Simulation")
        self.logger.info("=" * 70)

        self.print_summary()

        customers = self.generate_customers()

        self.export_customers(customers)

        self.logger.info("=" * 70)
        self.logger.info("Simulation completed successfully.")
        self.logger.info("=" * 70)

    def print_summary(self):

        self.logger.info(f"Country             : {self.country.name}")
        self.logger.info(f"Population          : {self.country.population:,}")
        self.logger.info(
            f"Mobile Money Users  : {self.country.mobile_money_users:,}"
        )
        self.logger.info(f"Regions             : {len(self.country.regions)}")

    def generate_customers(self):

        self.logger.info("Generating customers...")

        generator = CustomerGenerator(self.context)

        count = self.config["population"]["customers"]

        customers = generator.generate(count=count)

        self.logger.info(f"{len(customers):,} customers generated.")

        return customers

    def export_customers(self, customers):

        self.logger.info("Exporting customer master...")

        output_folder = Path("outputs")
        output_folder.mkdir(exist_ok=True)

        df = pd.DataFrame(
            [asdict(customer) for customer in customers]
        )

        output_file = output_folder / "customer_master.csv"

        df.to_csv(
            output_file,
            index=False,
        )

        self.logger.info(f"Customer file written to {output_file}")