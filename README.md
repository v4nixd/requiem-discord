<h1 align="center">
    <a href="https://discord.gg/rqm">
        <img alt="Requiem Banner" src="./assets/requiem_banner.png" width="400">
    </a>
    <br>
    Requiem Discord Bot
</h1>

<p align="center">
    All-in-one server management bot
    <br><br>
    <img alt="GitHub License" src="https://img.shields.io/github/license/v4nixd/requiem-discord">
    <br>
    <img alt="Static Badge" src="https://img.shields.io/badge/Python-3.14-blue">
    <img alt="Static Badge" src="https://img.shields.io/badge/uv-0.9.18-fuchsia">
    <img alt="Static Badge" src="https://img.shields.io/badge/disnake-2.12.0-yellow">
    <br>
    <img alt="Static Badge" src="https://img.shields.io/badge/isort-7.0.0-orange">
    <img alt="Static Badge" src="https://img.shields.io/badge/ruff-0.15.0-purple">
    <img alt="Static Badge" src="https://img.shields.io/badge/taskipy-1.14.1-blue">
    <br>
    <img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/w/v4nixd/requiem-discord">
</p>

## 📖 Overview

| Feature      | Description                                                    |
| ------------ | -------------------------------------------------------------- |
| Python 3.14  | Latest Python version                                          |
| Disnake      | Powerful and flexible Discord API wrapper for building bots    |
| uv           | Ultra-fast Python package manager and virtual environment tool |
| Docker-ready | Prepared for Docker to simplify deployment and hosting         |

## 🚧 Project Status

> [!NOTE]
> Release! `v0.1.0`

## 📦 Version

`v0.1.0`

## 🛠️ Development Setup

1. ```bash
   git clone https://github.com/v4nixd/requiem-discord.git
   cd requiem-discord
   ```

2. ```bash
   uv sync
   ```

3. ```bash
   uv run task dev
   ```

### 🧪 Quality checks

- **Linter** - `uv run ruff check . --fix`
- **Formatter** - `uv run ruff format .`
- **Import sort** - `uv run isort .`
- **Type checking** - `uv run pyright`
- **Global check** - `uv run task check`

## 🚀 Deploy

1. ```bash
   git clone https://github.com/v4nixd/requiem-discord.git
   cd requiem-discord
   ```

2. ```bash
   echo "DISCORD_TOKEN=change_me" > .env
   ```

3. ```bash
   docker compose up -d --build
   ```

## 🔄 Updating

```bash
docker compose down
git pull
docker compose up -d --build
```

### 💻 Useful commands

- Container list - `docker compose ps`
- Restart - `docker compose restart`
- Stop - `docker compose down`
- Images list - `docker images`

## 📝 TODO

- [ ] Add Invisible nickname prevention

## 📃 License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

<br>

<p align="center">
    © 2026 v4nixd All Rights Reserved
</p>
