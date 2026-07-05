"""
Entity Registry

Maintains all entities and relationships generated during the simulation.
"""

from collections import defaultdict


class EntityRegistry:
    """
    Central in-memory registry for all simulator entities.
    """

    def __init__(self):

        # Master objects
        self.dealers = {}
        self.customers = {}
        self.merchants = {}
        self.wallets = {}
        self.devices = {}
        self.sims = {}

        # Relationships
        self.dealer_to_customers = defaultdict(list)
        self.dealer_to_merchants = defaultdict(list)

        self.customer_to_wallet = {}
        self.customer_to_device = {}
        self.customer_to_sim = {}

    # ----------------------------------------------------
    # Dealer
    # ----------------------------------------------------

    def register_dealer(self, dealer):

        self.dealers[dealer.dealer_id] = dealer

    # ----------------------------------------------------
    # Customer
    # ----------------------------------------------------

    def register_customer(self, customer):

        self.customers[customer.customer_id] = customer

        self.dealer_to_customers[
            customer.dealer_id
        ].append(customer.customer_id)

        self.customer_to_wallet[
            customer.customer_id
        ] = customer.wallet_id

        self.customer_to_device[
            customer.customer_id
        ] = customer.device_id

        self.customer_to_sim[
            customer.customer_id
        ] = customer.sim_id

    # ----------------------------------------------------
    # Merchant
    # ----------------------------------------------------

    def register_merchant(self, merchant):

        self.merchants[
            merchant.merchant_id
        ] = merchant

        self.dealer_to_merchants[
            merchant.dealer_id
        ].append(merchant.merchant_id)

    # ----------------------------------------------------
    # Query Helpers
    # ----------------------------------------------------

    def get_customers_for_dealer(self, dealer_id):

        return self.dealer_to_customers.get(
            dealer_id,
            [],
        )

    def get_wallet(self, customer_id):

        return self.customer_to_wallet.get(customer_id)

    def get_device(self, customer_id):

        return self.customer_to_device.get(customer_id)

    def get_sim(self, customer_id):

        return self.customer_to_sim.get(customer_id)

    # ----------------------------------------------------
    # Statistics
    # ----------------------------------------------------

    def summary(self):

        return {

            "dealers": len(self.dealers),

            "customers": len(self.customers),

            "merchants": len(self.merchants),

            "wallets": len(self.wallets),

            "devices": len(self.devices),

            "sims": len(self.sims),
        }