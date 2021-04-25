import time
import pandas as pd
from flask import current_app
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError


answer = None
engine = None


class DbResponse:
    def __init__(self, successful, result=None, accepted=False, errormsg="",
                 count=0, exec_time=-1):
        self.successful = successful
        self.result = result
        self.errormsg = errormsg
        self.accepted = accepted
        self.exec_time = exec_time
        self.count = count


def setup_engine():
    global engine
    if not engine:
        dbpath = f"sqlite:///{current_app.config['TEST_DB_PATH']}"
        engine = create_engine(dbpath, echo=False)
    return engine


def run_query(statement: str, fetchall=False) -> DbResponse:
    engine = setup_engine()
    try:
        exec_time = -1
        start_time = time.time()
        result = pd.read_sql(statement, engine)
        exec_time = time.time() - start_time
    except OperationalError as e:
        return DbResponse(False, errormsg=e.orig.args[0], exec_time=exec_time)
    except Exception as e:
        return DbResponse(False, errormsg=e.args[0], exec_time=exec_time)

    accepted = check_result(result)
    count = len(result)
    if not fetchall:
        result = result.iloc[:10]
    if "index" in result.columns:
        result.drop("index", axis=1, inplace=True)
    return DbResponse(True, result, accepted=accepted, count=count,
                      exec_time=exec_time)


def check_result(df) -> bool:
    original_cols = df.columns
    # Normalizing columns so column names don't affect results
    df.columns = [i for i in range(len(original_cols))]
    answer = expected_result()
    accepted = answer.equals(df)
    df.columns = original_cols

    return accepted


def expected_result() -> pd.DataFrame:
    engine = setup_engine()
    query = """
        SELECT G.device_cat, COUNT(DISTINCT g.user_id) FROM users U
        INNER JOIN google_users G ON G.user_id=U.user_id
              AND last_login LIKE '%2019-07%'
        GROUP BY device_cat
        ORDER BY COUNT(DISTINCT g.user_id) DESC
        """
    global answer
    if not isinstance(answer, pd.DataFrame):
        answer = pd.read_sql(query, engine)
        # Normalizing columns so column names don't affect results
        answer.columns = [i for i in range(len(answer.columns))]

    return answer
