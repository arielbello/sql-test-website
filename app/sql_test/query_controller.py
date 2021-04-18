from flask import session, current_app
import pandas as pd
from sqlalchemy import create_engine


answer = None
engine = None


def setup_engine():
    global engine
    if not engine:
        engine = create_engine(f"sqlite:///{current_app.config['DB_PATH']}",
                               echo=True)
    return engine


def run_query(statement: str) -> pd.DataFrame:
    engine = setup_engine()
    if session.get("query") == statement:
        # TODO return cache
        pass
    result = pd.read_sql(statement, engine)
    session["query"] = statement
    return result


def check_result(statement: pd.DataFrame) -> bool:
    engine = setup_engine()
    query = """
        SELECT G.device_cat, COUNT(DISTINCT g.user_id) FROM users U
        INNER JOIN google_users G ON G.user_id=U.user_id
            AND last_login LIKE '%2019-07%'
        GROUP BY device_cat
        ORDER BY COUNT(DISTINCT g.user_id)
    """
    rows = run_query(statement)
    global answer
    if not isinstance(answer, pd.DataFrame):
        answer = pd.read_sql(query, engine)

    return (answer.equals(rows))
