from flask import session, current_app
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError


answer = None
engine = None


class DbResponse:
    def __init__(self, successful, result, accepted=False,
                 count=0, exec_time=-1):
        self.successful = successful
        self.result = result
        self.accepted = accepted
        self.exec_time = exec_time
        self.count = count


def setup_engine():
    global engine
    if not engine:
        engine = create_engine(f"sqlite:///{current_app.config['DB_PATH']}",
                               echo=True)
    return engine


def run_query(statement: str, fetchall=False) -> DbResponse:
    engine = setup_engine()
    try:
        result = pd.read_sql(statement, engine)
    except OperationalError as e:
        return DbResponse(False, e.orig.args[0])
    except Exception as e:
        return DbResponse(False, e.args[0])

    if not fetchall:
        result = result[:10]
    answer = expected_result()
    accepted = (answer.equals(result))
    return DbResponse(True, result, accepted, count=len(result))


def expected_result() -> pd.DataFrame:
    engine = setup_engine()
    query = """
        SELECT G.device_cat, COUNT(DISTINCT g.user_id) FROM users U
        INNER JOIN google_users G ON G.user_id=U.user_id
            AND last_login LIKE '%2019-07%'
        GROUP BY device_cat
        ORDER BY COUNT(DISTINCT g.user_id)
    """
    global answer
    if not isinstance(answer, pd.DataFrame):
        answer = pd.read_sql(query, engine)

    return answer
