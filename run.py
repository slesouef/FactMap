#! usr/bin/env python3
"""Launches the application

Load python-dotenv to retrieve API keys set in environment variables
Load Flask app module
"""
from dotenv import load_dotenv
from bot import APP


load_dotenv()

if __name__ == "__main__":
    APP.run()
