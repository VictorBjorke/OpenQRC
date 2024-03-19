#!/bin/bash

# Check OS Version
OS="$(uname)"
echo "Detected OS: $OS"

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "Python 3 could not be found. Please install Python 3."
    exit 1
fi

# Print Python version
echo "Python version: $(python3 --version)"

# Define GitHub URLs for the specific files
QCODES_URL="https://raw.githubusercontent.com/VictorBjorke/OpenQRC/main/qcodes.json"
OPENQRC_URL="https://raw.githubusercontent.com/VictorBjorke/OpenQRC/main/openqrc.py"

# Define download directory
DOWNLOAD_DIR="$HOME/OpenQRC"
mkdir -p $DOWNLOAD_DIR

# Download the specific files
echo "Downloading qcodes.json and openqrc.py..."
curl -o $DOWNLOAD_DIR/qcodes.json $QCODES_URL
curl -o $DOWNLOAD_DIR/openqrc.py $OPENQRC_URL


echo "Files downloaded to $DOWNLOAD_DIR."
