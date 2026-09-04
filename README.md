# Discord Bot Template (Pycord)

A minimal Discord bot template using [Pycord](https://github.com/Pycord-Development/pycord) — just the essentials to get started.

## Requirements

- Python 3.10+
- A Discord bot token ([Discord Developer Portal](https://discord.com/developers/applications))

## Setup

```bash
# 1. Clone the repo
git clone https://github.com/<your-user>/<your-repo>.git
cd <your-repo>

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure your bot token
cp .env.example .env
# then put your token into .env

# 5. Run the bot
python main.py
```

## Usage

The bot comes with one example slash command: `/ping` → replies with `Pong!`.

To add your own commands, just add a new `@bot.slash_command(...)` in `main.py` and restart the bot.

## Project Structure

```
.
├── .env.example       # Environment variables template
├── .gitignore
├── main.py            # Bot entry point
└── requirements.txt   # Dependencies
```

## License

DevCoder-License
https://devcoder.is-a.dev
 - Modifying the file is allowed in this case.
 - Redistribution is also allowed in this case.
 - The sale or monetization of the content is strictly prohibited.
