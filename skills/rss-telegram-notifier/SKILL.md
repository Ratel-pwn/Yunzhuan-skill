---
name: rss-telegram-notifier
description: Automatically check RSS feeds and push new articles to Telegram; use this skill whenever you need to subscribe to feeds, monitor updates, send notifications, set up RSS-to-Telegram pipelines, or create automated news/blog alert bots.
---

# RSS Telegram Notifier

Automatically check RSS feeds and push new articles to a Telegram channel or group.

## Scope & Boundaries

- Applicable: Automatically push updates from one or more RSS/Atom feeds to Telegram.
- Not applicable: Complex filtering (keywords, tag priorities), multi-platform distribution, rich-media formatting.
- Runtime dependency: Python 3 (standard library only, no third-party packages).

## Quick Start

All commands below default to running in the `skills/rss-telegram-notifier/` directory.

### 1. Configure `config.json`

Copy the template and edit it:

```bash
cp assets/config.json.template config.json
```

Edit `config.json`:

```json
{
  "telegram": {
    "bot_token": "YOUR_BOT_TOKEN",
    "chat_id": "YOUR_CHAT_ID"
  },
  "feeds": [
    {
      "url": "https://example.com/feed.xml",
      "max_entries": 5
    }
  ],
  "settings": {
    "check_interval_minutes": 60,
    "state_file": "rss_state.json",
    "silent_notifications": false
  }
}
```

### 2. Obtain Telegram Configuration

**Bot Token:**
- Find @BotFather on Telegram
- Send `/newbot` to create a new bot
- Copy the token it provides

**Chat ID:**
- Send a message to your channel/group
- Visit `https://api.telegram.org/bot<TOKEN>/getUpdates`
- Locate the number in `"chat":{"id":123456789`

### 3. Manually Check and Send

```bash
# Check for new articles
python3 scripts/rss_checker.py config.json rss_state.json

# Send new articles to Telegram
python3 scripts/telegram_sender.py <BOT_TOKEN> <CHAT_ID> '<ARTICLES_JSON>'
```

You can also chain the commands in a single pipeline:

```bash
python3 scripts/rss_checker.py config.json rss_state.json \
  | python3 scripts/telegram_sender.py <BOT_TOKEN> <CHAT_ID> -
```

### 4. Set Up a Scheduled Task

Use cron or another scheduling tool:

```bash
# Check once every hour
0 * * * * cd /path/to/skill && python3 scripts/rss_checker.py config.json rss_state.json | python3 scripts/telegram_sender.py BOT_TOKEN CHAT_ID -
```

## Message Format

### Single Article Push (≤3 articles)
```
📰 Article Title

Article summary...

📎 Read Original
📌 Source Name
🕐 Published Time
```

### Multi-Article Digest (>3 articles)
```
📬 Today's Updates (X articles)

1. Article Title 1
   Read Original | 📌 Source

2. Article Title 2
   Read Original | 📌 Source
```

## Input/Output Contract

### rss_checker.py

- Input: `<config.json> <state.json>`
- Output: Prints a JSON array of new articles to stdout
- Side effect: Updates `state.json` for deduplication

### telegram_sender.py

- Input: `<bot_token> <chat_id> <articles_json | ->`
- Output: Prints `Successfully sent X article(s)` on success
- Failure: Prints error to stderr and exits with a non-zero code

## Script Reference

### rss_checker.py

Check RSS feeds, return new articles, and update state.

```bash
python3 scripts/rss_checker.py <config.json> <state.json>
# Output: JSON array to stdout
```

### telegram_sender.py

Send formatted articles to Telegram.

```bash
# Read from argument
python3 scripts/telegram_sender.py <token> <chat_id> '<json_array>'

# Read from stdin (for piping)
echo '[{...}]' | python3 scripts/telegram_sender.py <token> <chat_id> -
```

## Configuration Reference

| Field | Description |
|-------|-------------|
| `telegram.bot_token` | Telegram Bot Token |
| `telegram.chat_id` | Target channel/group ID |
| `feeds[].url` | RSS feed URL |
| `feeds[].max_entries` | Maximum number of entries per check |
| `settings.check_interval_minutes` | Recommended check interval |
| `settings.state_file` | Suggested state file name (the script currently uses the command-line argument) |
| `settings.silent_notifications` | Reserved field (not currently read by the script) |

## Dependencies

Implemented using only the Python standard library — no extra installation required:
- `urllib.request` — HTTP requests
- `xml.etree.ElementTree` — RSS parsing
- `hashlib`, `json` — Data processing
