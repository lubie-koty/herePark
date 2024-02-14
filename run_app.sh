export APP_DB_PASSWORD=hppass
export APP_DB_USER=hpuser
export APP_DB_NAME=hereparkdb

docker compose -f docker-compose.yml up --build --always-recreate-deps
