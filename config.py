"""server config file"""
import os


SECRET_KEY = os.getenv("SECRET_KEY")

# Google API
MAPS_API = os.getenv("JSMAPS_KEY")
