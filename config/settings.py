"""
Centralized configuration and constants for the AI services.
"""
import os
import logging

# Application constants
APP_NAME = os.getenv("APP_NAME", "falcon_ai_services")
APP_ENV = os.getenv("APP_ENV", "development")

# Logging configuration
LOG_LEVEL_STR = os.getenv("LOG_LEVEL", "INFO").upper()
# Safely get the log level, defaulting to INFO
LOG_LEVEL = getattr(logging, LOG_LEVEL_STR, logging.INFO)

# AI Service Settings Placeholder
# (Add specific model names, timeouts, retries, etc. here later)
