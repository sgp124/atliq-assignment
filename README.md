### Setup guide

1. install dependencies using `pip install requirements.txt`
2. create `data` directory in the project folder and add `xlsx` files there
3. set database connection string in `alembic.ini` file under `sqlalchemy.url`
4. execute from `/alembic` directory `alembic upgrade head` to run all database migrations
5. execute `run.sh` 