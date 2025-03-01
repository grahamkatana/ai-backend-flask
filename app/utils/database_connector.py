"""
+----------------------------------------------------------------------------
| Description
+----------------------------------------------------------------------------
| Get the connection string to the database
| Based on the driver, dynamically get the connection string
+----------------------------------------------------------------------------
"""

import os


def get_connection_string():
    env = os.getenv("ENV")
    if env == "production":
        driver: str = os.getenv("PROD_DATABASE_DRIVER")
        user: str = os.getenv("PROD_DATABASE_USER")
        password: str = os.getenv("PROD_DATABASE_PASSWORD")
        server: str = os.getenv("PROD_DATABASE_HOST")
        port: int = os.getenv("PROD_DATABASE_PORT")
        db_name: str = os.getenv("PROD_DATABASE_NAME")
        db_driver: dict = {"pgsql": "postgresql+psycopg2", "mysql": "mysql+pymysql"}
        return f"{db_driver[driver]}://{user}:{password}@{server}:{port}/{db_name}"
    else:
        driver: str = os.getenv("DATABASE_DRIVER")
        user: str = os.getenv("DATABASE_USER")
        password: str = os.getenv("DATABASE_PASSWORD")
        server: str = os.getenv("DATABASE_HOST")
        port: int = os.getenv("DATABASE_PORT")
        db_name: str = os.getenv("DATABASE_NAME")
        db_driver: dict = {"pgsql": "postgresql+psycopg2", "mysql": "mysql+pymysql"}
        return f"{db_driver[driver]}://{user}:{password}@{server}:{port}/{db_name}"
