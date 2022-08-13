from src.infra.config import DBConnectionHandler
from src.infra.entities import Users
from collections import namedtuple


class UserRepository:
    @classmethod
    def insert_user(cls, name: str, password: str) -> Users:

        data = namedtuple("Users", "id, name, password")

        with DBConnectionHandler() as db_conn:
            try:
                new_user = Users(name=name, password=password)
                db_conn.session.add(new_user)
                db_conn.session.commit()

                return data(
                    id=new_user.id, name=new_user.name, password=new_user.password
                )

            except:
                db_conn.session.rollback()
                raise
            finally:
                db_conn.session.close()

        return None
