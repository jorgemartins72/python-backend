from src.infra.config import DBConnectionHandler
from src.infra.entities import Users


class FakerRepo:
    """Repositório simples pra testar"""

    @classmethod
    def insert_user(cls):
        with DBConnectionHandler() as db_conn:
            try:
                new_user = Users(name="Jorge", password="senha")
                db_conn.session.add(new_user)
                db_conn.session.commit()
            except:
                db_conn.session.rollback()
                raise
            finally:
                db_conn.session.close()
