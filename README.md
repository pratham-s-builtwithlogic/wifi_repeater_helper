# Smart Wi-Fi Repeater Deployment Helper

## Problem
Many homes and schools use old routers that fail beyond channel 48 on 2.4GHz. Teachers often face disconnection issues during online classes.

## Solution
This Python script helps:
- Scan current Wi-Fi environment
- Recommend optimal repeater placement
- Log configurations in a local MySQL database

## Tech Stack
- Python
- MySQL
- `socket`, `platform`, `subprocess` (cross-platform support)
- `mysql-connector-python`

## Features
- Detect current network channel
- Guide to set up repeaters
- Store historical setups for reuse

## Setup
1. Install dependencies: `pip install mysql-connector-python`
2. Setup your MySQL server and create the database using `wifi_repeater_helper/schema.sql`
3. Run: `python repeater_helper.py`

## Screenshots
_Include screenshots of terminal and repeater location guides here_

## Files
- `repeater_helper.py`: Main script
- `schema.sql`: MySQL table schema
- `README.md`: This file

## Future Improvements
- Auto-detect old routers
- Add GUI
- Export setup to PDF
