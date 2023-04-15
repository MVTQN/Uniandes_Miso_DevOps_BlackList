#!/bin/bash
export FLASK_APP=./src/app.py
pipenv run flask run -h 0.0.0.0 --port=3000