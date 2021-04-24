import pandas as pd
from sqlalchemy import create_engine


def format_dates(df):
    dt = df.select_dtypes(include=['datetime64'])
    for col in dt.columns:
        df[col] = df[col].astype('string')
        df[col] = list(map(lambda x: None if x == "NaT" else x, df[col]))
        df[col] = list(map(lambda x: x[:16] if x else None, df[col]))


engine = create_engine("sqlite:///test.db", echo=True)

users = pd.read_csv("users.csv", parse_dates=[2, 3], dayfirst=True)
g_users = pd.read_csv("google_users.csv", parse_dates=[3], dayfirst=True)
format_dates(users)
format_dates(g_users)

users.to_sql("users", engine, index=False, if_exists="replace")
g_users.to_sql("google_users", engine, index=False, if_exists="replace")
