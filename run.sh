#!/bin/bash

echo "Installing dependencies..."

pip install -r requirements.txt

echo "Running Candidate Ranking..."

python main.py

echo "Done."
