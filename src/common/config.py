"""
Mobile Money Fraud Simulator

Module: Config Manager

Purpose:
Loads and validates the application configuration from YAML.

Author: Ranganath Acharya
Architecture: Ranganath
Version: 0.1.0
"""

from pathlib import Path

import yaml


class ConfigManager:
    """Loads application configuration."""

    def __init__(self):

        self.config = {}

        self.load()

    def load(self):
        """Read configuration from YAML."""

        config_file = Path("config/config.yaml")

        with open(config_file, "r", encoding="utf-8") as file:

            self.config = yaml.safe_load(file)

    def get(self):

        return self.config