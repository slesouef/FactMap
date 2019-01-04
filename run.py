#! usr/bin/env python3
from bot import app
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    app.run()