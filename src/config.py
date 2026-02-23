from __future__ import annotations

import os
import typing

import yaml

from dotenv import load_dotenv


class Config:
    _instance: Config | None = None

    CONFIG_FILE = "config.yaml"

    def __init__(self) -> None:
        load_dotenv()

        if not os.path.exists(Config.CONFIG_FILE):
            raise FileNotFoundError(f"{Config.CONFIG_FILE} not found.")

        with open(Config.CONFIG_FILE, "r", encoding="utf-8") as f:
            self.config = yaml.safe_load(f)

    @staticmethod
    def instance() -> Config:
        if not Config._instance:
            Config._instance = Config()
        return Config._instance

    def get_env_var(self, envvar: str) -> str:
        if envvar not in os.environ:
            raise ValueError(f"Environment variable '{envvar}' not found.")
        return os.environ[envvar]
