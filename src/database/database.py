from mario_utils import MariaDatabase
import os

db = MariaDatabase(
    server=os.getenv('DB_SERVER'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_SCHEMA')
)
