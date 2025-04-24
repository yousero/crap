import sqlite3

from sqlmodel import SQLModel, Field, create_engine, Session
from faker import Faker
from typing import Optional
from datetime import datetime


class User(SQLModel, table=True):
  id: Optional[int] = Field(default=None, primary_key=True)
  name: str
  email: str
  created_at: datetime


def create_db_and_fake_data(db_file: str, num_records: int = 10):
  engine = create_engine(f'sqlite:///{db_file}')

  SQLModel.metadata.create_all(engine)

  fake = Faker()

  with Session(engine) as session:
    for _ in range(num_records):
      user = User(
        name=fake.name(),
        email=fake.email(),
        created_at=fake.date_time_this_year()
      )
      session.add(user)
    session.commit()


def backup_db_to_sql(db_file: str, sql_file: str):
  try:
    conn = sqlite3.connect(db_file)
    
    with open(sql_file, 'w') as f:
      for line in conn.iterdump():
        f.write(f'{line}\n')
    
  except sqlite3.Error as e:
    print(f'Error: {e}')
  finally:
    if conn:
      conn.close()


if __name__ == '__main__':
  db_file = 'example.db'
  sql_file = 'backup.sql'
  num_fake_records = 5

  create_db_and_fake_data(db_file, num_fake_records)
  
  backup_db_to_sql(db_file, sql_file)
