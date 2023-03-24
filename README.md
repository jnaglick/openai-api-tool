# 💬 OpenAI API Tool

Small wrapper of OpenAI API (Set to ChatGPT-3.5) for: 

* using when the web interface is having problems
* using system and assistant/user pairs (api only feature)
* executing slightly more verbose prompts
* easily saving conversations locally

## Setup:

0. Sign up / get your API key: https://platform.openai.com/signup

0. Create the env file: `cp .env.example .env`, put your API key where specified

0. Install deps (Use a python venv/etc, if you want): `pip3 install -r requirements.txt`

0. Run: `python ./prompt.py`

## Usages:

1. Just fill out the `user()`, `system()` and `examples()` functions as desired.

2. To save answers: `python ./prompt.py > answers`
