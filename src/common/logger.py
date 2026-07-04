"""
Logging Utility
"""

import sys

from loguru import logger


class Logger:

    _configured = False

    @classmethod
    def get_logger(cls):

        if not cls._configured:

            logger.remove()

            logger.add(
                sys.stdout,
                level="INFO",
                format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
                       "<level>{level: <8}</level> | "
                       "{message}",
            )

            cls._configured = True

        return logger