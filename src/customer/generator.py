"""
Customer Generator
"""

from datetime import date, timedelta

from faker import Faker

from src.customer.model import Customer
from src.common.enums import EntityType
from src.common.ids import IDGenerator
from src.common.reference_data import ReferenceData


class CustomerGenerator:
    """Generates synthetic customers."""

    def __init__(self, context):

        self.context = context

        self.random = context.random

        self.country = context.country

        self.fake = Faker()

        # Use the same simulation seed everywhere
        seed = context.config["simulation"]["random_seed"]
        self.fake.seed_instance(seed)

        self.occupations = ReferenceData.get("occupations")
        self.kyc_levels = ReferenceData.get("kyc_levels")
        self.wallet_status = ReferenceData.get("wallet_status")
        self.risk_bands = ReferenceData.get("risk_bands")

    def generate(self, count: int):

        customers = []

        today = date.today()

        for i in range(1, count + 1):

            age = self.random.randint(18, 70)

            dob = today - timedelta(days=age * 365)

            # ----------------------------
            # Select region based on dealer density
            # ----------------------------

            region = self.random.choices(
                self.country.regions,
                weights=[r.dealer_density for r in self.country.regions],
                k=1,
            )[0]

            # ----------------------------
            # Income depends on region
            # ----------------------------

            base_income = self.random.randint(8000, 60000)

            monthly_income = int(
                base_income * region.income_multiplier
            )

            # ----------------------------
            # Initial regional risk
            # ----------------------------

            if region.fraud_risk > 1.2:
                risk = "HIGH"
            elif region.fraud_risk > 0.9:
                risk = "MEDIUM"
            else:
                risk = "LOW"

            customer = Customer(

                customer_id=IDGenerator.generate(
                    EntityType.CUSTOMER,
                    i,
                ),

                first_name=self.fake.first_name(),

                last_name=self.fake.last_name(),

                gender=self.random.choice(
                    ["Male", "Female"]
                ),

                age=age,

                date_of_birth=dob,

                dealer_id=IDGenerator.generate(
                    EntityType.DEALER,
                    self.random.randint(1, 500),
                ),

                wallet_id=IDGenerator.generate(
                    EntityType.WALLET,
                    i,
                ),

                device_id=IDGenerator.generate(
                    EntityType.DEVICE,
                    i,
                ),

                sim_id=IDGenerator.generate(
                    EntityType.SIM,
                    i,
                ),

                registration_date=today - timedelta(
                    days=self.random.randint(0, 365)
                ),

                occupation=self.random.choice(
                    self.occupations
                ),

                monthly_income=monthly_income,

                region=region.name,

                district=f"District-{self.random.randint(1,20)}",

                kyc_level=self.random.choice(
                    self.kyc_levels
                ),

                wallet_status=self.wallet_status[0],

                risk_band=risk,
            )

            customers.append(customer)

        return customers