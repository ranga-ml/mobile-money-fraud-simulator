"""
Dealer Generator
"""

from datetime import date

from src.common.enums import EntityType
from src.common.ids import IDGenerator
from src.dealer.model import Dealer


class DealerGenerator:

    def __init__(self, context):

        self.context = context

        self.random = context.random

        self.country = context.country

    def generate(self):

        dealers = []

        dealer_number = 1

        for region in self.country.regions:

            #
            # Number of retail agents is proportional
            # to dealer density
            #

            agents = max(
                20,
                int(region.dealer_density * 100),
            )

            masters = max(
                1,
                agents // 20,
            )

            #
            # One Super Dealer per region
            #

            super_id = IDGenerator.generate(
                EntityType.DEALER,
                dealer_number,
            )

            dealers.append(
                Dealer(
                    dealer_id=super_id,
                    dealer_name=f"{region.name} Super Dealer",
                    dealer_type="SUPER_DEALER",
                    parent_dealer_id=None,
                    region=region.name,
                    district="Head Office",
                    registration_date=date.today(),
                    active=True,
                    float_balance=10_000_000,
                    cash_balance=2_000_000,
                    commission_balance=0,
                    customer_capacity=0,
                    merchant_capacity=0,
                )
            )

            dealer_number += 1

            master_ids = []

            #
            # Master Agents
            #

            for m in range(masters):

                master_id = IDGenerator.generate(
                    EntityType.DEALER,
                    dealer_number,
                )

                master_ids.append(master_id)

                dealers.append(
                    Dealer(
                        dealer_id=master_id,
                        dealer_name=f"{region.name} Master {m+1}",
                        dealer_type="MASTER_AGENT",
                        parent_dealer_id=super_id,
                        region=region.name,
                        district=f"District-{m+1}",
                        registration_date=date.today(),
                        active=True,
                        float_balance=1_000_000,
                        cash_balance=300_000,
                        commission_balance=0,
                        customer_capacity=0,
                        merchant_capacity=0,
                    )
                )

                dealer_number += 1

            #
            # Retail Agents
            #

            for a in range(agents):

                parent = master_ids[a % len(master_ids)]

                dealers.append(
                    Dealer(
                        dealer_id=IDGenerator.generate(
                            EntityType.DEALER,
                            dealer_number,
                        ),
                        dealer_name=f"{region.name} Agent {a+1}",
                        dealer_type="AGENT",
                        parent_dealer_id=parent,
                        region=region.name,
                        district=f"District-{self.random.randint(1,20)}",
                        registration_date=date.today(),
                        active=True,
                        float_balance=100_000,
                        cash_balance=20_000,
                        commission_balance=0,
                        customer_capacity=800,
                        merchant_capacity=25,
                    )
                )

                dealer_number += 1

        return dealers