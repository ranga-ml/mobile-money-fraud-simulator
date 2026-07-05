"""
Simulation Engine

Coordinates the execution of the simulator.
"""

from dataclasses import asdict
from pathlib import Path

import pandas as pd

from src.customer.generator import CustomerGenerator

from src.dealer.generator import DealerGenerator


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

        dealers = self.generate_dealers()

        customers = self.generate_customers()

        self.export_dealers(dealers)

        self.export_customers(customers)

        self.print_registry_summary()

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

        for customer in customers:
            self.context.registry.register_customer(customer)

        self.logger.info(f"{len(customers):,} customers generated.")

        return customers

    def generate_dealers(self):

        self.logger.info("Generating dealer network...")

        generator = DealerGenerator(self.context)

        dealers = generator.generate()

        for dealer in dealers:
            self.context.registry.register_dealer(dealer)

        self.logger.info(f"{len(dealers):,} dealers generated.")

        return dealers

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

    def export_dealers(self, dealers):

        output_folder = Path("outputs")
        output_folder.mkdir(exist_ok=True)

        df = pd.DataFrame(
            [asdict(dealer) for dealer in dealers]
        )

        output_file = output_folder / "dealer_master.csv"

        df.to_csv(
            output_file,
            index=False,
        )

        self.logger.info(f"Dealer file written to {output_file}")

    def print_registry_summary(self):

        stats = self.context.registry.summary()

        self.logger.info("=" * 70)
        self.logger.info("Registry Summary")
        self.logger.info("=" * 70)

        self.logger.info(f"Dealers   : {stats['dealers']:,}")
        self.logger.info(f"Customers : {stats['customers']:,}")
        self.logger.info(f"Merchants : {stats['merchants']:,}")
        self.logger.info(f"Wallets   : {stats['wallets']:,}")
        self.logger.info(f"Devices   : {stats['devices']:,}")
        self.logger.info(f"SIMs      : {stats['sims']:,}")