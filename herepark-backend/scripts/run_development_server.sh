#!/bin/bash
export APP_DB_PASSWORD=hppass
export APP_DB_USER=hpuser
export APP_DB_NAME=hereparkdb

poetry run uvicorn app.main:app --reload --host "0.0.0.0" --port 5000
