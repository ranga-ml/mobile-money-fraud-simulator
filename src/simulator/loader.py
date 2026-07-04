"""
Country Loader
"""

from pathlib import Path

import yaml

from src.simulator.country import Country
from src.simulator.country import Region


class CountryLoader:

    @staticmethod
    def load():

        file = Path("config/regions.yaml")

        with open(file, "r", encoding="utf-8") as f:

            data = yaml.safe_load(f)

        regions = []

        for region in data["regions"]:

            regions.append(

                Region(

                    name=region["name"],

                    urban_ratio=region["urban_ratio"],

                    income_multiplier=region["income_multiplier"],

                    dealer_density=region["dealer_density"],

                    fraud_risk=region["fraud_risk"],
                )
            )

        return Country(

            name=data["country"]["name"],

            currency=data["country"]["currency"],

            population=data["country"]["population"],

            mobile_money_users=data["country"]["mobile_money_users"],

            regions=regions,
        )