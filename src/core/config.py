from __future__ import annotations

import os
from typing import Any

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

    def get_var(self, path: str) -> Any:
        keys = path.split(".")
        data = self.config
        for key in keys:
            if key not in data:
                raise KeyError(f"Key '{key}' not found in config.")
            data = data[key]
        return data

    def set_var(self, path: str, value) -> None:
        self._set_value(self.config, path, value)
        with open(Config.CONFIG_FILE, "w", encoding="utf-8") as f:
            yaml.safe_dump(self.config, f)

    def get_env_var(self, envvar: str) -> str:
        if envvar not in os.environ:
            raise ValueError(f"Environment variable '{envvar}' not found.")
        return os.environ[envvar]

    def _set_value(self, data, path, value) -> None:
        keys = path.split(".")
        for key in keys[:-1]:
            if key not in data:
                data[key] = {}
            data = data[key]
        data[keys[-1]] = value
