#!/bin/bash
python -m venv .venv;
source .venv/bin/activate;
pip install pip --upgrade;
pip install -r requirements.txt;
pre-commit install;

