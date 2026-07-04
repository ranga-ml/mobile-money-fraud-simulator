"""
Entry point for the Mobile Money Fraud Simulator.
"""

from src.common.config import ConfigManager
import yaml


def load_config():
    """Load the YAML configuration file."""

    config_path = Path("config/config.yaml")

    with open(config_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def main():

    config = ConfigManager().get()

    print("=" * 50)
    print(f" {config['project']['name']}")
    print("=" * 50)

    print()

    print(f"Version             : {config['project']['version']}")
    print(f"Author              : {config['project']['author']}")

    print()

    print(f"Simulation Days     : {config['simulation']['days']}")
    print(f"Customers           : {config['population']['customers']:,}")
    print(f"Dealers             : {config['population']['dealers']:,}")
    print(f"Merchants           : {config['population']['merchants']:,}")

    print()
    print("Configuration loaded successfully.")


if __name__ == "__main__":
    main()