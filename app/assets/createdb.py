import pandas as pd
from sqlalchemy import create_engine


engine = create_engine("sqlite:///test.db", echo=True)

users = pd.read_csv("users.csv", parse_dates=[2, 3], dayfirst=True)
g_users = pd.read_csv("google_users.csv", parse_dates=[3], dayfirst=True)

users.to_sql("users", engine)
g_users.to_sql("google_users", engine)
