# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

import json
import psycopg2

from typing import Optional

from fastapi import FastAPI

# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:password@localhost:5432/books'

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()


connection = psycopg2.connect(
    host='localhost',
    database='fastdb',
    user='postgres',
    password='postgres'
)
print('connection:', connection)

cursor = connection.cursor()
print('cursor:', cursor)

# cursor.execute(
#     """
#     CREATE TABLE readings (
#         id INTEGER PRIMARY KEY,
#         humidity INTEGER
#     )
#     """
# )
# cursor.close()
# connection.commit()

app = FastAPI()


@app.get('/')
async def read_root():
    cursor.execute(
        """
        SELECT * FROM readings
        """
    )
    str_with_quotes = str([dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in cursor.fetchall()])
    str_with_quotes = str_with_quotes.replace("'",'"')
    return json.loads(str_with_quotes)