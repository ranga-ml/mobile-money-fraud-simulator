"""
Reference Data Loader

Loads business reference data shared across all generators.
"""

from pathlib import Path

import yaml

from src.common.exceptions import ConfigurationError


class ReferenceData:
    """
    Singleton-style loader for static reference data.
    """

    _data = None

    @classmethod
    def load(cls):

        if cls._data is None:

            file_path = Path("config/reference_data.yaml")

            if not file_path.exists():
                raise ConfigurationError(
                    f"Reference data file not found: {file_path}"
                )

            with open(file_path, "r", encoding="utf-8") as file:
                cls._data = yaml.safe_load(file)

        return cls._data

    @classmethod
    def get(cls, key: str):

        data = cls.load()

        if key not in data:
            raise ConfigurationError(
                f"Reference data key '{key}' not found."
            )

        return data[key]