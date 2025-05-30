# Mocked BE for KML-NMEA Simulator

## Installation

Make sure you have Python installed and run the following commands in the root folder of this repository:

```bash
# Create a virtual environment
python -m venv venv # depending on what you're using, `python` could be `py` or `python3`

# Activate virtual environment
source venv/bin/activate # LINUX
.\venv\Scripts\Activate.ps1 # WINDOWS

# Install packages
pip install -r requirements.txt
```

## Starting

To run:

```bash
fastapi dev main.py
```

Check FastAPI's documentation for more info: https://fastapi.tiangolo.com/#run-it
